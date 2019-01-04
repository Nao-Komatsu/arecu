# -*- coding: utf-8 -*-

from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

logger = getLogger('arecu').getChild('function')

def help(args):
    print('usage: arecu {subcommand} [options...] <target>\n')
    print('Show more detailed help:')
    print('\tarecu --help')
