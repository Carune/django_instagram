from uuid import uuid4
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed, Reply, Like, Bookmark
from user.models import User
import os
from MyINSTAGRAM.settings import MEDIA_ROOT


class Main(APIView):
    def get(self, request):
        # select * from content_feed; / 새로 추가된 피드가 최상단에 가게 하기 위해 order by 로 id를 역순 정렬
        email = request.session.get('email', None)

        feed_object_list = Feed.objects.all()
        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")

        feed_list = []

        for feed in feed_object_list:
            user = User.objects.filter(email=feed.email).first()
            print(user)
            reply_object_list = Reply.objects.filter(feed_id=feed.id)
            reply_list = []
            for reply in reply_object_list:
                user = User.objects.filter(email=reply.email).first()
                reply_list.append(dict(
                    reply_content=reply.reply_content, nickname=user.nickname))

            like_count = Like.objects.filter(
                feed_id=feed.id, is_like=True).count()
            is_liked = Like.objects.filter(
                feed_id=feed.id, email=email, is_like=True).exists()
            is_marked = Bookmark.objects.filter(
                feed_id=feed.id, email=email, is_marked=True).exists()

            feed_list.append(dict(id=feed.id, image=feed.image, content=feed.content, like_count=like_count,
                                  profile_image=user.profile_image, nickname=user.nickname, reply_list=reply_list, is_liked=is_liked, is_marked=is_marked))

        # for feed in feed_list:
        #     print(feed.content) # db 의 content(글 내용) 출력하여 확인해보기

        return render(request, "myinstagram/main.html", context=dict(feeds=feed_list, user=user))


class UploadFeed(APIView):
    def post(self, request):

        # 파일 불러오기
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        file = request.data.get('file')
        image = uuid_name
        content = request.data.get('content')
        email = request.session.get('email', None)

        Feed.objects.create(image=image, content=content,
                            email=email)

        return Response(status=200)


class Profile(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")

        feed_list = Feed.objects.filter(email=email).all()
        like_list = list(Like.objects.filter(
            email=email, is_like=True).values_list('feed_id', flat=True))
        my_like = Feed.objects.filter(id__in=like_list)

        bookmark_list = list(Bookmark.objects.filter(
            email=email, is_marked=True).values_list('feed_id', flat=True))
        my_bookmark = Feed.objects.filter(id__in=bookmark_list)

        return render(request, 'content/myprofile.html', context=dict(my_bookmark=my_bookmark, my_like=my_like, feed_list=feed_list, user=user))


class UploadReply(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        reply_content = request.data.get('reply_content', None)
        email = request.session.get('email', None)

        Reply.objects.create(
            feed_id=feed_id, reply_content=reply_content, email=email)

        return Response(status=200)


class ToggleLike(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        favorite_text = request.data.get('favorite_text', True)

        if favorite_text == 'favorite':
            is_like = True
        else:
            is_like = False

        email = request.session.get('email', None)

        # 기존에 좋아요를 누른 기록이 있다면 현재 상태로 업데이트하고, 없다면 새로 생성
        like = Like.objects.filter(feed_id=feed_id, email=email).first()

        if like:
            like.is_like = is_like
            like.save()
        else:
            Like.objects.create(
                feed_id=feed_id, is_like=is_like, email=email)

        return Response(status=200)


class ToggleBookmark(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        bookmark_text = request.data.get('bookmark_text', True)

        if bookmark_text == 'bookmark':
            is_marked = True
        else:
            is_marked = False

        email = request.session.get('email', None)

        bookmark = Bookmark.objects.filter(
            feed_id=feed_id, email=email).first()

        if bookmark:
            bookmark.is_marked = is_marked
            bookmark.save()
        else:
            Bookmark.objects.create(
                feed_id=feed_id, is_marked=is_marked, email=email)

        return Response(status=200)
