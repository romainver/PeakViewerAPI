from rest_framework import viewsets
from django.template import loader
from .serializers import PeakSerializer, RecordSerializer
from .models import Peak, Record
from django.http import HttpResponse, JsonResponse
from django.contrib.gis.geos import Polygon

class PeakViewSet(viewsets.ModelViewSet):
    queryset = Peak.objects.all().order_by('peak_name')
    serializer_class = PeakSerializer

def getpeakswithinBB(request, top_lat,top_long, bot_lat, bot_long ):
	bbox = (top_lat,top_long, bot_lat, bot_long)
	geom = Polygon.from_bbox(bbox)
	peaks = Peak.objects.filter(coordinates__within=geom)
	return HttpResponse(peaks)

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('forecasted_at')
    serializer_class = RecordSerializer
    
def docs(request):
	template = loader.get_template('doc/index.html')
	return HttpResponse(template.render())

def map(request):
	template = loader.get_template('map/index.html')
	peaks = Peak.objects.all()
	context = {'peaks':peaks}
	return HttpResponse(template.render(context, request))

def getrecords(request, pk):
	peak = Peak.objects.get(id=pk)
	records = Record.objects.filter(peak = peak)
	formatted_records = []
	for record in records :
		print(record.forecasted_at.timestamp())
		formatted_records.append([record.forecasted_at.timestamp() *1000, record.temperature])
	formatted_records.sort()
	json = {'peak':peak.peak_name,
			'records':formatted_records[0:3]}
	return JsonResponse(json)