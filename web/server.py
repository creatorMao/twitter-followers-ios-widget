from flask import Flask,request
from flask import render_template
import os,json
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from DBService import DBService
from flask_cors import CORS
import datetime

app=Flask(__name__)
CORS(app, resources=r'/*')
@app.route('/')
def index(name=None):
    return render_template('index.html')

@app.route('/add',methods=['GET'])
def addDownloadHistory():
    username=request.args.get("username")
    followersCount=request.args.get("followersCount")
    followersCountText=request.args.get("followersCountText")
    followersCountChange=request.args.get("followersCountChange")

    DBService().addTwitterFollowers(username,followersCount,followersCountText,followersCountChange)
    return "ok"

@app.route('/twitter/followers/latest',methods=['GET'])
def getFollowers():
    followersInfo=DBService().getFollowers()
    
    baseDate=datetime.datetime.now().strftime('%Y-%m-%d')
    followersInfo["FOLLOWERS_COUNT_CHANGE_TODAY"]=DBService().getFollowersCountChange(baseDate)

    return json.dumps(followersInfo)

if __name__=='__main__':
    app.run('0.0.0.0',9855,debug=False)