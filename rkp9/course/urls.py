from django.urls import path
from . import views
urlpatterns = [
    path('learndj/', views.learn_django),
    path('learndj2/', views.learn_django2),
    path('learndj3/', views.learn_django3),
    path('learndj4/', views.learn_django4),
    path('learndj5/', views.learn_django5),
    path('learndj6/', views.learn_django6),
    path('learndj7/', views.learn_django7),
]