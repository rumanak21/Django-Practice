from django.shortcuts import render

# Create your views here.

def learn_django(request):
    Course_name = 'Django'
    Duration = '2 Months'
    Seats = 20
    course_details= {'cname': Course_name, 'du': Duration, 'st': Seats}
    return render(request, 'course/course1.html', context=course_details)