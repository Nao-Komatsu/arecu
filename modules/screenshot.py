# -*- coding: utf-8 -*-

import modules
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

# Logging
logger = getLogger('arecu').getChild('screenshot')

# Output help message
def main(args):

    # Logging
    if (args.verbose):
        level = 'DEBUG'
    else:
        level = 'INFO'
    modules.log.config(level)

    path = '/sdcard/Download/ss.png'
    device = args.device

    logger.debug('Take a screenshot...')
    modules.function.call_subprocess(['adb', '-s', device, 'shell', 'screencap', '-p', path], level)

    logger.debug('Download screenshot...')
    modules.function.call_subprocess(['adb', '-s', device, 'pull', path], level)

    logger.debug('Delete temporary screenshot in a device...')
    modules.function.call_subprocess(['adb', '-s', device, 'shell', 'rm', path], level)
