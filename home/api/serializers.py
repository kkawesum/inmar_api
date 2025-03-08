from rest_framework import serializers
from metadata.models import Sku, SubCategory, Category, Location, Department


class SkuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sku
        fields = "__all__"
        

class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = "__all__"
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"
class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"
