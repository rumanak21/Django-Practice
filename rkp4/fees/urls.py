from django.urls import path
from . import views


urlpatterns = [
    path('feesdj/', views.learn_djfees),
    path('feespy/', views.learn_pyfees),
]