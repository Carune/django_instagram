"""MyINSTAGRAM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import Sub
from content.views import Main, UploadFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', Main.as_view()),
    # path('content/upload', UploadFeed.as_view())
    path('content/', include('content.urls')),  # content 앱에 있는 url 불러오기
    path('user/', include('user.urls'))
]

# 개발환경에서의 media 파일 서빙 (media 조회)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
