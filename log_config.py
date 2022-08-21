import logging
import uvicorn


# create logger
def init_loggers():
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = uvicorn.logging.DefaultFormatter("%(levelprefix)s %(asctime)s | %(message)s")
    # formatter = logging.Formatter("%(levelname)-8s  %(message)s - %(asctime)s")

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger

# logger = init_loggers()

# logger.debug('Debug message')
# logger.info('Info message')
# logger.warning('Warn message')
# logger.error('Error message')
# logger.critical('Critical message')