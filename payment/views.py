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
import uuid


# The Stripe docs and another tutotial was uses as the base for this code.
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
        current_datetime = datetime.datetime.now()
        meta_data = {"date": current_datetime, "user_id": user_id}
        line_items = []
        bag = request.session.get("shopping_bag")
        bag.pop("total_cost")
        count = 0
        for item in bag.items():
            product = {"name": "", "quantity": "", "currency": "usd",
                       "amount": ""}
            for product_field in item:
                if type(product_field) is not dict:
                    db_product = get_object_or_404(Product, id=product_field)
                    product["name"] = db_product.name
                    product["amount"] = str(db_product.prize * 100)
                else:
                    for value in product_field.values():
                        product["quantity"] = value
            meta_data["products"]["product" + str(count)] = db_product.id
            count += 1
            line_items.append(product)
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url="https://fitness-equipment.herokuapp.com/payment/success/",
                cancel_url="https://fitness-equipment.herokuapp.com/payment/error/",
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


# The Stripe docs and another tutotial was uses as the base for this code.
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
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event["type"] == 'checkout.session.completed':
        send_mail(
            "Your order",
            "Your order was successful",
            None,
            [event["data"]["object"]["customer_email"]],
            fail_silently=False,)
        order_id = uuid.uuid4
        user_id = event["data"]["object"]["metadata"]["user_id"]
        order = None
        if user_id:
            user = get_object_or_404(User, id=user_id)
            order = Order(id=order_id,
                          date=event["data"]["object"]["metadata"]["date"],
                          user=user, amount_paid=event["data"]["object"]["amount_total"],
                          shipping_address=event["data"]["object"]["shipping"]["address"],
                          customer_name=event["data"]["object"]["customer_email"],
                          customer_email=event["data"]["object"]["shipping"]["name"])
        else:
            order = Order(id=order_id,
                          date=event["data"]["object"]["metadata"]["date"],
                          amount_paid=event["data"]["object"]["amount_total"],
                          shipping_address=event["data"]["object"]["shipping"]["address"],
                          customer_name=event["data"]["object"]["customer_email"],
                          customer_email=event["data"]["object"]["shipping"]["name"])
        order.save()

    return HttpResponse(status=200)


def payment_success(request):
    return render(request, "payment/success.html")


def payment_error(request):
    return render(request, "payment/error.html")
