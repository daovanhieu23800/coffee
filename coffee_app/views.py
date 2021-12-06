from django.shortcuts import render
from .models import Item, Order, OrderItem, ShippingAddress
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
        order = {'get_cart_total':0, 'get_cart_quantity':0}
    context = {'items': items, 'order':order}
    return render(request, 'coffee_app/order.html', context)
def news(request):
    """The home page """
    return render(request, 'coffee_app/news.html')

    
def updateItem(request):
    data = json.loads(request.body)
    itemId = data['itemId']
    action = data['action']
    print(itemId)
    print(action)

    customer = request.user.customer
    item = Item.objects.get(id = itemId)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, item=item)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('item was added',safe=False)

def processOrder(request):
    print('Data: ',request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = int(data['form']['total'])
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
    )
    return JsonResponse('payment complete',safe=False)


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

