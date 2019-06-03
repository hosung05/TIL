from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')


def hello(request, name):
    greeting = f'Hello,{name}'
    return render(request, 'hello.html', {'greeting': greeting})