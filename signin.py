#! /usr/bin/python
import requests
import json
from time import time, localtime
from sys import argv

def get_today():
    nowtime = localtime(time())
    return f"{nowtime.tm_year}.{nowtime.tm_mon}.{nowtime.tm_mday}"


def signin(cookie):
    print("signing in...")
    
    # 创建一个session,作用会自动保存cookie
    session = requests.session()
    # 点签到之后的页
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    #checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    #state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    # 请求负载
    payload = {
        # 'token': 'glados_network'
        'token': 'glados.one'
    }
    # referer 当浏览器向web服务器发送请求的时候，一般会带上Referer，告诉服务器我是从哪个页面链接过来的，服务器 籍此可以获得一些信息用于处理。
    # json.dumps请求序列化
    checkin = session.post(url, headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent,
                           'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload)) # proxies=proxies)
    state = session.get(url2, headers={'cookie': cookie, 'referer': referer,
                        'origin': origin, 'user-agent': useragent}) # proxies=proxies)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        text = mess + '，you have '+time+' days left'
        return text

def get_result(cookie):
    success = True
    day = get_today()
    try:
        res = signin(cookie)
    except Exception as e:
        success = False
        res = str(e)
    if success:
        res = f"时间：{day} （UTC+8）\n结果：{res}"
    else:
        res = f"时间：{day} （UTC+8）\n结果：签到失败。\n原因：{res}"
    with open("result.txt", mode="w", encoding="utf-8") as f:
        f.write(res)
    return res

if __name__ == "__main__":
    cookie = argv[1]
    res = get_result(cookie)
    print(res)
