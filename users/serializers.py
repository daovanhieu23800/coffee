from rest_framework import serializers
from users.models import account

class accountSerializers(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = '__all__'