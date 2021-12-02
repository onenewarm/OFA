from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'testproject'


urlpatterns = [
    path('', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('account/register/', views.register_account, name='register_account'),
    path('user/auth/', views.userauth, name='auth'),
    path('sub/', views.sub, name='sub'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path("logout/", views.logout, name="logout"),
    path('sub/<str:sub_name>/', views.detail_sub, name='detail_sub'),
    path('recommend/', views.recommend_sub, name='recommend_sub'), #sub/recommend 에서 recommend로 수정 sub/<str:sub_name>과 충돌
    path('loadcsv/',views.loadcsv)
]
