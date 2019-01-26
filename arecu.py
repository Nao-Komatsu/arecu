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
import modules
from logging import getLogger

VERSION = '2.4.0'


# ----- Make parser -----

# Top-level parser
parser = argparse.ArgumentParser(
        prog='Arecu',
        usage='arecu {subcommand} [options...] <target>',
        description='%(prog)s is reverse engineering tool for apk.',
        epilog='Copyright (C) 2018 - 2019 Nao Komatsu',
        add_help=True)

parser.add_argument(
        '--version',
        version='%(prog)s version ' + VERSION,
        action='version',
        default=False)

parser.set_defaults(func=modules.function.print_help)

# Sub-commands parser
subparsers = parser.add_subparsers(
        title='subcommands',
        prog='arecu',
        help='For more detailed help add --help')

# "dec" command parser
parser_dec = subparsers.add_parser(
        'dec',
        aliases=['decompile'],
        help='Decompile & Decode the apk file')

parser_dec.add_argument(
        'apk_file',
        help='Target apk file')

parser_dec.add_argument(
        '-A', '--all',
        help='Unzip, Decompile and Decode with one option',
        action='store_true',
        default=False)

parser_dec.add_argument(
        '-u', '--unzip',
        help='Unzip the apk file',
        action='store_true',
        default=False)

parser_dec.add_argument(
        '-j', '--jdcmd',
        help='Decompile the apk file using JavaDecompiler',
        action='store_true',
        default=False)

parser_dec.add_argument(
        '-p', '--procyon',
        help='Decompile the apk file using Procyon Decompiler',
        action='store_true',
        default=False)

parser_dec.add_argument(
        '-a', '--apktool',
        help='Decode the apk file using Apktool',
        action='store_true',
        default=False)

parser_dec.add_argument(
        '-o', '--outdir',
        help='The name of directory that gets written',
        type=str,
        default='.')

parser_dec.add_argument(
        '-v', '--verbose',
        help='Increase verbosity level',
        action='store_true',
        default=False)

parser_dec.set_defaults(func=modules.decompile.main)

# "ss" command parser
parser_ss = subparsers.add_parser(
        'ss',
        aliases=['screenshot'],
        help='Take a screenshot of a device')

parser_ss.add_argument(
        'device',
        help='Target device')

parser_ss.add_argument(
        '-o', '--outdir',
        help='The name of directory that gets written',
        type=str,
        default='.')

parser_ss.add_argument(
        '-n', '--name',
        help='File name excluding extensions to be saved',
        type=str)

parser_ss.add_argument(
        '-i', '--increment',
        help='Increment by adding a number to file name',
        action='store_true',
        default=False)

parser_ss.add_argument(
        '-v', '--verbose',
        help='Increase verbosity level',
        action='store_true',
        default=False)

parser_ss.set_defaults(func=modules.screenshot.main)


# ----- Main process -----

# Logging
logger = getLogger('arecu')

# Argument analysis
args = parser.parse_args()

# To sub process
args.func(args)
