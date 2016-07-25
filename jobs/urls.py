from . import views
from django.conf.urls import url


app_name = 'jobs'

urlpatterns = [
    # /jobs
    url(r'^$', views.JobIndexView.as_view(), name='index'),

    # /jobs/<job_pk>
    url(r'^(?P<job_id>[0-9]+)/$', views.JobDetailView.as_view(), name='detail'),

    # /jobs/create
    url(r'^create/$', views.JobCreateView.as_view(), name='job-create'),

    # # /jobs/<job_id>/update
    # url(r'^(?P<job_id>[0-9]+)/update/$', views.JobUpdate.as_view(), name='job-update'),

]