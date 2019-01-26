# -*- coding: utf-8 -*-

import configparser
import modules
import os
from logging import getLogger
from pathlib import Path

logger = getLogger('arecu').getChild('screenshot')


# Configuration
inifile = '<INIFILE>'
config = configparser.ConfigParser()
config.read(inifile, 'UTF-8')
name = config.get('screenshot', 'file_name')
tmp_dir = config.get('screenshot', 'tmp_dir')


# Output help message
def main(args):

    global name, len

    # Logging
    if (args.verbose):
        level = 'DEBUG'
    else:
        level = 'INFO'
    modules.log.config(level)

    if (args.name):
        name = args.name

    if (args.increment):
        outdir = Path(args.outdir)
        file_list = list(outdir.glob(name + '_[0-9][0-9][0-9].png'))
        len = len(file_list)
        current_num = str(len + 1).zfill(3)
        next_num = str(len + 2).zfill(3)
        current = name + '_' + current_num
        next = name + '_' + next_num
        logger.debug('Length: \'{}\', Current: \'{}\', Next: \'{}\''.format(
            len, current + '.png', next + '.png'))
        name = current

    path = os.path.join(tmp_dir, 'tmp.png')
    device = args.device
    image = os.path.join(args.outdir, name + '.png')

    logger.debug('Take a screenshot...')
    modules.function.call_subprocess(
            ['adb', '-s', device, 'shell', 'screencap', '-p', path], level)

    logger.debug('Download screenshot...')
    modules.function.call_subprocess(
            ['adb', '-s', device, 'pull', path, image], level)
    logger.debug('Saved \'{}\''.format(image))

    logger.debug('Delete temporary screenshot in a device...')
    modules.function.call_subprocess(
            ['adb', '-s', device, 'shell', 'rm', path], level)
