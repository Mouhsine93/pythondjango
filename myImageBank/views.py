from rest_framework.views import APIView
from rest_framework.response import Response
from myImageBank.config import randomImageUrl
from django.http import Http404
import secrets

# Create your views here.

class RandomImage(APIView):
    def get(self, request, format=None):
        try:
            return Response({'url': secrets.choice(randomImageUrl)})
        except:
            raise Http404

class Image(APIView):
    def get(self, request, image_id, format=None):
        try:
            return Response({'url': randomImageUrl[image_id]})
        except:
            raise Http404
