import threading
import requests
from tools import get_ua
from helper import get_ip

requests.packages.urllib3.disable_warnings()

test_url_http = 'http://www.longchenggroup.com/'
test_url_https = 'https://ip.ihuan.me/'

PRO_TYPE = ['http', 'https']

headers = {
    "User-Agent": get_ua(),
}


def handIp():
    proxy = get_ip()
    # print(proxy)

    # proxy = "39.137.69.6:8080"

    proxies = {
        "http": "http://{}".format(proxy),  # "60.216.20.210:8001"
        "https": "https://{}".format(proxy),  # http://175.148.71.67:1133
    }

    try:
        resp = requests.get(test_url, proxies=proxies, headers=headers, timeout=0.3)
        if resp.status_code is 200:
            print('ok', proxy)
    except Exception:
        pass


if __name__ == '__main__':
    pro_type = PRO_TYPE[0]  # 可控参数
    test_url = test_url_http

    print(pro_type)

    while True:
        i = 0
        thread_obj = threading.Thread(target=handIp, args=())
        thread_obj.start()
        i += 1
