import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl

# Create your views here.
class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class RedirectionDetailProduit(APIView):
    def get_object(self, pk):
        try:
            response = requests.get(baseUrl+'product/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
    def get(self, request, pk, format=None):
        response = requests.get(baseUrl+'product/'+str(pk)+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"

###################
#...TME2 starts...#
from django.http import Http404
from rest_framework import renderers

class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpg'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data

#Uncomment if images may iclude PNG
#class PNGRenderer(renderers.BaseRenderer):
#    media_type = 'image/png'
#    format = 'png'
#    charset = None
#    render_style = 'binary'
#
#    def render(self, data, media_type=None, renderer_context=None):
#        return data

import json
from rest_framework.reverse import reverse

class ProduitImageRandom(APIView):
    renderer_classes = [JPEGRenderer]
#Uncomment if images may iclude PNG
#    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self, request, pk, format=None):
        try:
            projectUrl = reverse('projectRoot',request=request, format=format)
#Below three (human friendly) lines...
#            responseFromMyImageBank = requests.get(projectUrl+'myImage/random/')
#            extractedUrl = json.loads(responseFromMyImageBank.text)['url']
#            response = requests.get(extractedUrl)
#... are equivalent to the (AST friendly) line below:
            response = requests.get(json.loads(requests.get(projectUrl+'myImage/random/').text)['url'])
            return Response(response)
        except:
            raise Http404

class ProduitImage(APIView):
    renderer_classes = [JPEGRenderer]
#Uncomment if images may iclude PNG
#    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self, request, pk, image_id, format=None):
        try:
            projectUrl = reverse('projectRoot',request=request, format=format)
#Below three (human friendly) lines...
#            responseFromMyImageBank = requests.get(projectUrl+'myImage/'+str(image_id)+'/')
#            extractedUrl = json.loads(responseFromMyImageBank.text)['url']
#            response = requests.get(extractedUrl)
#... are equivalent to the (AST friendly) line below:
            response = requests.get(json.loads(requests.get(projectUrl+'myImage/'+str(image_id)+'/').text)['url'])
            return Response(response)
        except:
            raise Http404

#...end of TME2...#
###################

from mytig.models import ProduitEnPromotion
from mytig.serializers import ProduitEnPromotionSerializer

class PromoList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return Response(res)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class PromoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitEnPromotion.objects.get(pk=pk)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitEnPromotionSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"
