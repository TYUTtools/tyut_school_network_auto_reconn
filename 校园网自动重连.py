from re import T
import requests
from time import sleep
from datetime import datetime


def xiaoyuanwang_test():
    try:
        res = requests.get('https://baidu.com')
        print(datetime.now(), '网络正常。')
        return True
    except BaseException as e:
        print(e)
        print('连接断开！正在尝试重连...')
        # login_url = "http://219.226.127.250:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=219.226.127.250&port=&iTermType=1&wlanuserip=&wlanacip=&wlanacname=&redirect=&session=&ssid=&vlanid=&queryACIP=0&jsVersion=1.3.8&isTelephone=0&DDDDD=,0,【校园网用户名】&upass=【校园网密码】&R1=0&R2=&R6=0&v6ip=&para=00&0MKKey=123456"
        login_url = "http://219.226.127.250:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C【校园网用户名】&user_password=【校园网密码】&wlan_user_ip=101.7.172.6&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=8262&lang=zh"
        try:
            requests.get(login_url)
            res = requests.get('https://baidu.com')
            print('重连成功！')
            return True
        except BaseException as e:
            print('重连失败！')
            print(e)
            return False
    return True

if __name__ == '__main__':
    count=0
    while 1:
        flag = xiaoyuanwang_test()
        if flag:
            count = 0
        else:
            count+=1
        if count>10:
            exit()
        sleep(60)