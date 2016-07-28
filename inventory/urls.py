
from . import views
from django.conf.urls import url


app_name = 'inventory'

urlpatterns = [
    # /inventory
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /inventory/<item_id>
    url(r'^(?P<pk>[0-9]+)$', views.ItemDetailView.as_view(), name='detail'),

    # /inventory/create
    url(r'^create/$', views.ItemCreateView.as_view(), name='item-create'),

    # /inventory/<id>/update/
    url(r'^(?P<pk>[0-9]+)/update/$', views.ItemUpdateView.as_view(), name='item-update'),

    # /inventory/<id>/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ItemDeleteView.as_view(), name='item-delete')
]


