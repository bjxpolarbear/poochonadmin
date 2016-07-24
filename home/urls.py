from django.conf.urls import url

from . import views


app_name = 'home'

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
]