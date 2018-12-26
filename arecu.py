#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Arecu - Android Application Reverse Engineering Commandline Utility

Arecu is reverse engineering tool fot Android applications.

- Unzip the apk file
- Decompile the apk file using JavaDecompiler
- Decompile the apk file using Procyon Decompiler
- Decode the apk file using Apktool

'''

import argparse
import configparser
import modules
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

VERSION = '1.6.1'


##### Make Parser #####

parser = argparse.ArgumentParser(
        prog = 'Arecu',
        usage = 'arecu [options...] <apk_file>',
        description = '%(prog)s is reverse engineering tool for apk.',
        epilog = 'Copyright (C) 2018 Nao Komatsu',
        add_help = True)

parser.add_argument('apk_file',
        help = 'Target apk file.')

parser.add_argument('-A', '--all',
        help = 'Unzip, Decompile and Decode with one option.',
        action = 'store_true',
        default = False)

parser.add_argument('-u', '--unzip',
        help = 'Unzip the apk file.',
        action = 'store_true',
        default = False)

parser.add_argument('-j', '--jdcmd',
        help = 'Decompile the apk file using JavaDecompiler.',
        action = 'store_true',
        default = False)

parser.add_argument('-p', '--procyon',
        help = 'Decompile the apk file using Procyon Decompiler.',
        action = 'store_true',
        default = False)

parser.add_argument('-a', '--apktool',
        help = 'Decode the apk file using Apktool.',
        action = 'store_true',
        default = False)

parser.add_argument('-o', '--outdir',
        help = 'The name of directory that gets written. Default is current directory.',
        type = str,
        default = '.')

parser.add_argument('-v', '--verbose',
        help = 'Increase verbosity level.',
        action = 'store_true',
        default = False)

parser.add_argument('--version',
        version = '%(prog)s version ' + VERSION,
        action = 'version',
        default = False)


##### Configuration #####

# Argument Analysis
args = parser.parse_args()

# Logging
if (args.verbose):
    level = 'DEBUG'
else:
    level = 'INFO'

logger = getLogger('arecu')
modules.log.config(level)


##### Main Process #####

def main():
    modules.decompile.main(args, level)


if __name__ == '__main__':
    main()
