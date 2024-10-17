from django.shortcuts import render
from .models import UserProfile, StripeCustomer

def profile(request):
    """ Display users profile """
    try:
        # Get the user's Stripe subscription status
        stripe_customer = StripeCustomer.objects.get(user=request.user)

        # Determine if the user has an active subscription
        is_subscribed = stripe_customer.has_active_subscription()

    except StripeCustomer.DoesNotExist:
        # If no StripeCustomer exists, the user is not subscribed
        is_subscribed = False

    template = 'profiles/profiles.html' 
    context = {
        'is_subscribed': is_subscribed,
        }

    return render(request, template, context)