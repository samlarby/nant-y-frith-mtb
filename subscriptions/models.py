from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime, timedelta
import stripe

class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)
    current_period_end = models.DateTimeField(null=True)

    def has_active_subscription(self):
        """
        Returns True if the customer has an active subscription, False otherwise.
        """
        if not self.stripeSubscriptionId:
            return False

        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            subscription = stripe.Subscription.retrieve(self.stripeSubscriptionId)
            self.current_period_end = subscription['current_period_end'] # updates period end
            return subscription.status == 'active'
        except stripe.error.StripeError:
            return False  # Safely handle Stripe API errors
    
    # calcculate remaining time until next renewal 
    def time_until_renewal(self):
        if self.current_period_end:
            now = datetime.now(tz=self.current_period_end.tzinfo)
            remaining_time = self.current_period_end - now
            return remaining_time
        return timedelta(0)

    def __str__(self):
        return self.user.username


