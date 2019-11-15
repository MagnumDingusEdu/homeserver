from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def landing_page_view(request, *args, **kwargs):
    print(request.user)
    print("lalalalal")
    print(request.POST)
    print(request.GET)
    return render(request, 'landing/index.html', {'user': request.user})

def rickroll_view(*args, **kwargs):
    return redirect("http://bitly.com/98K8eH")




    