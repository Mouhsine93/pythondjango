from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from monTiGMagasin.config import baseUrl
from monTiGMagasin.models import InfoProduct
from monTiGMagasin.serializers import InfoProductSerializer

#######################
#...TME3 JWT starts...#
from rest_framework.permissions import IsAuthenticated
#...end of TME3 JWT...#
#######################

# Create your views here.
class InfoProductList(APIView):
#######################
#...TME3 JWT starts...#
    permission_classes = (IsAuthenticated,)
#...end of TME3 JWT...#
#######################
    def get(self, request, format=None):
        products = InfoProduct.objects.all()
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)
class InfoProductDetail(APIView):
#######################
#...TME3 JWT starts...#
    permission_classes = (IsAuthenticated,)
#...end of TME3 JWT...#
#######################
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)

class removeSaleProduct(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        product.sale = False
        product.save()
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)

class putOnSaleProduct(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, price, format=None):
        product = self.get_object(tig_id=tig_id)
        product.sale = True
        product.discount = price
        product.save()
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
class deleteProduct(APIView):
    def get_object(self, id):
        try:
            return InfoProduct.objects.get(id=id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def delete(self, request, id, format=None):
        product = self.get_object(id=id)
        print(product)
        product.delete()
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)
    
class editProduct(APIView):
    def get_object(self, id):
        try:
            return InfoProduct.objects.get(id=id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def put(self, request, id, format=None):
        product = self.get_object(id=id)
        serializer = InfoProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class createProduct(APIView):
    def post(self, request, format=None):
        serializer = InfoProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

