from rest_framework import serializers
from coffee_app.models import Item

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'