from django.urls import path
from .views import SongView, CreateSongView

urlpatterns = [
    path('song', SongView.as_view()),
    path('gen-song', CreateSongView.as_view()),
]
