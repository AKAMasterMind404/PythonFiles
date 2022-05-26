from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'home.html')


def page1(request):
    return render(request, 'page1.html', context={"numbers": [1, 2, 3, 4]})


def page2(request):
    return render(request, 'page2.html')


def page3(request):
    return render(request, 'page3.html')


def page4(request):
    return render(request, 'page4.html')

