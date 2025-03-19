import requests
import json
import os
import datetime


from datetime import date

# 获取当前日期
today = datetime.date.today()
print(today)









#初始化所有response
response_1, response_2, response_3, response_4, response_5, response_6, response_7, response_8, response_9 = None, None, None, None, None, None, None, None, None

status_code=None
file_path="config.json"
if os.path.exists(file_path):
    print(f"{file_path} 文件存在")
else:
    print(f"{file_path} 文件不存在")
    params = {
        'text': "自动发get请求失败",
        'desp': "cookie文件不存在"
    }
#    response = requests.get(iyuuurl, params=params)




with open('config.json', 'r', encoding='utf-8') as f:
    cookies_data = json.load(f)


cookies_cyanbug = cookies_data['cyanbug']
cookies_tosky = cookies_data['tosky']
cookies_qingwapt = cookies_data['qingwapt']
cookies_xiangdao = cookies_data['xiangdao']
cookies_zmpt = cookies_data['zmpt']


print(cookies_xiangdao)
iyuu_key = cookies_data.get("iyuu_key", "")
iyuuurl = f"https://iyuu.cn/{iyuu_key}.send"
tosky喊 = cookies_data.get("tosky喊","")
青蛙喊=cookies_data.get("青蛙喊","")
大青虫喊=cookies_data.get("大青虫喊","")
象岛喊=cookies_data.get("象岛喊","")
zmpt喊=cookies_data.get("zmpt喊","")



大青虫固定几号喊VIP=cookies_data.get("大青虫固定几号喊VIP","")
int(大青虫固定几号喊VIP)
print(tosky喊,青蛙喊,大青虫喊,象岛喊)
print(大青虫固定几号喊VIP)


if today.day==大青虫固定几号喊VIP:
    print("今天是设定的日期")
else:
    print("今天不是设定的日期")



# 第一个目标URL和请求设置


url_base = "https://cyanbug.net/shoutbox.php"


# 请求参数
params_1 = {
    'shbox_text': '青虫娘，求上传',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}

params_2 = {
    'shbox_text': '青虫娘，求魔力',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}
params_5 = {
    'shbox_text': '青虫娘，求彩虹id',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}

params_6 = {
    'shbox_text': '青虫娘，求vip',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}
# 请求头
headers = {
    'Host': 'cyanbug.net',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'iframe',
    'Referer': 'https://cyanbug.net/index.php',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5',
    'Priority': 'u=0, i'
}


