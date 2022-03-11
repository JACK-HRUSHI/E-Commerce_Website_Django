from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
import json

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

def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = { item['category'] for item in catprods }
    for cat in cats:
        prodtemp = Product.objects.filter( category = cat )
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, 'msg': ''}
    if len(allProds) == 0 or len(query)<3 :
        params = {'msg': 'Please make sure to enter relevant search query'}
    return render(request, 'shop/search.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc) # Contact() is a constructor of Contact Class
        contact.save()
        thank = True

        return render(request, 'shop/contact.html', {'thank': thank})

    return render(request, 'shop/contact.html')



def tracker(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        orderId = request.POST.get('orderId', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str) # (default=str) is used to handle exception related to time key
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def prodView(request, myid):
    # Fetch the product using Id
    product = Product.objects.filter(id=myid)
    print(product)

    return render(request, 'shop/prodview.html', {'product' : product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        add = request.POST.get('add1', '') + " " + request.POST.get('add2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, add=add, city=city, state=state, zip_code=zip_code, phone=phone) # Order() is a constructor of Order Class
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed.") # OrderUpdate() is a constructor of OrderUpdate Class
        update.save()
        thank = True
        id = order.order_id

        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'shop/checkout.html')
