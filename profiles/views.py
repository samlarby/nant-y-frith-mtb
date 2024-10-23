from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, StripeCustomer
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


def profile(request):
    """Display users profile"""
    user = request.user  # get user

    profile, created = UserProfile.objects.get_or_create(user_id=user.id)

    if not user.is_authenticated:
        return redirect('login')

    is_subscribed = False
    renewal_date_formatted = "N/A"  # Initialize with a default value

    try:
        # Get the user's Stripe subscription status
        stripe_customer = StripeCustomer.objects.get(user_id=user.id)

        # Determine if the user has an active subscription
        is_subscribed = stripe_customer.has_active_subscription()

        if stripe_customer.current_period_end:
            renewal_date_formatted = stripe_customer.current_period_end.strftime(
                "%d.%m.%Y"
            )

    except StripeCustomer.DoesNotExist:
        # No StripeCustomer exists, user is not subscribed
        pass

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserProfileForm(instance=profile)

    context = {
        "is_subscribed": is_subscribed,
        "renewal_date": renewal_date_formatted,
        "form": form,
        "user_profile": profile,
    }

    template = "profiles/profiles.html"
    return render(request, template, context)
