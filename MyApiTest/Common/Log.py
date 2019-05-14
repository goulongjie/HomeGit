import logging
from datetime import datetime
import threading
import os


class Log(object):
    def __init__(self):
        self.proDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.logDir = os.path.join(self.proDir, "Log")
        self.log = os.path.join(self.logDir, str(datetime.now().strftime("%Y-%m-%d %H%M%S.log")))

        # create result file if it doesn't exist
        if not os.path.exists(self.logDir):
            os.mkdir(self.logDir)

        # defined logger
        self.logger = logging.getLogger()
        # defined log level :
        self.logger.setLevel(logging.INFO)

        # defined StreamHandler
        sh = logging.StreamHandler()
        # defined FileHandler
        fh = logging.FileHandler(self.log,encoding="utf-8")
        fh.setLevel(logging.WARNING)
        # defined formatter
        self.fmt = "%(asctime)s - %(name)s - %(levelname)s | %(message)s"
        # defined formatter
        formatter = logging.Formatter(fmt=self.fmt)
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        # add handler
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def build_start_line(self, case_no):
        """
        write start line
        :return:
        """
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """
        write end line
        :return:
        """
        self.logger.info("--------" + case_no + " END--------")

    def info(self, msg):
        self.logger.info(f"message :: {msg}")

    def debug(self, msg):
        self.logger.debug(f"message :: {msg}")

    def warning(self, msg):
        self.logger.warning(f"message :: {msg}")

    def error(self, msg):
        self.logger.error(f"message :: {msg}")
if __name__ == "__main__":
    aa = Log().build_start_line("sssss")
    Log().warning("hahaha")
