from django.shortcuts import render
from .models import Customer, Item, News, Order, OrderItem, Promotions, ShippingAddress
from django.core import serializers
from django.http import HttpResponse
from .serializer import ItemSerializers
from django.http.response import JsonResponse
import json
import datetime

import json
# Create your views here.
def index(request):
    """The home page """
    return render(request, 'coffee_app/index.html')

def order(request):
    """The cart page"""
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_quantity':0,'get_cart_total_before_promotion':0}
    if order.promotion is None:
        context = {'items': items, 'order':order}
        #print("abc")
    else:
        context = {'items': items, 'order':order, 'promotion':order.promotion.content}
    return render(request, 'coffee_app/order.html', context)

def news(request):
    """The home page """
    return render(request, 'coffee_app/news.html')

def news_detail(request,id):
    """The home page """
    news = News.objects.get(id=id)
    context = {'news':news}
    return render(request, 'coffee_app/newsdetail.html',context)

def orderhistory(request):
    """The home page """
    orders = Order.objects.filter(customer=request.user.customer).order_by('date_ordered')
    context = {'orders':orders}
    return render(request, 'coffee_app/orderhistory.html',context)
    
def updateItem(request):
    data = json.loads(request.body)
    itemId = data['itemId']
    action = data['action']
    quantity = data['quantity']
    size = data['size']
    note = data['note']
    print(itemId)
    print(action)

    customer = request.user.customer
    item = Item.objects.get(id = itemId)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, item=item, quantity = quantity, size = size, note = note)

    #if action == 'add':
    #   orderItem.quantity += 1
    #elif action == 'remove':
    #    orderItem.quantity -= 1

    orderItem.save()

    #if orderItem.quantity <= 0:
    #    orderItem.delete()

    return JsonResponse('item was added',safe=False)

def processOrder(request):
    print('Data: ',request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_ID = transaction_id
    else:
        print("not logged in")
    print(total)
    if total == order.get_cart_total:
        order.complete = True
    order.save()
    ShippingAddress.objects.create(
    customer = customer,
    order = order,
    address = data['shipping']['address'],
    phone = data['shipping']['phone'],
    fname = data['shipping']['fname'],
    instructions = data['shipping']['instructions'],
    date_add = data['shipping']['bday']
    )
    return JsonResponse('payment complete',safe=False)
####remove item
def removeItem(request):
    data = json.loads(request.body)
    itemId = data['itemIdtoremove']
    orderItem, created = OrderItem.objects.get_or_create(id = itemId)
    orderItem.delete()
    return JsonResponse('remove successfully',safe=False)

###promotion
def update_promotion(request):
    data = json.loads(request.body)
    proId = data['promotionId']
    print(proId)
    if request.user.is_authenticated:
        promotion = Promotions.objects.get(id = proId)
        customer = request.user.customer
        thisorder, created = Order.objects.get_or_create(customer=customer, complete=False)
        thisorder.promotion = promotion
        
        thisorder.get_cart_total_before_promotion
        thisorder.get_cart_total
        thisorder.save()
    else:
        print("not logging")
    
    return JsonResponse('promotion was added',safe=False)

# def items(request):
#     items = Item.objects.order_by('price')
#     context = {'items': items}
#     return render(request, 'coffee_app/index.html', context)
def items(request):
    items = Item.objects.all().values()

    items_list = list(items)

    data = json.dumps(items_list)
    return HttpResponse(data, content_type="application/json")
####item detail
def items_detail_1(request):
    items = Item.objects.raw('SELECT * FROM coffee_app_Item WHERE type="favourite"')

    serializer = ItemSerializers(items, many = True)

    return JsonResponse(serializer.data, safe = False)

def items_detail_2(request):
    items = Item.objects.raw('SELECT * FROM coffee_app_Item WHERE type="coffee"')

    serializer = ItemSerializers(items, many = True)

    return JsonResponse(serializer.data, safe = False)

def items_detail_3(request):
    items = Item.objects.raw('SELECT * FROM coffee_app_Item WHERE type="fruit tea"')

    serializer = ItemSerializers(items, many = True)

    return JsonResponse(serializer.data, safe = False)

def items_detail_4(request):
    items = Item.objects.raw('SELECT * FROM coffee_app_Item WHERE type="ICE BLENDED"')

    serializer = ItemSerializers(items, many = True)

    return JsonResponse(serializer.data, safe = False)

def items_detail_5(request):
    items = Item.objects.raw('SELECT * FROM coffee_app_Item WHERE type="snack"')

    serializer = ItemSerializers(items, many = True)

    return JsonResponse(serializer.data, safe = False)


###news

def get_news(request):
    items = News.objects.all().values()

    items_list = list(items)

    data = json.dumps(items_list)
    return HttpResponse(data, content_type="application/json")

###Promotion

def get_promotion(request):
    items = Promotions.objects.all().values()

    items_list = list(items)

    data = json.dumps(items_list)
    return HttpResponse(data, content_type="application/json")

def store(request):
    """The home page """
    items = Item.objects.all()
    context = {'items':items}
    return render(request, 'coffee_app/store.html',context)