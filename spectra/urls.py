from django.conf.urls import url
from . import views

app_name = 'spectra'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^compare_2/$', views.compare2, name='compare_2'),
    url(r'^compare_1/(?P<pk>[0-9]+)$', views.compare1, name='compare_1'),
    url(r'^comparison/$', views.comparison, name='comparison'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]
