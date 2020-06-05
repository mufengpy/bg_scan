import requests
from tools import get_ua

proxy = '27.188.62.3:8060'

proxies = {
    "http": "http://{}".format(proxy),  # "60.216.20.210:8001"
    "https": "https://{}".format(proxy),  # http://175.148.71.67:1133
}

headers = {
    "User-Agent": get_ua(),
}

test_url = 'http://ehome.homekoo.com/login.php'

resp = requests.get(test_url, proxies=proxies, headers=headers)
print('ok', resp.status_code)
