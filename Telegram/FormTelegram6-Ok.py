import requests
from Classes.ClassUtility import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
}

# url = 'https://httpbin.org/ip'
# response = requests.get(url, proxies=proxies)

def send_msg(text):
   token = "6095108707:AAEctbEfBShqydGmK874LbDm93Kt5OOlAmk"
   chat_id = 839526387
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=-" + str(chat_id) + "&text=" + str(text)
   # results = requests.get(url_req,proxies=proxies)

   # print(results.json())

   Html.get_soup_for_subscene(url_req)

send_msg("Hello there!")