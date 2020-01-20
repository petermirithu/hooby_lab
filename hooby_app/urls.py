from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url('^$',views.home,name="home"),
    url(r'logout/',views.logout_request,name="logout"),
    url(r'^accounts/profile/',views.user_profile,name="profile"), 
    path('user/profile/<user_name>/',views.other_user_profile,name="othersprofile"), 
    url(r'^update/profile/',views.update_profile,name="updateprofile"),

]
