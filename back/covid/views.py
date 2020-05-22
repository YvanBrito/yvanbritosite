from django.http import JsonResponse
import json, time, urllib.request, os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dataPath = '../data.json'

# https://github.com/CSSEGISandData/COVID-19
# https://github.com/turicas/covid19-br
# https://brasil.io/api/dataset/covid19/
def globalCases(request):
    with open(os.path.join(BASE_DIR, dataPath), 'r') as myfile:
        data=myfile.read()

    resp = json.loads(data)
    return JsonResponse(resp['globalCases'], safe=False)

def brasilCases(request):
    with open(os.path.join(BASE_DIR, dataPath), 'r') as myfile:
        data=myfile.read()

    resp = json.loads(data)
    return JsonResponse(resp['brasilCases'], safe=False)

def toptenconfirmed(request):
    with open(os.path.join(BASE_DIR, dataPath), 'r') as myfile:
        data=myfile.read()

    resp = json.loads(data)
    return JsonResponse(resp['topTenConfirmed'], safe=False)

def worldregions(request):
    with open(os.path.join(BASE_DIR, dataPath), 'r') as myfile:
        data=myfile.read()

    resp = json.loads(data)
    return JsonResponse(resp['worldregions'], safe=False)

def updateDate(request):
    with open(os.path.join(BASE_DIR, dataPath), 'r') as myfile:
        data=myfile.read()

    resp = json.loads(data)
    return JsonResponse(resp['updateTime'], safe=False)
