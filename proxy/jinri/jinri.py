# coding=utf-8
import json
import requests
from lxml import etree
import tools

ips_http, ips_https = [], []
i = tools.get_date()


def run():
    host = "ip.ihuan.me"
    headers = {
        'User-Agent': tools.get_ua(),
        'Host': host,
    }

    def get_url():
        url = 'https://ip.ihuan.me/today.html'
        r = requests.get(url, headers=headers)
        selector = etree.HTML(r.text)
        target_url = selector.xpath("//div[@class='bs-callout bs-callout-info'][1]//@href")[0]
        return target_url

    url = 'https://' + host + get_url()
    print(url)

    r = requests.get(url, headers=headers)
    print(r.status_code)

    selector = etree.HTML(r.text)
    info_list = selector.xpath("//div[@class='panel-default']/div[@class='panel-body']")[0]
    ip_count = info_list.xpath(".//ol[@class='breadcrumb']//text()")[2]
    print(ip_count)
    ip_lists = info_list.xpath("./p[@class='text-left']//text()")
    print(ip_lists)
    # [' 39.137.69.7:8080@HTTP#[高匿]天津天津 移动', '39.137.69.9:80@HTTP#[高匿]天津天津 移动']
    for item in ip_lists:
        item_list = item.split('#')

        # 去除第一个字段没有ip
        if len(item_list[0]) < 10:
            continue

        # 存到列表
        if len(item_list) == 4:  # 长度为4的支持HTTPS
            print(item_list)
            ips_https.append(item_list)
        if 1 < len(item_list) < 4:
            ips_http.append(item_list)


# 存储到json文件
def write_to_txt(ips_http, ips_https):
    with open("jinri_ips_http.json", "w", encoding='utf-8') as f:
        json.dump(ips_http, f, ensure_ascii=False)

    with open("jinri_ips_https.json", "w", encoding='utf-8') as f:
        json.dump(ips_https, f, ensure_ascii=False)


if __name__ == "__main__":
    print("==================同步第{}页=====================".format(i))
    run()
    write_to_txt(ips_http, ips_https)
    print(len(ips_http + ips_https))