# 发送第一个GET请求
if 大青虫喊== "开":
    try:
        response_1 = requests.get(url_base, headers=headers, cookies=cookies_cyanbug, params=params_1)
        print("Response 1:")
        print(response_1.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during request 1: {e}")

    # 发送第二个GET请求
    try:
        response_2 = requests.get(url_base, headers=headers, cookies=cookies_cyanbug, params=params_2)
        print("Response 2:")
        print(response_2.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during request 2: {e}")
    if today.day == 大青虫固定几号喊VIP:
        try:
            response_5 = requests.get(url_base, headers=headers, cookies=cookies_cyanbug, params=params_5)
            print("Response 5:")
            print(response_5.text)
        except requests.exceptions.RequestException as e:
            print(f"Error during request 2: {e}")

        try:
            response_6 = requests.get(url_base, headers=headers, cookies=cookies_cyanbug, params=params_6)
            print("Response 6:")
            print(response_6.text)
        except requests.exceptions.RequestException as e:
            print(f"Error during request 2: {e}")







# tosky 喊
url = "https://t.tosky.club/shoutbox.php"

# 请求参数
params3 = {
    'shbox_text': '来点上传',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}
params4 = {
    'shbox_text': '来点魔力',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}
# 请求头
headers = {
    'Host': 't.tosky.club',
    'Sec-Ch-Ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'iframe',
    'Referer': 'https://t.tosky.club/index.php',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
    'Priority': 'u=0, i'
}


#tosky

if tosky喊== "开" :
    try:
        response_3 = requests.get(url, headers=headers, cookies=cookies_tosky, params=params3)
        print("Response 3:")
        print(response_3.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during request 3: {e}")

    try:
        response_4 = requests.get(url, headers=headers, cookies=cookies_tosky, params=params4)
        print("Response 3:")
        print(response_4.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during request 3: {e}")



#青蛙喊
url= "https://www.qingwapt.com/shoutbox.php"
params7 = {
    'shbox_text': '蛙总，求上传',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}
params8 = {
    'shbox_text': '蛙总，求下载',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}
headers = {
    'Host': 'www.qingwapt.com',
    'Sec-Ch-Ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'iframe',
    'Referer': 'https://www.qingwapt.com/index.php',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
    'Priority': 'u=0, i'
}

#青蛙


if 青蛙喊== "开" :
    try:
        response_7 = requests.get(url, headers=headers, cookies=cookies_qingwapt, params=params7)
        print("Response 7:")
        print(response_7.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during request 3: {e}")

    # 以下为青蛙喊下载，需要请自己删除注释符号
    # try:
    #     response_8 = requests.get(url, headers=headers, cookies=cookies_qingwapt, params=params8)
    #     print("Response 8:")
    #     print(response_8.text)
    # except requests.exceptions.RequestException as e:
    #     print(f"Error during request 3: {e}")




#象岛
xdurl="https://ptvicomo.net/shoutbox.php"
params9 = {
    'shbox_text': '小象求象草',
    'shout': '发送',
    'sent': 'yes',
    'type': 'shoutbox'
}



headers = {
    'Host': 'ptvicomo.net',
    'Sec-Ch-Ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'iframe',
    'Referer': 'https://ptvicomo.net/index.php',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
    'Priority': 'u=0, i'
}


if 象岛喊=="开":
    try:
        response_9 = requests.get(xdurl, headers=headers, cookies=cookies_xiangdao, params=params9)
        print("Response 9:")
        print(response_9.text)

    except requests.exceptions.RequestException as e:
        print(f"Error during request 3: {e}")



#zmpt


xdurl="https://zmpt.cc/shoutbox.php"
params10 = {
    'shbox_text': '皮总，求电力',
    'shout': '发送',
    'sent': 'yes',
    'type': 'shoutbox'
}
params11 = {
    'shbox_text': '皮总，求上传',
    'shout': '发送',
    'sent': 'yes',
    'type': 'shoutbox'
}



headers = {
    'Host': 'zmpt.cc',
    'Sec-Ch-Ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'iframe',
    'Referer': 'https://zmpt.cc/index.php',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
    'Priority': 'u=0, i'
}




if zmpt喊=="开":
    try:
        response_10=requests.get(xdurl, headers=headers, cookies=cookies_zmpt, params=params10)
        print("Response 10:")
        print(response_10.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during request 3: {e}")

    try:
        response_11 = requests.get(xdurl, headers=headers, cookies=cookies_zmpt, params=params11)
        print("Response 11:")
        print(response_11.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during request 3: {e}")





#初始化iyuu返回值
r1, r2, r3, r4, r5, r6, r7, r8,r9,r10,r11= "", "", "", "", "", "", "", "","","",""

# 检查每个响应状态
if response_1 is not None:
    if response_1.status_code < 300:
        r1 = "大青虫上传求成功\n"
    else:
        r1 = "大青虫求上传失败，HTTP响应: " + str(response_1.status_code) + "\n"
else:
    r1 = "大青虫求上传失败，无响应\n"

if response_2 is not None:
    if response_2.status_code < 300:
        r2 = "大青虫魔力求成功\n"
    else:
        r2 = "大青虫求魔力失败，HTTP响应: " + str(response_2.status_code) + "\n"
else:
    r2 = "大青虫求魔力失败，无响应\n"

if response_3 is not None:
    if response_3.status_code < 300:
        r3 = "tosky求上传成功\n"
    else:
        r3 = "tosky求上传失败，HTTP响应: " + str(response_3.status_code) + "\n"
else:
    r3 = "tosky求上传失败，无响应\n"

if response_4 is not None:
    if response_4.status_code < 300:
        r4 = "tosky求魔力成功\n"
    else:
        r4 = "tosky求魔力失败，HTTP响应: " + str(response_4.status_code) + "\n"
else:
    r4 = "tosky求魔力失败，无响应\n"

if response_5 is not None:
    if response_5.status_code < 300:
        r5 = "大青虫求彩虹ID成功\n"
    else:
        r5 = "大青虫求彩虹ID失败，HTTP响应: " + str(response_5.status_code) + "\n"
else:
    r5 = "大青虫求彩虹ID失败，无响应\n"

if response_6 is not None:
    if response_6.status_code < 300:
        r6 = "大青虫求VIP成功\n"
    else:
        r6 = "大青虫求VIP失败，HTTP响应: " + str(response_6.status_code) + "\n"
else:
    r6 = "大青虫求VIP失败，无响应\n"

if response_7 is not None:
    if response_7.status_code < 300:
        r7 = "青蛙求上传成功\n"
    else:
        r7 = "青蛙求上传失败，HTTP响应: " + str(response_7.status_code) + "\n"
else:
    r7 = "青蛙求上传失败，无响应\n"

if response_8 is not None:
    if response_8.status_code < 300:
        r8 = "青蛙求下载成功\n"
    else:
        r8 = "青蛙求下载失败，HTTP响应: " + str(response_8.status_code) + "\n"
else:
    r8 = "青蛙求下载失败，无响应\n"


if response_9 is not None:
    if response_9.status_code < 300:
        r9 = "象岛求象草成功\n"
    else:
        r9 = "象岛求象草失败，HTTP响应: " + str(response_9.status_code) + "\n"
else:
    r9 = "象岛求象草失败，无响应\n"





if response_10 is not None:
    if response_10.status_code < 300:
        r10 = "织梦求电力成功\n"
    else:
        r10 = "织梦求电力失败失败，HTTP响应: " + str(response_9.status_code) + "\n"
else:
    r10 = "织梦求电力失败，无响应\n"


if response_11 is not None:
    if response_11.status_code < 300:
        r11 = "织梦求上传成功\n"
    else:
        r11 = "织梦求上传失败，HTTP响应: " + str(response_9.status_code) + "\n"
else:
    r11 = "织梦求上传失败，无响应\n"









# 打印各个请求的HTTP响应状态码
# 定义text和desp变量
text = "自动发送get请求"
desp = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11

# 定义请求参数
params = {
    'text': text,
    'desp': desp
}

# 发送GET请求
response = requests.get(iyuuurl, params=params)

# 打印响应
print(desp)
print("Response Status Code:", response.status_code)
print("Response Text:", response.text)



