from django.urls import path

from core.views import category_list,products_details,products_lists,category_details,products_of_category

urlpatterns = [
    path('products/', products_lists),
    path('products/<int:product_id>', products_details),
    path('categories/', category_list),
    path('categories/<int:category_id>', category_details),
    path('categories/<int:category_id>/products', products_of_category)
]
