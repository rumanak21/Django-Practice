from django.urls import path
from . import views
urlpatterns = [
    path('getfees/', views.dejango_fees),
]