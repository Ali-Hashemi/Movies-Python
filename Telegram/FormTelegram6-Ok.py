import requests
from Classes.ClassUtility import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
}


# url = 'https://httpbin.org/ip'
# response = requests.get(url, proxies=proxies)

def send_msg(text):
    token = "7063790590:AAG-AyxYSz0EVcSm21QdYecxJoXJ4ut6Ndk"
    # chat_id = "-266914872"
    chat_name = "@james2_channel"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + str(chat_name) + "&text=" + str(
        text)
    # results = requests.get(url_req,proxies=proxies)

    url_req2 = "https://api.telegram.org/bot" + token + "/sendPhoto"
    results = requests.post(url_req2, data={'chat_id': chat_name},
                            files={'photo': open('C:/Users/Ali/Desktop/Temp/Folder.jpg', 'rb')})

    # print(results.json())

    Html.get_soup_for_subscene(url_req2)
    print(url_req)


send_msg("Hello there!")
