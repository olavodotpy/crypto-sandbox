from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from typing import Dict
import requests





class APIHandler:
    """
        handl = APIHandler("URL")
    
    param = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }

    path = handl.get_path_URL("simple/price")

    handl.printResponse(param)

    """
    def __init__(self, base_URL) -> None:
        self.base_URL = base_URL


    def get_base_URL(self) -> str:
        return self.base_URL


    def get_path_URL(self, path_param) -> str:
        return f"{self.base_URL}/{path_param}"


    def search_object(self) -> dict:
        pass


    def JSON_response(self, path, query_params: Dict = {}) -> dict:
        try:
            response = requests.get(path, params=query_params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as _:
            return {"error": _}


    def printResponse(self, query_params: Dict = {}) -> str:
        print(str(self.JSON_response(path, query_params)))



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