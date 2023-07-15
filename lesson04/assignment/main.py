import logging
from utils.custom_formatter import CustomFormatter
from utils.config import set_logger
from exercise import ex_01_02, ex_03, ex_04, ex_05, ex_06, ex_07, ex_08, ex_09, ex_10, ex_11
import datetime


def init_main_logger():
    logger = logging.getLogger("lesson_4.exercise")
    logger.setLevel(logging.DEBUG)
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    ch = logging.StreamHandler()
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)

    set_logger(logger)


init_main_logger()
ex_01_02()
ex_03()
ex_04()
ex_05()
ex_06()
ex_07()
ex_08()
ex_09()
ex_10()
ex_11()
