from django.urls import path, re_path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
    re_path('list/', views.list, name='list'),
    re_path(r'^view/(?P<num>[0-9]+)/$', views.view, name='view'),
    re_path(r'^delete/(?P<num>[0-9]+)/$', views.delete, name='delete'),
    re_path(r'^updateform/(?P<num>[0-9]+)/$', views.updateform, name='updateform'),
]

