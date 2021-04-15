from django.shortcuts import render
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe


# The Stripe docs and another tutotial was uses as the base for this code.
# https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout#redirect-customers
# https://testdriven.io/blog/django-stripe-tutorial/
@csrf_exempt
def create_checkout(request):
    if request.method == "POST":
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url="https://fitness-equipment.herokuapp.com/payment/success/",
                cancel_url="https://fitness-equipment.herokuapp.com/payment/error/",
                payment_method_types=["card"],
                mode="payment",
                line_items=[
                    {
                        "name": 'Basic Barbell',
                        "quantity": 1,
                        "currency": 'usd',
                        "amount": '10000',
                    }
                ]
            )
            print(checkout_session)
            return JsonResponse({'sessionId': checkout_session["id"]})
        except Exception as e:
            return JsonResponse({"error": str(e)})
