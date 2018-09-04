from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^spectra/', include('spectra.urls')),
    url(r'^', include('spectra.urls')),
]
