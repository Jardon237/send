from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def sent(request):
    return render(request, 'sent.html', {})

def recieved(request):
    return render(request, 'recieved.html', {})

def branches(request):
    return render(request, 'branches.html', {})