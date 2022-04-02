from django.shortcuts import render
from rest_framework.views import APIView

class Main(APIView):
    def get(self, request):
        print("call get")
        return render(request, "miwoomago/main.html")

    def post(self, request):
        print("call post")
        return render(request, "main.html")

