from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_link = serializers.HyperlinkedIdentityField(view_name='retrieve', lookup_field='pk')
    # title = serializers.CharField(validators=[validate_title])

    def get_my_discount(self, obj):
        return obj.get_discount()

    class Meta:
        model = Product
        fields = ['id', 'edit_link', 'user', 'title', 'content', 'price', 'sale_price', 'my_discount']

    def validate_title(self, value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('Already in use')
        return value
