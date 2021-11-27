from django.shortcuts import render
from .models import Item
from django.core import serializers
from django.http import HttpResponse
from .serializer import ItemSerializers
from django.http.response import JsonResponse

import json
# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'coffee_app/index.html')


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

