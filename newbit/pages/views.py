from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {
    })


def result(request):
    test = request.GET.get('q')
    print(test)
    return render(request, 'pages/result.html', {
        'test': test
    })
