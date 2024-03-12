from django.urls import path, register_converter
from monTiGMagasin import views

class FloatConverter:
    regex = r'\d+(\.\d+)?'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)

register_converter(FloatConverter, 'float')

urlpatterns = [
    path('infoproducts/', views.InfoProductList.as_view()),
    path('infoproduct/<int:tig_id>/', views.InfoProductDetail.as_view()),
    path('removeSaleProduct/<int:tig_id>/', views.removeSaleProduct.as_view()),
    path('putOnSaleProduct/<int:tig_id>/<float:price>/', views.putOnSaleProduct.as_view()),
    path('deleteProduct/<int:id>/', views.deleteProduct.as_view()),
    path('createProduct/', views.createProduct.as_view()),
    path('editProduct/<int:id>/', views.editProduct.as_view()),
]
