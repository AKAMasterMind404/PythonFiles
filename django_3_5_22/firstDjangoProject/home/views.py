from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    context = {"var1":"AATTHHAARRVV"}
    return render(request, 'index.html', context)


def about(request):
    return HttpResponse("About page")


def profile(request):
    return HttpResponse("Profile page")
