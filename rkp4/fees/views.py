from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_djfees(request):
    return HttpResponse("Django Fees 300tk")

def learn_pyfees(request):
    return HttpResponse("Python Fees 200tk")