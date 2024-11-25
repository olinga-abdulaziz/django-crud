from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def drinks_list(request):
    if request.method=='GET':
        #Get all drinks
        drinks=Drink.objects.all()
        #Serialize drinks
        serializer=DrinkSerializer(drinks,many=True)
        #Return json data
        return Response(serializer.data)

@api_view(['GET','POST'])  
def add_Drink(request):
    if request.method=='POST':
        #get request data and desriliaze them
        serializer=DrinkSerializer(data=request.data)
        #check if request is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def drink_Detail(request,id):
    try:
        drink=Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method=='GET':
        serializer=DrinkSerializer(drink)
        return Response(serializer.data)
    
    
    
@api_view(['PUT'])
def drink_Update(request,id):
    try:
        drink=Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method=='PUT':
        serializer=DrinkSerializer(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['DELETE'])
def drink_Delete(request,id):
    try:
        drink=Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)