from django.shortcuts import render
from datetime import datetime
# Create your views here.
def learn_django(request):
    return render(request, 'course/course1.html',
    {'nm':'Django is Awesome.'}) 

def learn_django2(request):
    d = datetime.now()
    return render(request, 'course/course2.html', {'dt':d}) 

def learn_django3(request):
    
    return render(request, 'course/course3.html',
    {'p1':19.56634, 'p2': 19.00000, 'p3': 19.15500})

def learn_django4(request):
    return render(request, 'course/course4.html',
    {'nm':'Django', 'st':5}) 

def learn_django5(request):
    student = {'names' :['Rumana', 'Sanzida', 'Faisal', 'Tushar']}
    return render(request, 'course/course5.html', student) 

def learn_django6(request):
    stu = {'stu1': {'name' : 'Rumana', 'roll': '101'},
            'stu2':{'name' : 'Sanzida', 'roll': '102'},
            'stu3':{'name' : 'Faisal', 'roll': '103'},
            'stu4':{'name' : 'Tushar', 'roll': '104'}
          }
    students = {'student' : stu}
    return render(request, 'course/course6.html', students) 

def learn_django7(request):
    data = {'stu1': {'name' : 'Rumana', 'roll': '101'},
              'stu2':{'name' : 'Sanzida', 'roll': '102'},
              'stu3':{'name' : 'Faisal', 'roll': '103'},
              'stu4':{'name' : 'Tushar', 'roll': '104'}
            }
    return render(request, 'course/course7.html',
    {'data':data}) 