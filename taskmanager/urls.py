from django.conf.urls import url

from . import views

urlpatterns = (
    #/taskmanager/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/taskmanager/new/
    url(r'^new/$', views.CreateView.as_view(), name='new'),
    #/taskmanager/1/
    url(r'^(?P<pk>[0-9]+)/$', views.edit_task, name='edit'),
    #/taskmanager/1/delete/
    url(r'^(?P<task_id>[0-9]+)/delete/$', views.delete, name='delete'),
    #/taskmanager/1/editinplace/
    url(r'^(?P<pk>[0-9]+)/editinplace/$', views.editinplace, name='editinplace'),
)