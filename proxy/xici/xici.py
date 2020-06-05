# coding=utf-8
import json
import requests
from lxml import etree
import tools

ips_http, ips_https = [], []


def run(page):
    url = "https://www.xicidaili.com/nn/{}"
    headers = {
        'User-Agent': tools.get_ua(),
        'Host': "www.xicidaili.com",
    }
    r = requests.get(url.format(page), headers=headers)
    print(r.status_code)

    selector = etree.HTML(r.text)
    info_list = selector.xpath('//table[@id="ip_list"]//tr')
    print(info_list)
    info_list = info_list[1:]
    for info in info_list:
        ip = ''.join(info.xpath('./td[2]/text()'))
        port = ''.join(info.xpath('./td[3]/text()'))
        protocol = (''.join(info.xpath('./td[6]/text()'))).lower()
        speed = (''.join(info.xpath('./td[7]//@style'))).lower()
        conTime = (''.join(info.xpath('./td[8]//@style'))).lower()
        life = (''.join(info.xpath('./td[9]/text()'))).lower()

        # 存到列表
        if protocol == 'http':
            ips_http.append([protocol + "://" + ip + ":" + port, speed, conTime, life])
        if protocol == 'https':
            ips_https.append([protocol + "://" + ip + ":" + port, speed, conTime, life])


# 存储到json文件
def write_to_txt(ips_http, ips_https):
    with open("xici_ips_http.json", "w", encoding='utf-8') as f:
        json.dump(ips_http, f, ensure_ascii=False)

    with open("xici_ips_https.json", "w", encoding='utf-8') as f:
        json.dump(ips_https, f, ensure_ascii=False)


if __name__ == "__main__":
    for i in range(1, 2):
        print("==================同步第{}页=====================".format(i))
        run(i)
    write_to_txt(ips_http, ips_http)
    print(len(ips_http + ips_https))
