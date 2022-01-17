from django.urls import path
from . import views

urlpatterns = [
    path('', views.didi, name='n1'),
    path('services', views.services, name='servin'),
    path('delete/<taskid>', views.deletetask, name='deletetask'),
    path('edit/<taskid>', views.edittask, name='edittask'),
    path('complete/<taskid>', views.completetask, name='completetask'),
    path('pending/<taskid>', views.pendingtask, name='pendingtask'),
]
