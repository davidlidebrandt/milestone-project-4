from django.shortcuts import render
import stripe
from django.conf import settings
from django.http import JsonResponse


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
YOUR_DOMAIN = "http://127.0.0.1:8000/"


def create_checkout(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Stubborn Attachments',
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({"error": f"{e}"})
