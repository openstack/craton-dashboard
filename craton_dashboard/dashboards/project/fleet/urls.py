from django.conf.urls import url

from craton_dashboard.dashboards.project.fleet import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]

