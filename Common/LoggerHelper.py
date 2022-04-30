import logging, time, os

class LoggerHelper():

    def __init__(self,logPath):

        print(logPath)
        if not os.path.exists(logPath):
            print(logPath)
            os.mkdir(logPath)

        self.logname = os.path.join(logPath, "{}.log".format(time.strftime("%Y-%m-%d")))  # 日志的名称
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)