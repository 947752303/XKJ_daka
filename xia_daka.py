import requests
import time
import json
import os

one_day = 86400
info = os.environ.get('INFO', '').split('\n')
location = os.environ.get('LOC', '').split('\n')
answers = os.environ.get('ANS', '').split('\n')

uid = info[0]
szyx = info[1]
bj = info[2]
gh = info[3]
xm = info[4]
sjh2 = info[5]
xb = info[6]

latitude = location[0]
longitude = location[1]
jrsfzx3 = location[2]
xxdz41 = location[3]

jrtwfw5 = answers[0]
jrsfcxfrzz8 = answers[1]
jrsfjgwh6 = answers[2]
jrsfjghb7 = answers[3]
jrsfywhrjc9 = answers[4]
jrsfjcgrrq11 = answers[5]
jssfyqzysgl12 = answers[6]
sfcyglq13 = answers[7]
sfncxaswfx16 = answers[8]
jrsfyhbrjc10 = answers[9]
sfyyqxgzz14 = answers[10]

headers = {
    "Host": "ehallplatform.xust.edu.cn",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.26(0x18001a34) NetType/WIFI Language/zh_CN",
    "Content-Type": "text/json",
    "Content-Length": "950",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Accept": "*/*",
    "Origin": "http://ehallplatform.xust.edu.cn",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"http://ehallplatform.xust.edu.cn/default/jkdk/mobile/mobJkdkAdd_test.jsp?uid={uid}="
}


def login(uid):
    url_cookie = f"http://ehallplatform.xust.edu.cn/default/jkdk/mobile/mobJkdkAdd_test.jsp?uid={uid}"
    response = requests.get(url=url_cookie)
    cookies = response.headers["Set-Cookie"].split(";")[0]
    print("cookies-->", cookies)

    return cookies


def getLoction(latitude, longitude):
    url_map = f"https://restapi.amap.com/v3/geocode/regeo?location={longitude}%2C{latitude}&coordsys=gps&output=json&key=15af27a93de4e725ad8ae393767b52bf&extensions=base"
    res = requests.get(url_map)
    loc_addressComponent = res.json()["regeocode"]["addressComponent"]
    szdd4 = f"中国{loc_addressComponent['province']}{loc_addressComponent['city']}{loc_addressComponent['district']}"
    shi = loc_addressComponent['city']
    xian = loc_addressComponent['district']
    sheng = loc_addressComponent['province']

    loc = [szdd4, shi, xian, sheng]

    return loc


def run():
    # 获取位置信息
    loc = getLoction(latitude, longitude)
    # 获取cookies
    cookies = login(uid)

    # 获取打卡时间
    time_int = time.time()
    time_str = time.localtime(time_int)
    time_str_tomorrow = time.localtime(time_int + one_day)
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time_str)
    current_day = time.strftime('%Y-%m-%d', time_str)
    tomorrow_day = time.strftime('%Y-%m-%d', time_str_tomorrow)

    data_json = {
        "xkdjkdk": {
            "szdd4": loc[0],
            "yx": "",
            "id": "",
            "szyx": szyx,
            "xslx": "2",
            "gh": gh,
            "empid": "601146",
            "xm": xm,
            "jrsfyhbrjc10": jrsfyhbrjc10,
            "zy": "",
            "dm": "4007095",
            "shi": loc[1],
            "sfncxaswfx16": sfncxaswfx16,
            "jrtwfw5": jrtwfw5,
            "procinstid": "",
            "jrsfzx3": jrsfzx3,
            "sfxs": "是",
            "xian": loc[2],
            "jg": "",
            "jrsfjghb7": jrsfjghb7,
            "jrsfjcgrrq11": jrsfjcgrrq11,
            "sjh2": sjh2,
            "xb": xb,
            "jingdu": longitude,
            "hqddlx": "1",
            "ymtys": "",
            "xydm": "4007",
            "jrrq1": tomorrow_day,
            "jdlx": "0",
            "bjdm": "4007095",
            "tbsj": current_time,
            "glkssj131": "",
            "jrsfcxfrzz8": jrsfcxfrzz8,
            "guo": "中国",
            "gljssj132": "",
            "fcjtgj17": "",
            "sfcyglq13": sfcyglq13,
            "xxdz41": xxdz41,
            "weidu": latitude,
            "jssfyqzysgl12": jssfyqzysgl12,
            "shzt": "-2",
            "fcjtgj17Qt": "",
            "sfzh": "",
            "bj": bj,
            "sfyyqxgzz14": sfyyqxgzz14,
            "zydm": "",
            "jrsfjgwh6": jrsfjgwh6,
            "sheng": loc[3],
            "time": current_day,
            "jrsfywhrjc9": jrsfywhrjc9,
            "qtxx15": None
        }
    }
    url_daka = "http://ehallplatform.xust.edu.cn/default/jkdk/mobile/com.primeton.eos.jkdk.xkdjkdkbiz.jt.biz.ext"
    data = json.dumps(data_json)
    headers["Cookie"] = cookies
    res = requests.post(url=url_daka, headers=headers, data=data)  # 健康打卡提交
    final = res.text
    print(final)
    if final == "{}":
        print("打卡成功")


if __name__ == "__main__":
    run()
