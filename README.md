# twitter-followers-ios-widget

![example](./Images/QQ图片20220409153253.jpg)

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
修改/conf.ini文件
```
[user]
userName = xxx
```

## 1.2 启动抓取主服务
```
python3 server.py
```

## 1.3 启动获取最新关注数量接口
```
cd web
python3 server.py
```

~~~
curl http://xxxx:9855/twitter/followers/latest



{
    "USER_NAME": "", 
    "FOLLOWERS_COUNT": "7358", 
    "FOLLOWERS_COUNT_TEXT": "7,358", 
    "FOLLOWERS_COUNT_CHANGE": "1", 
    "IMP_DATE": "2022-04-30", 
    "IMP_TIME": "2022-04-30 02:55:25", 
    "FOLLOWERS_COUNT_CHANGE_TODAY": 4 
}
~~~

## 1.4 修改小组件代码
将twitter-followers.js中代码复制到scriptsable应用中，并修改请求地址

~~~
async getData() {
    let api = "http://xxxx" + '/twitter/followers/latest'
    let req = new Request(api)
    let res = await req.loadJSON()
    //console.log(res)
    return res
    }
~~~
