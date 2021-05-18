from django.shortcuts import render

# Create your views here.
def dejango_course(request):
    return render(request, 'course/info.html', {'nm': 'Django Course'})