
from . import views
from django.conf.urls import url


app_name = 'clients'

urlpatterns = [
    # /clients
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /clients/<client_id>
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),

    # /clients/add
    url(r'^add/$', views.ClientCreate.as_view(), name='client-add'),

    # /clients/<client_id>/update/
    url(r'^(?P<pk>[0-9]+)/update/$', views.ClientUpdate.as_view(), name='client-update'),

    # /clients/<client_id>/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ClientDelete.as_view(), name='client-delete')
]



