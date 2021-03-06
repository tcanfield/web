from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from hellodjango.views import hello, current_datetime, hours_ahead, index
from hellodjango.books import views
from bible.views import initdb, daily, register
from sudoku.views import sudoku
from disick.views import disick
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('', 
	(r'^$', index),
	url(r'^hello/$', hello),
	url(r'^time/$', current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^search/', views.search),
	url(r'^initdb/', initdb),
	url(r'^daily/$', daily),
        url(r'^sudoku/$', sudoku),
        url(r'^disick/$', disick),
	url(r'^registration/register/$', register),
	(r'^accounts/login/$', login),
	(r'^accounts/logout/$', logout),
	(r'^admin/', include(admin.site.urls)),
)
