from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

from core.models import Category,Product



def category_list(request):
    categories=Category.objects.all()
    categories_json=[category.take_category_json() for category in categories]
    return JsonResponse(categories_json,safe=False)



def category_details(request,category_id):
    try:
        category=Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error':'No category'})
    return JsonResponse(category.take_category_json())



def products_of_category(request,category_id):
    products=Product.objects.all()
    product_is_category=[]
    for i in range(len(products)):
        if products[i].category_id.id==category_id:
            product_is_category.append(products[i])
        else:
            continue
    if(len(product_is_category)!=0):
        products_is_category_json=[product.take_product_json()
                                   for product in product_is_category]
        return JsonResponse(products_is_category_json,safe=False)
    else:
        return JsonResponse("error: No category products")


def products_lists(request):
    products=Product.objects.all()
    products_json=[product.take_product_json() for product in products]
    return JsonResponse(products_json,safe=False)


def products_details(request,product_id):
    try:
        product=Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse("error: Product does't exist")

    return JsonResponse(product.take_product_json())