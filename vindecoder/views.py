# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from vindecoder.models import Car
from vindecoder.serializers import CarSerializer
from pymongo import MongoClient


def car_list(request):
    if request.method == 'GET':
        # cars = Car.objects.all()
        # serializer = CarSerializer(cars, many=True)
        # return JsonResponse(serializer.data, safe=False)

        # cars = Car.objects()

        # return JsonResponse(serializer.data, safe=False)
        cars = Car.objects.all()

        serializer = CarSerializer(cars, many=True)
        json = JsonResponse(serializer.data, safe=False)
        return json


def car_certain(request, key):
    try:
        car = Car.objects(wmi=key.upper())
    except Car.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarSerializer(car, many=True)
        return JsonResponse(serializer.data, safe=False)