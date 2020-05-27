from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from devradar.models import Dev
from devradar.serializers import DevSerializer
import json
import urllib.request


@csrf_exempt
def dev_list(request):
    """
    List all code devs, or create a new dev.
    """
    if request.method == 'GET':
        devs = Dev.objects.all()
        serializer = DevSerializer(devs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        data["location"] = str(data["latitude"]) + ";" + str(data["longitude"])
        resp = urllib.request.urlopen("https://api.github.com/users/" + data["github_username"])
        github_data = json.loads(resp.read())
        data["name"] = github_data["name"]
        data["avatar_url"] = github_data["avatar_url"]
        if github_data["bio"] is None:
            data["bio"] = ""
        else:
            data["bio"] = github_data["bio"]

        serializer = DevSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def dev_detail(request, pk):
    """
    Retrieve, update or delete a dev.
    """
    try:
        dev = Dev.objects.get(pk=pk)
    except Dev.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DevSerializer(dev)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DevSerializer(dev, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dev.delete()
        return HttpResponse(status=204)
