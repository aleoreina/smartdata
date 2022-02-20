from rest_framework import serializers
from core.models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
   class Meta:
       model = Subscription
       fields = ('email', )

