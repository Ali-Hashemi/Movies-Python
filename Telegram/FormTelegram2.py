import requests
import os
from Classes.ClassUtility import *
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
}
url = 'https://www.google.com'
# url = 'https://www.baidu.com'
proxy = '5f63276b-a4e0-45da-af40-james@fnl95109.avinav2ray.space:56072?encryption=none&security=none&type=tcp&headerType=http&host=fast.com#adminooo-jamesBond'
proxies = {
    'vless': 'vless://' + proxy
}
# data = requests.get(url, headers=headers, proxies=proxies, timeout=2)
# print(data.text)

token = '6095108707:AAEctbEfBShqydGmK874LbDm93Kt5OOlAmk'
receiver_id = 839526387

content = 'salam'

base_url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=-' + str(receiver_id) + '&text=' + str(
    content)

some_url = "https://api.telegram.org/bot6095108707:AAEctbEfBShqydGmK874LbDm93Kt5OOlAmk/sendMessage?chat_id=-839526387&text=salam"

Html.get_soup_for_subscene(url=base_url)

# print(base_url)

# 'https://api.telegram.org/bot<TOKEN>/getUpdates'


# 'https://api.telegram.org/bot6095108707:AAEctbEfBShqydGmK874LbDm93Kt5OOlAmk/getUpdates'