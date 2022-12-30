import datetime
import inspect
import logging

import pytest
#to generate HTML report use ("py.test --html=report.html -s")


@pytest.mark.usefixtures("setup")
class baseclass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]  #it will provide name of function which calls this class (i.e test_DEMO) in logs instead of Base_class
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger