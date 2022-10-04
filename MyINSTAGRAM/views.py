from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    # 클래스 Sub 실행시 get으로 호출할 경우 실행
    def get(self, request):
        return render(request, "myinstagram/main.html")

    # 클래스 Sub 실행시 post로 호출할 경우 실행
    def post(self, request):
        return render(request, "myinstagram/main.html")
