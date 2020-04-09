from django.shortcuts import render
from .models import Product,Category

def index(recuest):
    name="Edige"
    street=("Ualichanova",19,1)
    data={"name":name,"street":street}
    return render(recuest,'api.html',context=data)

def products(recuest):
    products=Product.objects.all()
    data={"products":products}
    return render(recuest,'api_products.html',context=data)

def product(recuest,product_id):
    product=Product.objects.get(id=product_id)
    data={"product":product}
    return render(recuest,'api_product.html',context=data)

def categories(recuest):
    categories=Category.objects.all()
    data={"categories":categories}
    return render(recuest,'categories.html',context=data)

def category(recuest,category_id):
    category=Category.objects.get(id=category_id)
    data={"category":category}
    return render(recuest,'category.html',context=data)

def pruductsByCategory(request,category_id):
    products=Product.objects.all()
    products1=[]
    for i in products:
        if (i.category==Category.objects.get(id=category_id).name):
            products1.append(i)
    data={"products":products1}
    return render(request,'productsByCategory.html',context=data)
    

