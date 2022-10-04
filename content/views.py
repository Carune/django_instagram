from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed


class Main(APIView):
    def get(self, request):
        # select * from content_feed; / 새로 추가된 피드가 최상단에 가게 하기 위해 order by 로 id를 역순 정렬
        feed_list = Feed.objects.all().order_by('-id')

        # for feed in feed_list:
        #     print(feed.content) # db 의 content(글 내용) 출력하여 확인해보기

        return render(request, "myinstagram/main.html", context=dict(feeds=feed_list))


class UploadFeed(APIView):
    def post(self, request):

        file = request.data.get('file')
        image = request.data.get('image')
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        return Response(status=200)
