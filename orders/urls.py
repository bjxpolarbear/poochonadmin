from . import views
from django.conf.urls import url


app_name = 'orders'

urlpatterns = [
    # /orders
    url(r'^$', views.OrderIndexView.as_view(), name='index'),

    # /orders/<quote_id>
    url(r'^(?P<pk>[0-9]+)$', views.OrderDetailView.as_view(), name='detail'),

    # /orders/create
    url(r'^create/$', views.OrderCreateView.as_view(), name='order-create'),

    # /orders/<order_id>/update
    url(r'^(?P<pk>[0-9]+)/update/$', views.OrderUpdateView.as_view(), name='order-update'),

    # /orders/<order_id>/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.OrderDeleteView.as_view(), name='order-delete'),

    # /quotes/<order_id>/convert/
    url(r'^(?P<pk>[0-9]+)/convert/$', views.ConvertToJobView.as_view(), name='order-convert')
]