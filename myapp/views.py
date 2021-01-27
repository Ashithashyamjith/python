from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testfn(request):
    return HttpResponse("hello")
def testfn2(request):
    return HttpResponse("welcome")
def testfn3(request):
    return render(request,'test.html')
