import graphene

from graphene_django import DjangoObjectType 
from .models import Shop, Products
from rx import Observable

class ProductType(DjangoObjectType): 
    class Meta:
        model = Products
        fields = "__all__"
        
class ShopType(DjangoObjectType): 
    class Meta:
        model = Shop
        fields = "__all__"

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product = graphene.Field(ProductType, product_id=graphene.Int())
    shop = graphene.List(ShopType)

    def resolve_all_products(self, info, **kwargs):
        return Products.objects.all()

    def resolve_product(self, info, product_id):
        return Products.objects.get(pk=product_id)

    def resolve_shop(self, info, **kwargs):
        return Shop.objects.all()
    
class Subscription(graphene.ObjectType):
    products = graphene.String()

    def resolve_products(root, info):
        return Observable.interval(3000) \
                         .map(lambda i: Products.objects.count())

schema = graphene.Schema(query=Query, subscription=Subscription)