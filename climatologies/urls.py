from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^history/$', views.History, name='history'),
    url(r'^api/v1/json/$', views.ClimaJson, name='climaJson'),
    url(r'^api/v2/json/$', views.ClimaJson2, name='climaJson2'),
    url(r'^graphic/$', views.Graphic, name='graphic'),
    url(r'^graphic/form/$', views.getForm, name='getForm'),
    url(r'^graphic/form/c3/$', views.getFormc3, name='getFormc3'),
    url(r'^ajax/year/$', views.climaParam, name='climaParam'),
]