from django.conf.urls import include, url
from django.contrib import admin
from post.views import PostsList
from post import views



urlpatterns = [
    # url(r'^$', PostsList.as_view(), name = "home"),
    url(r'^$',views.home, name = "home"),
    url(r'(?P<post_id>[^/]+)', views.post_view, name='post'),
    url(r'(?P<post_id>[^/]+)/(?P<slug>[-\w]+)$', views.post_view, name='post_slug'),
] 
