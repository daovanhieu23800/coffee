from rest_framework import serializers
from users.models import account, customer

class accountSerializers(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = '__all__'

class customerSerializers(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'