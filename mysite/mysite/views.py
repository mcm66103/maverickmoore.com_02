from django.shortcuts import render

def index(request):
    return render(request, 'mysite/index.html')

def demo(request):
    return render(request, 'mysite/demo.html')
