from django.conf.urls import url
from . import views
from . import gameapp
from django.urls import path

urlpatterns = [
    url('^$',views.home,name="home"),
    url(r'logout/',views.logout_request,name="logout"),
    url(r'^accounts/profile/',views.user_profile,name="profile"), 
    path('user/profile/<user_name>/',views.other_user_profile,name="othersprofile"), 
    url(r'^update/profile/',views.update_profile,name="updateprofile"),
    # game
    url(r'^home/game/$',gameapp.index,name="game_home"),
    url(r'^play/$',gameapp.play,name="play"),
    path('pusher/auth/',gameapp.pusher_authentication,name="push_auth"),
    url(r'^search/music/$',views.fetch_music,name="music"),
    path('music/<str:music_id>/',views.single_music_item,name="single_music"),
    url(r'^add/review/$',views.add_review,name='add_review'),

]
