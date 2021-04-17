from django.shortcuts import render, HttpResponse, get_object_or_404
from django.conf import settings
from django.http.response import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
import stripe


# The Stripe docs and another tutotial was uses as the base for this code.
# https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout#redirect-customers
# https://testdriven.io/blog/django-stripe-tutorial/
@csrf_exempt
def create_checkout(request):
    if request.method == "POST":
        customer_email = []
        if request.user.is_authenticated:
            customer_email.append(request.user.email)
        line_items = []
        bag = request.session.get("shopping_bag")
        bag.pop("total_cost")
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
            line_items.append(product)
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url="https://fitness-equipment.herokuapp.com/payment/success/",
                cancel_url="https://fitness-equipment.herokuapp.com/payment/error/",
                payment_method_types=["card"],
                customer_email=[],
                shipping_address_collection={'allowed_countries': ["SE"]},
                mode="payment",
                line_items=line_items
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

    if event['type'] == 'checkout.session.async_payment_succeeded':
        send_mail(
            "Your order",
            "Your oder was successful",
            None,
            ["dl_brd@hotmail.com"],
            fail_silently=False,)

    return HttpResponse(status=200)


def payment_success(request):
    line_items = []
    bag = request.session.get("shopping_bag")
    total_cost = bag.get("total_cost")
    bag.pop("total_cost")
    for item in bag.items():
        product = {"name": "", "quantity": "", "currency": "usd", "amount": ""}
        for i in item:
            if type(i) is not dict:
                db_product = get_object_or_404(Product, id=i)
                product["name"] = db_product.name
                product["amount"] = str(db_product.prize * 10)
            else:
                for value in i.values():
                    product["quantity"] = value
        line_items.append(product)

    return render(request, "payment/success.html")


def payment_error(request):
    return render(request, "payment/error.html")
