from django.shortcuts import render, redirect

from .form import MakeMassage
from .models import Message
from django.views.decorators.csrf import csrf_exempt


def show(request):
    messages = Message.objects.all()
    return render(request, 'gvozd/feedback_list.html', {'messages': messages})


def forum(request):
    if request.method == 'POST':
        form = MakeMassage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/feedback/show')
    form = MakeMassage()
    context = {
        'form': form,
    }
    return render(request, 'gvozd/feedback.html', context)

