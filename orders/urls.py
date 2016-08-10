from . import views
from django.conf.urls import url


app_name = 'orders'

urlpatterns = [
    # /orders
    url(r'^$', views.OrderIndexView.as_view(), name='index'),
]