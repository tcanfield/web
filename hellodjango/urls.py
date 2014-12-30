from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from mysite.views import hello, current_datetime, hours_ahead
from mysite.books import views
from bible.views import initdb, daily, register

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	url(r'^hello/$', hello),
	url(r'^time/$', current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^search/', views.search),
	url(r'^initdb/', initdb),
	url(r'^daily/$', daily),
	url(r'^registration/register/$', register),
	(r'^accounts/login/$', login),
	(r'^accounts/logout/$', logout),
	(r'^admin/', include(admin.site.urls)),
)
