from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .form import MakeMassage
from .models import Message
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.urls import path



def show(request):
    messages = Message.objects.all()
    return render(request, 'gvozd/feedback_list.html', {'messages': messages})


def forum(request):
    if request.method == 'POST':
        form = MakeMassage(request.POST)
        favour_id = form.data['favour']
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('show/' + favour_id)
    form = MakeMassage()
    context = {
        'form': form,
    }
    return render(request, 'gvozd/feedback.html', context)


def favour_id(request, favour_id = 0):
    messages = Message.objects.filter(favour_id=favour_id).order_by('id')
    return render(request, 'gvozd/feedback_list.html', {'messages': messages})
