from django.shortcuts import render


def main(request):
    hello = 'Hello'
    return render(request, 'gvozd/index.html', {'hello': hello})

def user_check(request, name):
    hello = 'Hello ' + name
    return render(request, 'gvozd/index.html', {'hello': hello})
# Create your views here.
