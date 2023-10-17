from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # htmx urls
    path('login/htmx/', htmx_login, name='htmx_login'),
    path('register/htmx/', htmx_register, name='htmx_register'),
]