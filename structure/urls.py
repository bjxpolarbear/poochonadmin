from . import views
from django.conf.urls import url


app_name = 'structure'

urlpatterns = [

    # /structure/
    url(r'^$', views.StructureIndexView.as_view(), name='index'),

    # /structure/packages/json/
    url(r'^packages/json$', views.ServicePackageJsonView.as_view(), name='quote-json'),

    # /structure/services/json/
    url(r'^services/json$', views.ServiceJsonView.as_view(), name='quote-json'),
]
