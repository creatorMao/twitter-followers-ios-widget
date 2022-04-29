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
                                    FOLLOWERS_COUNT_TEXT VARCHAR(500),\
                                    FOLLOWERS_COUNT_CHANGE VARCHAR(500),\
                                    IMP_DATE VARCHAR(10) DEFAULT (date('now')),\
                                    IMP_TIME VARCHAR(19) DEFAULT (datetime('now','localtime'))\
                        )")
        pass

    def addTwitterFollowers(self, username,followersCount,followersCountText,followersCountChange):
        self.db.execute("INSERT INTO T_TWITTER_FOLLOWERS_HISTORY(USER_NAME,FOLLOWERS_COUNT,FOLLOWERS_COUNT_TEXT,FOLLOWERS_COUNT_CHANGE) VALUES(?,?,?,?)",(username,followersCount,followersCountText,followersCountChange))

    def getLatestFollowers(self):
        result=self.db.query("SELECT * FROM T_TWITTER_FOLLOWERS_HISTORY ORDER BY IMP_TIME DESC LIMIT 1")
        res={}
        for row in result:
            res= {
                'USER_NAME':row[0],
                'FOLLOWERS_COUNT':row[1],
                'FOLLOWERS_COUNT_TEXT':row[2],
                'FOLLOWERS_COUNT_CHANGE':row[3],
                'IMP_DATE':row[4],
                'IMP_TIME':row[5],
            }
        return res

    def getFollowerChange(self,baseDate):
        result=self.db.query("SELECT SUM(FOLLOWERS_COUNT_CHANGE),MAX(IMP_TIME),MAX(FOLLOWERS_COUNT),MAX(FOLLOWERS_COUNT_TEXT) FROM T_TWITTER_FOLLOWERS_HISTORY WHERE IMP_DATE=?",(baseDate,))
        res={}
        for row in result:
            res= {
                'FOLLOWERS_COUNT_CHANGE':row[0],
                'IMP_TIME':row[1],
                'FOLLOWERS_COUNT':row[2],
                'FOLLOWERS_COUNT_TEXT':row[3]
            }
        return res