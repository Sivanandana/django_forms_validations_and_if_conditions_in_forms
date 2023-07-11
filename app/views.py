from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def studentform(request):
    SO=Studentform()
    d={'SO':SO}
    if request.method=='POST':
        SOD=Studentform(request.POST)
        if SOD.is_valid():
            return HttpResponse('valid data')
        else:
            return HttpResponse('invalid data')
    return render(request,'studentform.html',context=d)