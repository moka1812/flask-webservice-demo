#!flask/bin/python
from flask import Flask

app = Flask(__name__)

from flask import request
from utils.getHeaderInfo import getHeaderInfo
from logging.handlers import RotatingFileHandler
from time import strftime

@app.route('/')
def index():
    headerInfo = getHeaderInfo(request)
    print(headerInfo)
    return headerInfo, 200

if __name__ == '__main__':
    import logging
    logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
    logging.basicConfig(format = logFormatStr, filename = "global.log", level=logging.DEBUG)
    formatter = logging.Formatter(logFormatStr,'%m-%d %H:%M:%S')
    fileHandler = logging.FileHandler("summary.log")
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)
    streamHandler.setFormatter(formatter)
    app.logger.addHandler(streamHandler)
    app.logger.info("Logging is set up.")
    app.run(host='0.0.0.0',debug=True)
