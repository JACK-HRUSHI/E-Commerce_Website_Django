from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders

def index(request):

# START OF FINAL

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = { item['category'] for item in catprods }
    for cat in cats:
        prod = Product.objects.filter( category = cat )
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

# END OF FINAL

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def prodView(request, myid):
    # Fetch the product using Id
    product = Product.objects.filter(id=myid)
    print(product)

    return render(request, 'shop/prodview.html', {'product' : product[0]})

def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        add = request.POST.get('add1', '') + " " + request.POST.get('add2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(name=name, email=email, add=add, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
    return render(request, 'shop/checkout.html')
