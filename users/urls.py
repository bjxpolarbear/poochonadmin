from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'users'

urlpatterns = [
    # url('^', include('django.contrib.auth.urls')),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^login/$', auth_views.login,{
        'redirect_field_name': 'home:index',
        'template_name': 'users/login.html',
    }, name='login'),

    url(r'^logout/$', auth_views.logout,{
        'redirect_field_name': 'home:index',
        'template_name': 'users/logout.html',
    },  name='logout')
]