from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import stripe

class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    # def has_active_subscription(self):
    #     """
    #     Returns True if the customer has an active subscription, False otherwise.
    #     """
    #     if not self.stripeSubscriptionId:
    #         return False

    #     try:
    #         stripe.api_key = settings.STRIPE_SECRET_KEY
    #         subscription = stripe.Subscription.retrieve(self.stripeSubscriptionId)
    #         return subscription.status == 'active'
    #     except stripe.error.StripeError:
    #         return False  # Safely handle Stripe API errors

    def __str__(self):
        return self.user.username


