from django.urls import path
from . import views

urlpatterns = [
    path('movies', views.get_movies, name='token_refresh'),
    path('register', views.login, name='token_refresh'),
]