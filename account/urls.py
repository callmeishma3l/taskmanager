from django.conf.urls import url

from django.contrib.auth import views as builtin_views
from django.contrib.auth import forms as builtin_forms

from . import views,forms

urlpatterns = (
    url(r'^$', views.usercp, name='usercp'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^password-change/done/$', builtin_views.password_change_done,
        {'template_name': 'account/password-change-done.html'}, name='password-change-done'),
    url(r'password-change/$', builtin_views.password_change,
        {'template_name': 'account/password-change.html',
         'post_change_redirect': 'account:password-change-done',
         'password_change_form': builtin_forms.PasswordChangeForm}, name='password-change'),
)