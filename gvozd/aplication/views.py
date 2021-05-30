from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from .models import Favour, Aplications


def makeorder(request):
    favour = Favour.objects.all()
    return render(request, 'gvozd/signin.html',{'favour':favour})


@csrf_exempt
def getform(request):
    if request.method == 'GET':
        return render(request, 'gvozd/signin.html')
    if request.method == 'POST':
        fid = request.POST["favour_id"]
        favour = Favour.objects.filter(pk=fid)
        ffirst_name = request.POST["first_name"]
        fdate = request.POST["date"]
        femail = request.POST["email"]
        new_application = Aplications(favour=favour[0],first_name = ffirst_name, email =femail, date = fdate)
        new_application.save()
        return render(request, 'gvozd/signin.html')


@csrf_exempt
def apps_info(request):
    applications = Aplications.objects.all()
    return render(request, 'gvozd/table.html', {'applications': applications})
