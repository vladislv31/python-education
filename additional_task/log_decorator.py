import logging
import sys
import time

logger = logging.getLogger('MyLogger')
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.setFormatter(logging.Formatter(fmt='[%(asctime)s] %(message)s'))

logger.addHandler(stream_handler)


get_time = lambda: round(time.time() * 1000)


def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info('Started %s function', func.__name__)
        start_time = get_time()
        func()
        end_time = get_time()
        logger.info('Finished %s function in %d milliseconds', func.__name__, end_time - start_time)

    return wrapper


@log_decorator
def test():
    time.sleep(1)
    print('do nothing')


test()
