import json
import requests
import threading
from tools import get_ua
from helper import get_ip
import os

PRO_TYPE = ['http', 'https']

os.chdir('..')

requests.packages.urllib3.disable_warnings()

headers = {
    "User-Agent": get_ua(),
}

usable_ip_http, usable_ip_https = list(), list()


def getUsableIps(platform):
    def openFiles():
        '打开代理ip文件'
        with open('proxy/{}/{}_ips_http.json'.format(platform, platform), "r", encoding='utf-8') as f:
            ips_http = json.load(f)
        with open('proxy/{}/{}_ips_https.json'.format(platform, platform), "r", encoding='utf-8') as f:
            ips_https = json.load(f)
        return ips_http, ips_https

    def handIp(proxy, pro_type):
        '得到可用ip'
        proxies = {
            "http": "http://{}".format(proxy),
            "https": "https://{}".format(proxy),
        }

        test_url, usable_ip = None, None

        if pro_type == PRO_TYPE[0]:
            test_url = test_url_http
            usable_ip = usable_ip_http

        if pro_type == PRO_TYPE[1]:
            test_url = test_url_https
            usable_ip = usable_ip_https

        try:
            resp = requests.get(test_url, proxies=proxies, headers=headers, timeout=0.3)
            if resp.status_code == 200:
                print(test_url, proxy)
                usable_ip.append(proxy)
        except Exception:
            pass

    def filterProxy(platform, ips_http, ips_https):
        i = 0
        if platform == 'jinri':
            # ['182.254.183.234:808@HTTP', '[高匿]广东广州 电信/联通/移动', '支持HTTPS', '支持POST']
            for proxy in ips_http:
                proxy = proxy[0].split('@')[0].strip()
                print('{} {} {} test...'.format(PRO_TYPE[0], i, proxy))
                thread_obj = threading.Thread(target=handIp, args=(proxy, PRO_TYPE[0]))
                thread_obj.start()
                i += 1

            for proxy in ips_https:
                proxy = proxy[0].split('@')[0].strip()
                print('{} {} {} test...'.format(PRO_TYPE[1], i, proxy))
                thread_obj = threading.Thread(target=handIp, args=(proxy, PRO_TYPE[1]))
                thread_obj.start()
                i += 1

        # return filterProxy(proxy)

    # 存储到json文件
    def write_to_txt(ips_http, ips_https):
        with open('proxy/{}/usable_{}_ips_http.json'.format(platform, platform), "w", encoding='utf-8') as f:
            json.dump(ips_http, f, ensure_ascii=False)

        with open('proxy/{}/usable_{}_ips_https.json'.format(platform, platform), "w", encoding='utf-8') as f:
            json.dump(ips_https, f, ensure_ascii=False)

    # 1.打开文件，得到爬取的ip
    ips_http, ips_https = openFiles()
    # 2.过滤得到可用的ip
    filterProxy(platform, ips_http, ips_https)
    # 3. 将可用ip存储起来
    write_to_txt(usable_ip_http, usable_ip_https)


if __name__ == '__main__':
    platform = 'jinri'
    test_url_http = 'http://www.longchenggroup.com/'
    test_url_https = 'https://ip.ihuan.me/'
    getUsableIps(platform)
