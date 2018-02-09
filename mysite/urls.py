from django.conf.urls import url, include
from django.contrib import admin
from blog import urls
from blog import urls as url1
from auth_u import urls as url2
from auth_u import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(url1)),
    url(r'^register/$', include(url2)),
]