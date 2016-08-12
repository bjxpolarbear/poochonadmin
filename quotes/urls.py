from django.conf.urls import url
from . import views


app_name = 'quotes'

urlpatterns = [
    # /quotes
    url(r'^$', views.QuoteIndexView.as_view(), name='index'),

    # /quotes/<quote_id>
    url(r'^(?P<pk>[0-9]+)$', views.QuoteDetailView.as_view(), name='detail'),

    # /quotes/create
    url(r'^create/$', views.QuoteCreateView.as_view(), name='quote-create'),
    url(r'^create/(?P<pk>[0-9]+)$', views.QuoteCreateView.as_view(), name='quote-create'),

    # /quotes/<quote_id>/update
    url(r'^(?P<pk>[0-9]+)/update/$', views.QuoteUpdateView.as_view(), name='quote-update'),

    # /quotes/<quote_id>/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.QuoteDeleteView.as_view(), name='quote-delete'),

    # /quotes/<quote_id>/convert/
    url(r'^(?P<pk>[0-9]+)/convert/$', views.ConvertToOrderView.as_view(), name='quote-convert')
]