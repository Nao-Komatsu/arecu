#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Arecu - Android Application Reverse Engineering Commandline Utility

Arecu is reverse engineering tool fot Android applications.

- Unzip the apk file
- Decompile the apk file using JavaDecompiler
- Decompile the apk file using Procyon Decompiler
- Decode the apk file using Apktool

'''

from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO
import argparse
import os
import shutil
import zipfile
import modules
import sys
import subprocess

VERSION = '1.5.1'

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

# Global Variables
TMP_DIR = '/tmp/arecu_tmp'
TOOLS_PATH = '/usr/local/bin/arecu_dir'

# Argument Analysis
args = parser.parse_args()

if (args.all):
    unzip = True
    jdcmd = True
    procyon = True
    apktool = True
else:
    unzip = args.unzip
    jdcmd = args.jdcmd
    procyon = args.procyon
    apktool = args.apktool

# Logging
if (args.verbose):
    level = 'DEBUG'
else:
    level = 'INFO'

logger = getLogger('arecu')
handler = StreamHandler()
handler.setLevel(level)
logger.setLevel(level)
logger.addHandler(handler)
logger.propagate = False
format = Formatter('%(levelname)s\t%(name)s\t%(message)s')
handler.setFormatter(format)


##### Function Definition #####

def call_subprocess(cmd):
    '''call_subprocess function

    Execution subprocess and Output branching by log level.

    Args:
        cmd (list): Command to be executed

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


##### Main Process #####

def main():

    # Initialization
    logger.debug('--- Initialization ---')
    apk = args.apk_file
    basename = os.path.basename(apk)
    logger.debug('Target apk file is \'{}\''.format(basename))
    name, ext = os.path.splitext(basename)
    outdir = os.path.join(args.outdir, name)
    logger.debug('Output directory is \'{}\''.format(args.outdir))

    if (os.path.exists(TMP_DIR)):
        logger.debug('Remove directory \'{}\''.format(TMP_DIR))
        shutil.rmtree(TMP_DIR)

    # Decompile
    if (jdcmd or procyon or unzip):

        logger.debug('Create directory \'{}\''.format(TMP_DIR))
        os.makedirs(TMP_DIR, exist_ok = True)

        # Unzip
        logger.info('--- Unzip apk file ---')
        logger.debug('Unzip \'{}\' to \'{}\''.format(apk, TMP_DIR))
        with zipfile.ZipFile(apk) as existing_zip:
            existing_zip.extractall(TMP_DIR)

        if (unzip):
            logger.debug('Copy \'{}\' to \'{}_unzip\''.format(TMP_DIR, outdir))
            shutil.copytree(TMP_DIR, outdir + '_unzip')

        # Dex to Jar
        if (jdcmd or procyon):
            logger.info('--- Convert Dex to Jar ---')
            call_subprocess([TOOLS_PATH + '/dex2jar/d2j-dex2jar.sh',
                TMP_DIR + '/classes.dex', '-o', TMP_DIR + '/classes.jar'])

            # JavaDecompiler
            if (jdcmd):
                logger.info('--- Decompile using JavaDecompiler ---')
                call_subprocess([TOOLS_PATH + '/jd-cmd/jd-cli',
                    '-od', outdir + '_jdcmd', TMP_DIR + '/classes.jar'])

            # Procyon Decompiler
            if (procyon):
                logger.info('--- Decompile using Procyon Decompiler ---')
                call_subprocess(['java', '-jar', TOOLS_PATH + '/procyon/procyon.jar',
                    '-jar', TMP_DIR + '/classes.jar', '-o', outdir + '_procyon'])

        logger.debug('--- Clean up ---')
        logger.debug('Remove directory \'{}\''.format(TMP_DIR))
        shutil.rmtree(TMP_DIR)

    # Decode
    if (apktool):
        logger.info('--- Decode using Apktool ---')
        call_subprocess(['apktool', 'decode', apk, '-o', outdir + '_apktool'])

    logger.info('Done!')


if __name__ == '__main__':
    main()
