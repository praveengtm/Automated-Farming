from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensordata

def index(request):
	# data = Sensordata.objects.all()
	data = Sensordata.objects.order_by('-sampleindex')[:5]

	dl = len(data)
	print(dl)
	return render(request, "Sensor/show.html",{"objects":data,"length":dl})

def more(request,sampleindex):
	obj = Sensordata.objects.filter(pk = sampleindex).first()
	print(obj.humidity)
	return render(request, "Sensor/more.html",{"object":obj})

