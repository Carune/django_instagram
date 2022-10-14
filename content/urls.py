from django.urls import path
from .views import UploadFeed, Profile, UploadReply, ToggleLike, ToggleBookmark, Main

urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('reply', UploadReply.as_view()),
    path('like', ToggleLike.as_view()),
    path('bookmark', ToggleBookmark .as_view()),
    path('myprofile', Profile.as_view()),
]
