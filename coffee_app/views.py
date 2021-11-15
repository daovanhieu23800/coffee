from django.shortcuts import render
from .models import Item
from django.core import serializers
from django.http import HttpResponse
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


