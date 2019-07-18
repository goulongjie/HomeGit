import logging
from datetime import datetime
import threading
import os


class Log(object):
    def __init__(self):
        # get the parent directory
        self.proDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # join directory
        self.logDir = os.path.join(self.proDir,"Log")
        # join filename
        self.log=os.path.join(self.logDir,str(datetime.now().strftime("%Y-%m-%d %H:%m")))
        # create result file if it doesn't exist
        if not os.path.exists(self.logDir):
            os.mkdir(self.logDir)

        # defined logger
        self.infoLogger = logging.getLogger()
        # defined Log level :
        self.infoLogger.setLevel(logging.INFO)
        # defined filelogger
        self.fileLogger = logging.getLogger()
        self.fileLogger.setLevel(logging.INFO)

        # defined StreamHandler
        sh = logging.StreamHandler()
        # defined FileHandler
        fh = logging.FileHandler(self.log,encoding="utf-8")

        # defined formatter
        self.fmt = "%(asctime)s - %(name)s - %(levelname)s | %(message)s"
        #defined formatter
        formatter = logging.Formatter(fmt=self.fmt)
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        # add handler
        self.infoLogger.addHandler(sh)
        self.fileLogger.addHandler(fh)

    def build_start_line(self, case_no):
        """
        write start line
        :return:
        """
        self.infoLogger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """
        write end line
        :return:
        """
        self.infoLogger.info("--------" + case_no + " END--------")

    def info(self,msg):
        self.infoLogger.info(f"message :: {msg}")


if __name__=="__main__":
    # aa = Log().build_start_line("sssss")
    Log().info("hahaha")