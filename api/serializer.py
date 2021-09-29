from django.db.models import fields
from rest_framework import routers, serializers, viewsets
from dashboard.models import Product,Order
from user.models import Profile




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'