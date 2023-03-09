from django.urls import path
from .views import home, registerUser, loginUser, logoutUser
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('register/', registerUser, name='register'),
    path('logout/', logoutUser, name='logout'),
    path('login/', loginUser, name='login')

]