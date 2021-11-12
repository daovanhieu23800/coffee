from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse, JsonResponse
from users.models import account
from users.serializers import accountSerializers
from django.core.files.storage import default_storage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('coffee_app:index'))

def register(request):
    return

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


class accountDetail(APIView):
    def get_object(self,id):
        try:
            accounts = account.objects.get(id=id)
        except account.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        accounts = self.get_object(id)
        accounts_serializers = accountSerializers(accounts)
        return Response(accounts_serializers.data)
    
    def put(self, request,id):
        accounts = self.get_object(id)
        accounts_serializers = accountSerializers(accounts,data=request.data)
        if accounts_serializers.is_valid():
            accounts_serializers.save()
            return Response(accounts_serializers.data,)
        return Response(accounts_serializers.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        accounts = self.get_object(id)
        accounts.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

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

@api_view(['GET','PUT','DELETE'])
def account_detail(request,pk):
    try:
        accounts = account.objects.get(pk=pk)
    except account.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        accounts_serializers = accountSerializers(accounts)
        return Response(accounts_serializers.data)
    elif request.method == 'PUT':
        accounts_serializers = accountSerializers(accounts,data=request.data)
        if accounts_serializers.is_valid():
            accounts_serializers.save()
            return Response(accounts_serializers.data,)
        return Response(accounts_serializers.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        accounts.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)