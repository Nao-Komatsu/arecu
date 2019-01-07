# -*- coding: utf-8 -*-

import configparser
import modules
import os
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

logger = getLogger('arecu').getChild('screenshot')

# Configuration
inifile = '<INIFILE>'
config = configparser.ConfigParser()
config.read(inifile, 'UTF-8')
name = config.get('screenshot', 'file_name')
tmp_dir = config.get('screenshot', 'tmp_dir')

# Output help message
def main(args):

    # Logging
    if (args.verbose):
        level = 'DEBUG'
    else:
        level = 'INFO'
    modules.log.config(level)

    global name
    if (args.name):
        name = args.name

    image = name + '.png'
    path = os.path.join(tmp_dir, image)
    device = args.device
    outdir = os.path.join(args.outdir, image)

    logger.debug('Take a screenshot...')
    modules.function.call_subprocess(['adb', '-s', device, 'shell', 'screencap', '-p', path], level)

    logger.debug('Download screenshot...')
    modules.function.call_subprocess(['adb', '-s', device, 'pull', path, outdir], level)
    logger.debug('Saved \'{}\''.format(outdir))

    logger.debug('Delete temporary screenshot in a device...')
    modules.function.call_subprocess(['adb', '-s', device, 'shell', 'rm', path], level)
