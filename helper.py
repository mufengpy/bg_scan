import re
import json
import random
import requests
from tools import get_ua
import sys

finished_line_num = 0  # 正在执行第几行
session = requests.Session()

line_num = 0  # line_num 用于统计行数


# print(session)

def isFalse(arg):
    '如果arg为假'
    if not arg:
        return True


def get_ui_args():
    import os
    from tools import file_len

    files = [item for item in os.listdir('conf') if item.endswith('.txt')]

    dic_len = dict([(item, file_len('conf/' + item)) for item in files])

    return dic_len


def get_domain(url):
    def get_status(url):
        return True if requests.get(url).status_code is 200 else False

    if not get_status(url):
        sys.exit()

    from urllib.parse import urlparse
    path = urlparse(url)
    if path.scheme:
        domain_url = path.scheme + "://" + path.netloc
    else:
        domain_url = 'http://' + path.netloc
        domain_url = 'https://' + path.netloc if get_status(domain_url) is False else domain_url

    return domain_url


def CheckUrl(url):
    '检测url是否合法'

    # 1.是否为空
    if not url.strip():
        return
    # 2.是否是http/https开头
    elif not re.match(r'^https?:/{2}\w.+$', url):
        return
    # 3.url不带http/https开头
    elif re.match(r'^www.\w.+$', url):
        print('带上http也没用阿')
        return
    else:
        return get_domain(url)


def scan(self, url, need_status_code, need_dic_line_nums, timeout=2):
    def startRequest(url):
        '发送请求'
        headers = {
            "User-Agent": get_ua(),
        }
        global session
        # http_type = url.split(':')[0]
        proxy = get_ip()

        proxies = {
            "http": "http://{}".format(proxy),
            "https": "https://{}".format(proxy),
        }
        # {'http': 'http://60.205.132.71:80', 'https': 'https://60.205.132.71:80'}

        resp = session.get(url.strip(), headers=headers, timeout=timeout, proxies=proxies)
        resp_status_code = str(resp.status_code)
        title_need_status_code = [item[0] for item in need_status_code]

        global finished_line_num
        finished_line_num += 1

        print(need_dic_line_nums, resp_status_code, url, proxies)
        rate = round(finished_line_num / need_dic_line_nums, 3)
        print(rate)
        self.m_gauge1.SetValue(rate * 100)

        if resp_status_code[0] in title_need_status_code:  # eg. need_status_code 2XX 3XX
            print('6666', url, resp_status_code)
            global line_num
            self.m_grid1.SetCellValue(line_num, 0, url)
            self.m_grid1.SetCellValue(line_num, 1, resp_status_code)

            line_num += 1
        # print(resp_status_code)

    def start():
        startRequest(url)

    try:
        start()
    except Exception as e:
        print(e)


def get_ip_old(http_type, platform='jinri'):
    if http_type == 'http':
        with open("proxy/{}/usable_{}_ips_http.json".format(platform, platform), "r", encoding='utf-8') as f:
            f = json.load(f)
    if http_type == 'https':
        with open("proxy/{}/usable_{}_ips_https.json".format(platform, platform), "r", encoding='utf-8') as f:
            f = json.load(f)

    return random.choice(f)


def get_ip():
    resp_json = requests.get("http://111.231.109.232:5010/get/").json()
    return resp_json['proxy']

