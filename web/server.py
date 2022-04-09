from flask import Flask,request
from flask import render_template
import os,json
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from DBService import DBService
from flask_cors import CORS

app=Flask(__name__)
CORS(app, resources=r'/*')
@app.route('/')
def index(name=None):
    return render_template('index.html')

@app.route('/twitter/followers/latest',methods=['GET'])
def getFollowers():
    result=DBService().getFollowers()
    return json.dumps(result)

if __name__=='__main__':
    app.run('0.0.0.0',9855,debug=False)