from django.contrib import admin
from django.urls import path
from posts.views import index,post_list,post_detail,post_create,PostLits,PostDetail

urlpatterns = [
    path('admin/',admin.site.urls),
    path('index/',index),
    #path('posts/',post_list,name='post-list'),
    path('posts/',PostLits.as_view()),
    path('posts/create/',post_create),
    path('posts/<int:pk>/',PostDetail.as_view()),
    #path('posts/<int:post_id>/',post_detail,name='post-detail')
]
