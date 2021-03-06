from django.shortcuts import render, HttpResponse, get_object_or_404
from django.conf import settings
from django.http.response import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from products.models import Product
from . models import Order, OrderItem
import stripe
import datetime


# The Stripe docs and another tutorial was uses as the base for this code.
# https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout#redirect-customers
# https://testdriven.io/blog/django-stripe-tutorial/
@csrf_exempt
def create_checkout(request):
    if request.method == "POST":
        customer_email = ""
        user_id = None
        if request.user.is_authenticated:
            customer_email = request.user.email
            user_id = request.user.id
        meta_data = {"user_id": user_id, }
        line_items = []
        bag = request.session.get("shopping_bag")
        bag.pop("total_cost")
        count = 0
        for item in bag.items():
            product = {"name": "", "quantity": "", "currency": "usd",
                       "amount": ""}
            quantity = ""
            for product_field in item:
                if type(product_field) is not dict:
                    db_product = get_object_or_404(Product, id=product_field)
                    if db_product.discount_rate:
                        db_product.prize = int(
                            db_product.prize * db_product.discount_rate.rate)
                    product["name"] = db_product.name
                    product["amount"] = str(db_product.prize * 100)
                else:
                    for value in product_field.values():
                        product["quantity"] = value
                        quantity = str(value)
            meta_data[str(db_product.id)] = quantity
            count += 1
            line_items.append(product)
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        if request.user.is_authenticated:
            try:
                checkout_session = stripe.checkout.Session.create(
                    success_url=("https://fitness-equipment.herokuapp.com" +
                                 "/payment/success/"),
                    cancel_url=("https://fitness-equipment.herokuapp.com" +
                                "/payment/error/"),
                    payment_method_types=["card"],
                    customer_email=customer_email,
                    shipping_address_collection={'allowed_countries': ["SE"]},
                    mode="payment",
                    line_items=line_items,
                    metadata=meta_data,
                )
                return JsonResponse({'sessionId': checkout_session["id"]})
            except Exception as e:
                return JsonResponse({"error": str(e)})
        else:
            try:
                checkout_session = stripe.checkout.Session.create(
                    success_url=("https://fitness-equipment.herokuapp.com" +
                                 "/payment/success/"),
                    cancel_url=("https://fitness-equipment.herokuapp.com" +
                                "/payment/error/"),
                    payment_method_types=["card"],
                    shipping_address_collection={'allowed_countries': ["SE"]},
                    mode="payment",
                    line_items=line_items,
                    metadata=meta_data,)
                return JsonResponse({'sessionId': checkout_session["id"]})
            except Exception as e:
                return JsonResponse({"error": str(e)})


# The Stripe docs and another tutorial was uses as the base for this code.
# https://stripe.com/docs/payments/handling-payment-events
# https://testdriven.io/blog/django-stripe-tutorial/
@csrf_exempt
def confirmation_of_payment(request):
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event["type"] == 'checkout.session.completed':
        try:
            user_id = event["data"]["object"]["metadata"]["user_id"]
        except KeyError:
            user_id = None
        order = None
        current_date = datetime.datetime.now()
        amount_paid = int(event["data"]["object"]["amount_total"])/100
        city = event["data"]["object"]["shipping"]["address"]["city"]
        street = event["data"]["object"]["shipping"]["address"]["line1"]
        code = event["data"]["object"]["shipping"]["address"]["postal_code"]
        shipping_address = city + " " + street + " " + code
        customer_email = event["data"]["object"]["customer_details"]["email"]
        customer_name = event["data"]["object"]["shipping"]["name"]
        if user_id:
            user = get_object_or_404(User, id=user_id)
            order = Order(
                          date=current_date,
                          user=user,
                          amount_paid=amount_paid,
                          shipping_address=shipping_address,
                          customer_email=customer_email,
                          customer_name=customer_name)
        else:
            order = Order(
                          date=current_date,
                          amount_paid=amount_paid,
                          shipping_address=shipping_address,
                          customer_email=customer_email,
                          customer_name=customer_name)
        order_id = order.id
        order_name = order.customer_name
        order_total = order.amount_paid
        order.save()

        product_list = event["data"]["object"]["metadata"]
        try:
            product_list.pop("user_id")
        except KeyError:
            product_list = event["data"]["object"]["metadata"]

        message = (f"Hi {order_name}\n Your order {order_id} was successfull" +
                   ", below you will find the details of your order.\n" +
                   f"\ntotal cost: {order_total} dollars")

        for key, value in product_list.items():
            order = get_object_or_404(Order, id=order_id)
            product = get_object_or_404(Product, id=key)
            units_sold = int(value) + product.units_sold
            product.units_sold = units_sold
            product.save()

            new_item = OrderItem(product=product, order=order, quantity=value)
            message += f"\nProduct: {product.name}, quantity: {value}"
            new_item.save()

        message += "\n"
        message += "\nQuestions? contact us at fitness.equipment.fe@gmail.com"
        send_mail(
            "Your order",
            message,
            None,
            [customer_email],
            fail_silently=True,)

    return HttpResponse(status=200)


def payment_success(request):
    try:
        del request.session["shopping_bag"]
    except KeyError:
        request.session["shopping_bag"] = {}
    return render(request, "payment/success.html")


def payment_error(request):
    return render(request, "payment/error.html")
