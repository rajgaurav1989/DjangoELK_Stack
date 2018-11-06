import logging
from logging import StreamHandler
import logstash
import sys

def getLogger() :
    logger = logging.getLogger('python-logstash-logger')
    logger.setLevel(logging.INFO)
    logger.addHandler(logstash.TCPLogstashHandler("localhost", 5959, version=1))
    logger.addHandler(StreamHandler())
    return logger