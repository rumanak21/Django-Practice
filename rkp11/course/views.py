from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return render(request, 'course/course1.html', {'tittle':'Django Course', 'cname':'Django'})