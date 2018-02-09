from django.conf.urls import url
from django.contrib import admin
from auth_u import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.RegisterFormView.as_view())
]