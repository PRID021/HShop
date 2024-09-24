from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):
    permission_classes = []

    def get(self, request):
        return Response({"message": "Hello, world!"})
