logger = 0
os = 0

def set_logger(lgr):
    global logger
    logger = lgr
    
    # logger.debug("debug message")
    # logger.info("info message")
    # logger.warning("warning message")
    # logger.error("error message")
    # logger.critical("critical message")
    
    

def get_logger():
    return logger

def set_os(o):
    global os
    os = o

def get_os():
    return os

