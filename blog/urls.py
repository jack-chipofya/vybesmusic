from django.urls import path
from . import views
from .views import PostDetail
urlpatterns=[
    path('',views.index,name='index'),
    path('<slug:slug>/',PostDetail.as_view(),name='post_index'),
    path('videos/<slug:slug>/',views.video,name='video'),
    path('news/<slug:slug>/',views.news,name='news')
    ]