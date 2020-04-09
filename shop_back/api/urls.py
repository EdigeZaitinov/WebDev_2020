from django.urls import path
from api import views
urlpatterns = [
    path('', views.index,name='index'),
    path('products/', views.products,name='products'),
    path('products/<int:product_id>/', views.product,name='product'),
    path('categories/', views.categories,name='categories'),
    path('categories/<int:category_id>/', views.category,name='category'),
    path('categories/<int:category_id>/products/',views.pruductsByCategory,name='pruductsByCategory')
]