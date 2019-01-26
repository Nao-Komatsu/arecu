# -*- coding: utf-8 -*-

from logging import getLogger, StreamHandler, Formatter

logger = getLogger('arecu').getChild('log')


def config(level):

    # logger
    logger.parent.setLevel(level)

    # handler
    handler = StreamHandler()
    handler.setLevel(level)
    format = Formatter('%(levelname)s\t%(name)s\t%(message)s')
    handler.setFormatter(format)

    # Set handler to logger
    logger.parent.addHandler(handler)

    logger.debug('Log conf setting')
