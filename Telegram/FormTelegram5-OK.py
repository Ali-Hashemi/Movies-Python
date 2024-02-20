import requests

proxies = {
    'http': 'socks5://Gj9v9s9SNJ:jNehysEglj@95.216.110.109:44073'
    # 'https': 'socks5://Gj9v9s9SNJ:jNehysEglj@95.216.110.109:44073'
}

url = 'https://httpbin.org/ip'
response = requests.get(url, proxies=proxies)

print(response)

import sys
# import socks

from telethon import TelegramClient
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.errors import FloodWaitError, RPCError

# username = "Gj9v9s9SNJ"
# password = "jNehysEglj"
# host = "95.216.110.109"  # a valid host
# port = "44073"  # a valid port
# proxy = (socks.SOCKS5, host, port, True, username, password)
