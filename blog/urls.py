from django.conf.urls import url
from django.contrib import admin
from blog import views as view1
from auth_u import views as view2

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', view1.home, name='home'),
    url(r'^about/$', view1.about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', view1.show_article, name='article'),
    url(r'^register/$', view2.RegisterFormView.as_view()) 
]