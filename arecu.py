#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Arecu - Android Application Reverse Engineering Commandline Utility

Arecu is reverse engineering tool fot Android applications.

- Unzip the apk file
- Decompile the apk file using JavaDecompiler
- Decompile the apk file using Procyon Decompiler
- Decode the apk file using Apktool

'''

from logging import getLogger, StreamHandler, DEBUG
import argparse
import os
import shutil
import zipfile
import modules
import sys
import subprocess

### Configuration ###
TMP_DIR = '/tmp/arecu_tmp'
TOOLS_PATH = '/usr/local/bin/arecu_dir'
VERSION = '1.2.0'

### Make Parser ###
parser = argparse.ArgumentParser(
        prog = 'Arecu',
        usage = 'arecu [options...] <apk_file>',
        description = 'Arecu is reverse engineering tool for apk.',
        epilog = 'Copyright (C) 2018 Nao Komatsu',
        add_help = True)

parser.add_argument('apk_file',
        help = 'Target apk file.')

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

parser.add_argument('--version',
        version = '%(prog)s version ' + VERSION,
        action = 'version',
        default = False)

### Logging Configuration ###
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

def main():
    # Analysis argument
    args = parser.parse_args()
    apk = args.apk_file
    basename = os.path.basename(apk)
    name, ext = os.path.splitext(basename)
    outdir = args.outdir + '/' + name

    # Decompile
    if (args.jdcmd or args.procyon or args.unzip):

        # Initialization
        logger.debug('\n--- Initialization ---')

        if (os.path.exists(TMP_DIR)):
            logger.debug('Remove ' + TMP_DIR)
            shutil.rmtree(TMP_DIR)

        logger.debug('Make ' + TMP_DIR)
        os.makedirs(TMP_DIR, exist_ok = True)

        # Unzip
        logger.debug('\n--- Unzip apk file ---')
        with zipfile.ZipFile(apk) as existing_zip:
            existing_zip.extractall(TMP_DIR)

        if (args.unzip):
            logger.debug('Copy ' + TMP_DIR + ' to ' + outdir + '_unzip')
            shutil.copytree(TMP_DIR, outdir + '_unzip')

        # Dex to Jar
        if (args.jdcmd or args.procyon):
            logger.debug('\n--- Convert Dex to Jar ---')
            subprocess.run([TOOLS_PATH + '/dex2jar/d2j-dex2jar.sh',
                TMP_DIR + '/classes.dex',
                '-o', TMP_DIR + '/classes.jar'])

            # JavaDecompiler
            if (args.jdcmd):
                logger.debug('\n--- Decompile using JavaDecompiler ---')
                subprocess.run([TOOLS_PATH + '/jd-cmd/jd-cli', '-od',
                    outdir + '_jdcmd',
                    TMP_DIR + '/classes.jar'])

            # Procyon Decompiler
            if (args.procyon):
                logger.debug('\n--- Decompile using Procyon Decompiler ---')
                subprocess.run(['java',
                    '-jar', TOOLS_PATH + '/procyon/procyon.jar',
                    '-jar', TMP_DIR + '/classes.jar',
                    '-o', outdir + '_procyon'])

        logger.debug('\n--- Clean up ---')
        logger.debug('Remove ' + TMP_DIR)
        shutil.rmtree(TMP_DIR)

    # Decode
    if (args.apktool):
        logger.debug('\n--- Decode using Apktool ---')
        subprocess.run(['apktool',
            'decode', apk,
            '-o', outdir + '_apktool'])

if __name__ == '__main__':
    main()
