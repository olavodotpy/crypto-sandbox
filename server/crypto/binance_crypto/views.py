from django.shortcuts import render
from typing import Dict, List, Any
import requests





# Vou criar um classe que vai conter a manipulação dessa API como:
# Atributo que guarda a URL principal da REST
# Métodos que façam requisição de path e query
# Métodos que retornan(get) resultados e valores desejados
# que será usados no get do APIView

class CryptoAPIHandler:
    def __init__(self, base_URL) -> None:
        self.base_URL = base_URL


    def get_base_URL(self) -> str:
        return self.base_URL
    

    def add_path_in_URL(self, path_param):
        full_URL = f"{self.base_URL}/{path_param}"
        return full_URL

    
    def add_query_params(self, path, query_pararms):
        full_URL = f"{self.base_URL}/{path}"
        response = requests.get(full_URL, params=query_pararms)
        return response.json()










if __name__ == "__main__":
    pass
    # tratar para sair da melhor forma


    # API_hardl = CryptoAPIHandler("https://api.coingecko.com/api/v3")
    # param = {
    #     'ids': "bitcoin",
    #     'vs_currencies': "usd",
    # }
    # r = API_hardl.add_query_params("simple/price", param)

    # print(r)