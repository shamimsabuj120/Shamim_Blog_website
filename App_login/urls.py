from django.urls import path
from App_login import views


app_name = 'App_login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('user-change/', views.user_change, name='user_change'),
    path('password/', views.pass_change, name='pass_change'),
    path('add-pro-pic/', views.add_pro_pic, name='add_pro_pic'),
    path('change-pro-pic/', views.change_pro_pic, name='change_pro_pic')
]

