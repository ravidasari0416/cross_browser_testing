import logging
import os

#import constants


def get_module_logger(mod_name):
    logger = logging.getLogger(mod_name)
    logger.setLevel(logging.DEBUG)

    # create a file handler
    # handler = logging.FileHandler('Test.log')
    handler = logging.FileHandler("{0}/{1}.log".format(os.path.dirname(os.path.abspath("logger_util.py")), "AutomationLogs"))  # , mode='w'
    handler.setLevel(logging.DEBUG)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s  %(name)s %(lineno)d  %(levelname)s - %(message)s')
    # formatter = logging.Formatter('{} {} {} {}'.format("asctime", "name", "levelname", "message"))
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)

    console_fh = logging.StreamHandler()
    console_fh.setFormatter(formatter)
    logger.addHandler(console_fh)           ### streams logs to console (stdout)

    return logger