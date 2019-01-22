from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
   url(r'^api/', include('movies.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
