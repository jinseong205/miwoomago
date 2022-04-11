from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed

class Main(APIView):
    def get(self, request):
        print("call get")
        feed_list= Feed.objects.all()
        return render(request, "miwoomago/main.html", context=dict(feed_list=feed_list))

    def post(self, request):
        print("call post")
        return render(request, "miwoomago/main.html")

