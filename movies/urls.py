from django.conf.urls import include, url
from movies import views

urlpatterns = [
    url(r'^movies', views.MovieList.as_view()),
]
