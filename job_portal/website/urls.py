from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
urlpatterns = [

    url(r'^$', views.homepage,name = 'home-page'),
    url(r'^register/$', views.user_registration, name='user-registration'),
    url(r'^login/$', auth_views.login,{'template_name':'loginpage.html'},name='login-page'),
    url(r'^login/logged_in/$', views.logged_in, name='logged-in'),

    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),

    ### url for job -list detailed page

    url(r'^login/logged_in/(?P<id>\d+)/$',views.job_detail,name = 'job_detail'),

]
