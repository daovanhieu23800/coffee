from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
#from django.views.decorators.csrf import csrf_exempt
#from users import serializers
#from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse, JsonResponse
from users.models import account, customer
from users.serializers import accountSerializers, customerSerializers
from django.core.files.storage import default_storage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('coffee_app:index'))

def register(request):
    return
### test API
###error
###account
class account_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = account.objects.all()         
    serializer_class = accountSerializers
    lookup_field = 'id'
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request,  *args, **kwargs):
        return self.destroy(request,*args,**kwargs)


class accountAPIview(APIView):
    def get(self,request):
        accounts = account.objects.all()
        accounts_serializers = accountSerializers(accounts,many = True)
        return Response(accounts_serializers.data)
    
    def post(self, request):
        accounts_serializers = accountSerializers(data = request.data)
        if accounts_serializers.is_valid():
            accounts_serializers.save()
            return Response(accounts_serializers.data,status = status.HTTP_201_CREATED)
        return Response(accounts_serializers.errors, status = status.HTTP_400_BAD_REQUEST)
#customer

class customer_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = customer.objects.all()         
    serializer_class = customerSerializers
    lookup_field = 'id_account'
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request,  *args, **kwargs):
        return self.destroy(request,*args,**kwargs)


class customerAPIview(APIView):
    def get(self,request):
        customers = customer.objects.all()
        customers_serializers = customerSerializers(customers,many = True)
        return Response(customers_serializers.data)
    
    def post(self, request):
        customers_serializers = customerSerializers(data = request.data)
        if customers_serializers.is_valid():
            customers_serializers.save()
            return Response(customers_serializers.data,status = status.HTTP_201_CREATED)
        return Response(customers_serializers.errors, status = status.HTTP_400_BAD_REQUEST)



####test API
#@api_view(['GET','POST'])
#def accountApi(request):
#    if request.method == 'GET':
##        accounts = account.objects.all()
#        accounts_serializers = accountSerializers(accounts,many = True)
#        return Response(accounts_serializers.data)
#
#    elif request.method == 'POST':
#        accounts_serializers = accountSerializers(data = request.data)
#        if accounts_serializers.is_valid():
#            accounts_serializers.save()
#            return Response(accounts_serializers.data,status = status.HTTP_201_CREATED)
#        return Response(accounts_serializers.errors, status = status.HTTP_400_BAD_REQUEST)

#    elif request.method == 'PUT':
#      accounts_serializers = accountSerializers(Account,data=request.data)
#        if accounts_serializers.is_valid():
#            accounts_serializers.save()
#            return JsonResponse("Update successfully", safe = False)
#        return JsonResponse("Failed to Update")
#    elif request.method == 'DELETE':
#        accounts = account.objects.get(id=id)
#        accounts.delete()
#        return JsonResponse("Delete SuccessFUlly", safe = False)

#@api_view(['GET','PUT','DELETE'])
#def account_detail(request,pk):
#    try:
#        accounts = account.objects.get(pk=pk)
#    except account.DoesNotExist:
#        return Response(status = status.HTTP_404_NOT_FOUND)
#    
#    if request.method == 'GET':
#        accounts_serializers = accountSerializers(accounts)
#        return Response(accounts_serializers.data)

#    elif request.method == 'PUT':
#        accounts_serializers = accountSerializers(accounts,data=request.data)
#        if accounts_serializers.is_valid():
#            accounts_serializers.save()
#            return Response(accounts_serializers.data)
#        return Response(accounts_serializers.errors, status = status.HTTP_400_BAD_REQUEST)
    
#    elif request.method == 'DELETE':
#        accounts.delete()
 #       return Response(status = status.HTTP_204_NO_CONTENT)
#
def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)