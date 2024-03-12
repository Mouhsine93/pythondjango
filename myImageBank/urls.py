from django.urls import path
from myImageBank import views

urlpatterns = [
    path('myImage/random/', views.RandomImage.as_view()),
    path('myImage/<int:image_id>/', views.Image.as_view()),
]
