from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["GET"])
def ping(request):
    return Response(status=status.HTTP_200_OK, data={"data": "Hello world!"})
