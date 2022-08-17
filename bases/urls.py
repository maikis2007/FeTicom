from django.urls import path
from bases.views import BlankView
from django.contrib.auth import views as auth_views

app_name = "bases"
urlpatterns = [
    path('', BlankView.as_view(), name="blank"),
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='bases/login.html'), name="logout"),
]
