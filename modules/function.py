# -*- coding: utf-8 -*-

import subprocess
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

logger = getLogger('arecu').getChild('function')


##### Function Definition #####

# Output help message
def print_help(args):
    print('usage: arecu {subcommand} [options...] <target>\n')
    print('Show more detailed help:')
    print('\tarecu --help')

# Call subprocess
def call_subprocess(cmd, level):
    '''call_subprocess function

    Execution subprocess and Output branching by log level.

    Args:
        cmd (list): Command to be executed
        level (string): Log level

    Returns:
        None
    '''

    if (level == 'INFO'):
        try:
            subprocess.run(cmd, stdout = subprocess.PIPE, check = True)
        except subprocess.CalledProcessError:
            logger.info('Error: {}'.format(cmd))

    else:
        try:
            subprocess.run(cmd, check = True)
        except subprocess.CalledProcessError:
            logger.info('Error: {}'.format(cmd))
