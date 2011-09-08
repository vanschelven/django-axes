from django.conf.urls.defaults import *
from django.http import HttpResponse

from django.contrib import admin
admin.autodiscover()

def success(request):
    return HttpResponse("Success")

urlpatterns = patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^admin/$', include(admin.site.urls)),

    ('.*', success),
)
