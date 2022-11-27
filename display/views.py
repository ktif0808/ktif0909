from django.shortcuts import render
from display import models
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'display/index.html')

def getIP(request):
    context = {}
    ip = ""
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse(ip)

def getUsers(request):
    queryset = models.User.objects.all()[:20]
    return JsonResponse({"users" : list(queryset.values())})
