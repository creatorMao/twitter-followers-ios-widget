import sys
import time
import DBService
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

    def GetTwitterFollowers(self,username):
        while True:
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            option.add_argument('–disable-gpu')
            driver = webdriver.Chrome(chrome_options=option)

            driver.get("https://twitter.com/"+username)
            followers = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span')
            followersCountText=followers.text
            #followersCountText="6,998" 
            followersCount=self.RemoveFormat(followersCountText)
            followersCountChange=self.CalcCountChange(followersCount)
            print(followersCountText)

            self.dbService.addTwitterFollowers(username,followersCount,followersCountText,followersCountChange)
            
            time.sleep(1*3600*1) #一个小时

#主模块执行
if __name__ == "__main__":
    RTK = TwitterFollowers()
    sys.exit()