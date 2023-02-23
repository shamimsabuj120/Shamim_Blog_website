from django.urls import path
from App_Blog import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create-blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('blog_details/<str:slug>', views.blog_details, name='blog_details'),
    path('liked_post/<pk>/', views.liked, name='liked_post'),
    path('unliked_post/<pk>/', views.unliked, name='unliked_post'),
    path('my_blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit_blog/<pk>/', views.UpdateBlog.as_view(), name='edit_blog')
]