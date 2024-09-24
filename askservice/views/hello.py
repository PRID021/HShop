from requests import Response
from rest_framework.views import APIView


class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})
