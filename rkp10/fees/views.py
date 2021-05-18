from django.shortcuts import render

# Create your views here.
def dejango_fees(request):
    return render(request, 'fees/info.html', {'fe':'Fees 200 tk'})