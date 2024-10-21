import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import StripeCustomer


@login_required
def subscribe(request):
    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)

        return render(request, 'subscribe/subscribe.html', {
            'subscription': subscription,
            'product': product,
        })

    except StripeCustomer.DoesNotExist:
        return render(request, 'subscribe/subscribe.html')

@login_required
def unsubscribe(request):
    try:
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)

        # cancel the subscription
        stripe.Subscription.delete(subscription.id)
        stripe_customer.delete()

        subject = 'Unsubscribe Confirmation'
        message = render_to_string('subscribe/email/unsubscription-confirmation.txt', {
            'user': request.user,
        })
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],
            fail_silently=False,
        )

        return redirect('unsubscribe_confirmation')  # Redirect to the subscription page or wherever you prefer
    except StripeCustomer.DoesNotExist:
        return redirect('subscriptions-subscribe')
    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return redirect('subscriptions-subscribe')


@login_required
def unsubscribe_confirmation(request):
    """Render a confirmation page after the user has unsubscribed"""
    return render(request, 'subscribe/unsubscribe-confirmation.html')


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        if request.get_host().startswith("localhost") or "gitpod.io" in request.get_host():
            domain_url = 'https://8000-samlarby-nantyfrithmtb-cc7bzg8jhc8.ws-eu116.gitpod.io/'  # Use Gitpod URL in dev
        else:
            domain_url = 'https://nant-y-frith-mtb-b55326ff08d0.herokuapp.com/'  # So users are directed back to the heroku app and not to gitpod when they subscribe

        stripe.api_key = settings.STRIPE_SECRET_KEY # automatically send request to create a new Checkout session
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'subscriptions/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'subscriptions/cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[    
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1, 
                    },
                ],
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

@login_required
def success(request):
    return render(request, 'subscribe/success.html')

@login_required
def cancel(request):
    return render(request, 'subscribe/cancel.html')

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']  
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new StripeCustomer
        stripe_customer, created = StripeCustomer.objects.get_or_create(
            user=user,
            defaults={
                'stripeCustomerId': stripe_customer_id,
                'stripeSubscriptionId': stripe_subscription_id,
                'current_period_end': datetime.fromtimestamp(session['current_period_end']),  # Save the renewal date
            }
        )

        # if customer already exists
        if not created:
            stripe_customer.stripeCustomerId = stripe_customer_id
            stripe_customer.stripeSubscriptionId = stripe_subscription_id
            stripe_customer.current_period_end = datetime.fromtimestamp(session['current_period_end'])
            stripe_customer.save()


        print(user.username + ' just subscribed.')


        subject = 'Subscription Confirmation'
        message = render_to_string('subscribe/email/subscription-confirmation.txt', {
                'user': user,
                'subscription_id': stripe_subscription_id,
        })
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

    return HttpResponse(status=200)
