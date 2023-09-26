from re import T
import requests
from time import sleep
from datetime import datetime

user_account = 'xiaoming5567'  # 校园网用户名，通常为姓名拼音加上学号后四位
user_password = 'MDij0765'  # 校园网密码，通常由两个大写字母+两个小写字母+四位数字组成


def get_local_ip():
    import socket

    # 获取本机计算机名称
    hostname = socket.gethostname()
    # 获取本机ip
    ip = socket.gethostbyname(hostname)
    return ip


def xiaoyuanwang_test():
    try:
        res = requests.get('https://baidu.com')
        print(datetime.now(), '网络正常。')
        return True
    except BaseException as e:
        print(e)
        print('连接断开！正在尝试重连...')

        login_url = f"http://219.226.127.250:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C{user_account}&user_password={user_password}&wlan_user_ip={get_local_ip()}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=4005&lang=zh"

        try:
            res1 = requests.get(login_url)
            res = requests.get('https://baidu.com')
            print('重连成功！')
            return True
        except BaseException as e:
            print('重连失败！', res1.text)
            print(e)
            return False
    return True


if __name__ == '__main__':
    count=0
    print(get_local_ip())
    while 1:
        flag = xiaoyuanwang_test()
        if flag:
            count = 0
        else:
            count+=1
        if count>10:
            exit()
        sleep(60)