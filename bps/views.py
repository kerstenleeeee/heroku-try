# License
# Author: Kristine-Clair Lee
# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo 
# of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019 

# Code History
# Lee - 01/30/19 - Initial Commit
# Lee - 01/30/19 - Added views

# File creation date: 01/30/19
# Development Group: 3
# Client Group: 3
# Description: Django database views

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bps.models import Building, Floor, Routes
from bps.serializers import BuildingSerializer, FloorSerializer, RouteSerializer
from rest_framework import status

# variables
# blue_print --- object
# serializer --- object/model serializer

# Get the list of the buildings
@api_view(['GET', 'POST'])
def BuildingList(request):
    if request.method == 'GET':
        blue_print = Building.objects.all()
        serializer = BuildingSerializer(blue_print, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BuildingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# get the list of the floors
@api_view(['GET', 'POST'])
def FloorList(request):
    if request.method == 'GET':
        blue_print = Floor.objects.all()
        serializer = FloorSerializer(blue_print, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FloorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# get a building object
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def BuildingViews(request, pk):
    try:
        blue_print = Building.objects.get(buildID = pk)
    except Building.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BuildingSerializer(blue_print)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BuildingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = BuildingSerializer(blue_print, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blue_print.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# get a floor object
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def FloorViews(request, pk):
    try:
        blue_print = Floor.objects.get(floorID = pk)
    except Floor.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FloorSerializer(blue_print)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FloorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = FloorSerializer(blue_print, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blue_print.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# get the list of the floors
@api_view(['GET', 'POST'])
def routeList(request):
    if request.method == 'GET':
        blue_print = Route.objects.all()
        serializer = RouteSerializer(blue_print, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RouteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# get a building object
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def routeViews(request, pk):
    try:
        blue_print = Route.objects.get(roomNo = pk)
    except Route.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RouteSerializer(blue_print)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RouteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = RouteSerializer(blue_print, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blue_print.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)