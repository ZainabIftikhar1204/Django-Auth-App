from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime

@api_view(['GET'])
def index(request):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    msg = "Server is Live! Current Time is: "
    return Response(data=msg + date, status=status.HTTP_200_OK)

