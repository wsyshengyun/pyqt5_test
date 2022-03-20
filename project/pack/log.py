# coding:utf8


import logging


path_log = "log/log.log"
level = logging.INFO
logging.basicConfig(level=level
        , format= '%(asctime)s - %(name)s - %(levelname)s : %(message)s'
        , filename= path_log
        , datefmt= '%Y/%m/%d %H:%M:%S'
         )
logger = logging.getLogger(__name__)


# def getLogger():
#     return logger