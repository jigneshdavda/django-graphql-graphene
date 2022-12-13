from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Shop, Products
from .serializers import ShopSerializer, ProductsSerializer

class ShopListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the shop items for given requested user
        '''
        shop = Shop.objects.get(user = request.user.id, is_active = 1)
        serializer = ShopSerializer(shop)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the shop with given shop data
        '''
        data = {
            'user' : request.user.id,
            'name' : request.data.get('shop_name'),
            'address' : request.data.get('shop_address'),
            'email_id' : request.data.get('shop_email_id'),
            'contact_number' : request.data.get('shop_contact_number'),
            'location' : request.data.get('shop_location'),
            'is_active' : '1'
        }
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the product items for given requested user
        '''
        products = Products.objects.filter(is_active = 1)
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the product with given product data
        '''
        # fetch logged in user shop id
        shop = Shop.objects.get(user = request.user.id, is_active = 1)
        
        data = {
            'shop' : str(shop.id),
            'name' : request.data.get('product_name'),
            'description' : request.data.get('product_description'),
            'price' : request.data.get('product_price'),
            'is_active' : '1',
        }
        serializer = ProductsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)