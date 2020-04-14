import dicttoxml
import time
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .function.estimator import estimator
from  django.views.decorators.http import require_http_methods
from  django.views.decorators.csrf import  csrf_exempt
import json


# Create your views here.
FILENAME='log.txt'

@csrf_exempt
@require_http_methods(['POST'])
def estimatorJson(request):
    dic_data=json.loads(request.body)
    data=estimator(dic_data)
    #writeToLogFile(request)
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(['POST'])
def estimatorXml(request):
    dic_data=json.loads(request.body)
    data=estimator(dic_data)
    xml=dicttoxml.dicttoxml(data,custom_root ='estimator')
    #writeToLogFile(request)
    return HttpResponse(xml, content_type ='application/xml')


@require_http_methods(['GET'])
def log(request):
    #writeToLogFile(request)
    return HttpResponse(readFromLogFile())


def  readFromLogFile():
    file = open(FILENAME,'r')
    return file.readlines()


