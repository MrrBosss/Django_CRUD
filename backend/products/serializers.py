from rest_framework import serializers
from .models import Product, FAQ, Banner, Brand, ProductWeight, ProductList, ProductColor
from rest_framework.reverse import reverse
from . import validators
from api.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True,

    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user",read_only=True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello,
                                              validators.unique_product_title])
    
    body = serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            'owner',                         
            'pk',
            'title',
            'body',
            'price',
            'sale_price',
            'public',
            'path',
            'endpoint',
        ]
   
    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }

    
    def get_edit_url(self, obj):
        request = self.context.get('request')  #self.request
        if request is None: 
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)



class ProductWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductWeight
        fields = "__all__"




class ProductListDetailSerializer(serializers.ModelSerializer):
    weight = ProductWeightSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = "__all__"

# TODO: FAQ product ni ichida

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"



class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = "__all__"


class ProductWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductWeight
        fields = "__all__"



class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
        


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ['name', 'color']