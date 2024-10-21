from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .handler_api import APIHandler 





class DataTrigger(APIView):
    
    def get(self, request):
        # Making the request to the external API
        handl = APIHandler("https://api.coingecko.com/api/v3")

        path = handl.get_path_URL("simple/price")

        param = {
            "ids": "bitcoin",
            "vs_currencies": "usd",
        }

        response = handl.JSON_response(path, param)

        return Response(response)
