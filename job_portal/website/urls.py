from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
urlpatterns = [

    url(r'^$', views.homepage,name = 'home-page'),
    url(r'^register/$', views.user_registration, name='user-registration'),
    url(r'^login/$', auth_views.login,{'template_name':'loginpage.html'},name='login-page')
]
