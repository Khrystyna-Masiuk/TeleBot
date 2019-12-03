import re  
import requests  
import json  
  
  
URL = "https://deezerdevs-deezer.p.rapidapi.com/search"

  

def load_api():  
    return json.loads(requests.get(URL).text)  
  
  
# def get_api(ccy_key):  
#     for exc in load_api():  
#         if ccy_key == exc['ccy']:  
#             return exc  
#     return False  
  
  
# def get_apis(ccy_pattern):  
#     result = []  
#     ccy_pattern = re.escape(ccy_pattern) + '.*'  
#   for exc in load_exchange():  
#         if re.match(ccy_pattern, exc['ccy'], re.IGNORECASE) is not None:  
#             result.append(exc)  
#     return result