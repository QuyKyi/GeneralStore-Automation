import logging
import time
from Consts.consts import Consts
from colorlog import ColoredFormatter
class Logger:

    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        curr_time = time.strftime("%Y-%m-%d")
        self.LogFileName = Consts.LOG_FILE + curr_time + '.txt'
        print(self.LogFileName)
        # "a" to append the logs in same file, "w" to generate new logs and delete old one
        fh = logging.FileHandler(self.LogFileName, mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)

log = Logger(__name__,logging.INFO)
log.logger.info("Design by: ABC")