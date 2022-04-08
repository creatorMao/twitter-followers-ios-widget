import os
import uuid
from Common import SQLiteHelper

class DBService():

    def __init__(self):
        self.initDBConnect()
        self.initTable()

    def initDBConnect(self):
        self.db = SQLiteHelper.SQLiteHelper(os.path.abspath(
            os.path.dirname(__file__))+"/DB/DB.db")
        pass

    def initTable(self):
        self.db.execute("CREATE TABLE IF NOT EXISTS T_TWITTER_FOLLOWERS_HISTORY(\
                                    USER_NAME VARCHAR(500),\
                                    FOLLOWERS_COUNT VARCHAR(500),\
                                    IMP_DATE VARCHAR(10) DEFAULT (date('now')),\
                                    IMP_TIME VARCHAR(19) DEFAULT (datetime('now','localtime'))\
                        )")
        pass

    def addTwitterFollowers(self, userId,followers):
        self.db.execute("INSERT INTO T_TWITTER_FOLLOWERS_HISTORY(USER_NAME,FOLLOWERS_COUNT) VALUES(?,?)",(userId,followers))

    def getFollowers(self):
        result=self.db.query("SELECT * FROM T_TWITTER_FOLLOWERS_HISTORY ORDER BY IMP_TIME DESC LIMIT 1")
        res={}
        for row in result:
            res= {
                'USER_NAME':row[0],
                'FOLLOWERS_COUNT':row[1],
                'IMP_DATE':row[2],
                'IMP_TIME':row[3],
            }
        return res