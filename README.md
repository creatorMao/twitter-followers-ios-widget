# twitter-followers-ios-widget

![example](./Images/QQ图片20220409000919.png)

# 环境

- 能访问twitter网站
- 一个安装了chromedriver的
    [docker环境 docker-python-chromedriver](https://github.com/kmmiles/docker-python-chromedriver)
- pip3 install selenium
- pip3 install requests
- pip3 install flask
- pip3 install flask-cors

# 使用

## 1.1 设置抓取用户id
修改/server.py文件
```
self.GetTwitterFollowers("")
```

## 1.2 启动抓取主服务
```
python3 server.py
```

## 1.3 启动获取最新关注接口
```
cd web
python3 server.py
```

~~~
curl http://xxxx:9855/twitter/followers/latest


{
    "USER_NAME": "", 
    "FOLLOWERS_COUNT": "6976", 
    "FOLLOWERS_COUNT_TEXT": "6,976", 
    "FOLLOWERS_COUNT_CHANGE": "-24", 
    "IMP_DATE": "2022-04-09", 
    "IMP_TIME": "2022-04-09 14:37:14"
}
~~~