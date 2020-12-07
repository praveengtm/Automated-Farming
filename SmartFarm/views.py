from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensordata

def index(request):
	data = Sensordata.objects.all()
	dl = len(data)
	print(dl)
	return render(request, "SmartFarm/show.html",{"objects":data,"length":dl})

def more(request,sample_id):
	obj = Sensordata.objects.filter(pk = sample_id).first()
	print(obj.humidity)
	return render(request, "SmartFarm/more.html",{"object":obj})

