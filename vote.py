import random
from random import choice
import sys
import time
import datetime
import threading
import re

import requests
from bs4 import BeautifulSoup


# 构建ip pool-可用的ip池
def get_ip():
    url = 'http://www.xicidaili.com/nn'
    my_headers = {
        'Accept': 'text/html, application/xhtml+xml, application/xml;',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Referer': 'http: // www.xicidaili.com/nn',
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 45.0.2454.101Safari / 537.36'
    }
    r = requests.get(url,headers=my_headers)
    soup = BeautifulSoup(r.text,'html.parser')
    data = soup.find_all('td')
    ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')  #匹配IP
    port_compile = re.compile(r'<td>(\d+)</td>')  #匹配端口
    ip = re.findall(ip_compile,str(data))    #获取所有IP
    port = re.findall(port_compile,str(data))  #获取所有端口
    ip_pool = [':'.join(i) for i in zip(ip,port)]  #列表生成式
    #组合IP和端
    print (ip_pool)
    return ip_pool

# 设置user-agent列表,每次请求时，随机挑选一个user-agent
ua_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
    ]

def get_url(url,code=0,ips=[]):
    try:
        ip = choice(ips)
    except:
        return False
    else:
        #指定代理ip
        proxies = {
            'http':ip
        }
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Content-Type":"application/x-www-form-urlencoded",
        
        "Host":"www.rp-china.org",
        "Origin":"http://www.rp-china.org",
        "Referer":"http://www.rp-china.org/redirect.php?tid=25305&goto=lastpost",
        "Upgrade-Insecure-Requests":"1",
        'User-Agent':choice(ua_list)
        }
    try:

        url1 = "http://www.rp-china.org/misc.php?action=votepoll&fid=7&tid=25305&pollsubmit=yes&quickforward=yes&inajax=1"
        data = {"formhash":"ec376ded","pollanswers[]":"289"}
        s = requests.get(url=url,proxies=proxies)
        result = requests.post(url=url1,data=data,headers=headers,proxies=proxies)
    except requests.exceptions.ConnectionError:
        print('ConnectionError')
        if not ips:
            print ('ip 已失效')
            sys.exit()
        if ip in ips:
            ips.remove(ip)
        get_url(url,code,ips)
    else:
        date = datetime.datetime.now().strftime('%H:%M:%S')
        print(result.text)
        print("第{}次投票成功\n时间：{}\n所用ip：{} \n剩余ip数：{}".format(code,date,ip,len(ips)))
        print("------------")


def main(url):
    ips = []
    #xrange() 生成的是一个生成器
    for i in range(500):
        # 每隔1000次重新获取一次最新的代理IP，每次可获取最新的100个代理IP
        if i % 100 == 0:
            ips.extend(get_ip())
        #启动线程，每隔1s产生一个线程，可通过控制时间加快投票速度
        t1 = threading.Thread(target=get_url,args=(url,i,ips))
        t1.start()
        time.sleep(1)  #time.sleep的最小单位是毫秒

if __name__ == '__main__':

    url = "http://www.rp-china.org/redirect.php?tid=25305&goto=lastpost#lastpost"
    main(url)
