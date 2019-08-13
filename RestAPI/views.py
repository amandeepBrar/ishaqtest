# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Weather,Location
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from django.http import Http404
from datetime import date, timedelta, datetime
from dateutil.parser import parse
import json

class WeatherView(APIView):
    def post(self, request, format=None):
    	data = request.data
    	objs = Weather.objects.filter(id=data['id'])
    	if len(objs)!=0:
    		return Response([], status=status.HTTP_400_BAD_REQUEST)
    	location = Location(lat=data['location']['lat'],lon=data['location']['lon'],city=data['location']['city'],state=data['location']['state'])
    	location.save()
    	weather = Weather(id=data['id'],date=data['date'],location=location,temperature=json.dumps(data['temperature']))
    	weather.save()
        return Response([], status=status.HTTP_200_OK)
    def get(self,request,format=None):
    	return Response([], status=status.HTTP_200_OK)


class EraseView(APIView):

	def delete(self, request, format=None):
		Weather.objects.all().delete()
		return Response([], status=status.HTTP_200_CREATED)

