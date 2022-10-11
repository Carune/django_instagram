from django.urls import path
from .views import UploadFeed, Profile

urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('myprofile', Profile.as_view())
]
