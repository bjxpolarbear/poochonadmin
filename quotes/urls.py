from django.conf.urls import url
from . import views


app_name = 'quotes'

urlpatterns = [
    # /quotes
    url(r'^$', views.QuoteIndexView.as_view(), name='index'),
]