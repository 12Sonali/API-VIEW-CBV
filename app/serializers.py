from rest_framework import serializers
from app.models import *
class ProductcategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Productcategory
        fields='__all__'
        


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'