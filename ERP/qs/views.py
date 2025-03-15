from django.shortcuts import render,HttpResponse

# Create your views here.

def vindex(request):
    return HttpResponse("Welcom to Index Page")