from django.shortcuts import render,HttpResponse
def login(request):
    return HttpResponse("hello there")

# def dash(request):
#     return HttpResponse("hello there")

def dash(request):
    return render(request,"dashboard.html")

# Create your views here.
