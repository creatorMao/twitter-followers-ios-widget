import imp
import sys
import time
import DBService
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TwitterFollowers():
    def __init__(self):
        self.dbService=DBService.DBService()
        self.GetTwitterFollowers("")

    def RemoveFormat(self,text):
        return text.replace(',','')

    def CalcCountChange(self,followersCount):
        lastCount=0
        nowCount=followersCount
        countKeyField='FOLLOWERS_COUNT'

        last=self.dbService.getFollowers()
        if countKeyField in last.keys():
            lastCount= int(last[countKeyField],10)

        nowCount=int(followersCount,10)

        return nowCount-lastCount

    def requestDeal(self,url):
        i = 0
        while i < 3:
            try:
                time.sleep(0.5)
                return  requests.get(url, timeout=5,headers=self.headers)
            except requests.exceptions.RequestException:
                print(url)
                print("[请求超时]:第"+str(i+1)+"次请求超时！即将进行第"+str(i+2)+"次尝试！")
                i += 1

    def GetTwitterFollowers(self,username):
        while True:
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            option.add_argument('disable-gpu')
            option.add_argument('--no-sandbox')

            driver = webdriver.Chrome(chrome_options=option)

            driver.get("https://twitter.com/"+username)
            driver.implicitly_wait(20)

            followers = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span')
            followersCountText=followers.text
            #followersCountText="6,998" 
            followersCount=self.RemoveFormat(followersCountText)
            followersCountChange=self.CalcCountChange(followersCount)
            print(followersCountText)

            self.dbService.addTwitterFollowers(username,followersCount,followersCountText,followersCountChange)
            try:
                remote=""
                self.requestDeal(remote+"/add?username="+username+"&followersCount="+followersCount+"&followersCountText"+followersCountText+"&followersCountChange="+followersCountChange)
            except Exception as error:
                pass

            print('一个小时后，再次抓取~')
            time.sleep(1*3600*1) #一个小时

#主模块执行
if __name__ == "__main__":
    RTK = TwitterFollowers()
    sys.exit()