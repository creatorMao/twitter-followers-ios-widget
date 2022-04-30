import os
import configparser

class ConfigHelper:

    def __init__(self,configPath):
        self.config=configparser.ConfigParser()
        print(configPath)
        self.config.read(configPath, encoding="utf-8")
        pass

    def getConfig(self,section,key):
        return self.config.get(section,key)
    