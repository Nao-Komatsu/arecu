#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Arecu - Android Application Reverse Engineering Commandline Utility

Arecu is reverse engineering tool fot Android applications.

- Unzip the apk file
- Decompile the apk file using JavaDecompiler
- Decompile the apk file using Procyon Decompiler
- Decode the apk file using Apktool

'''

from logging import getLogger, StreamHandler, DEBUG, INFO
import argparse
import os
import shutil
import zipfile
import modules
import sys
import subprocess

VERSION = '1.3.1'

##### Make Parser #####

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

# Logging
if (args.verbose):
    level = 'DEBUG'
else:
    level = 'INFO'

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(level)
logger.setLevel(level)
logger.addHandler(handler)
logger.propagate = False


##### Main Process #####

def main():

    # Initialization
    logger.debug('\n--- Initialization ---')
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
    if (args.jdcmd or args.procyon or args.unzip):

        logger.debug('Create directory \'{}\''.format(TMP_DIR))
        os.makedirs(TMP_DIR, exist_ok = True)

        # Unzip
        logger.debug('\n--- Unzip apk file ---')
        logger.debug('Unzip \'{}\' to \'{}\''.format(apk, TMP_DIR))
        with zipfile.ZipFile(apk) as existing_zip:
            existing_zip.extractall(TMP_DIR)
        logger.debug('Unzip finished')

        if (args.unzip):
            logger.debug('Copy \'{}\' to \'{}_unzip\''.format(TMP_DIR, outdir))
            shutil.copytree(TMP_DIR, outdir + '_unzip')

        # Dex to Jar
        if (args.jdcmd or args.procyon):
            logger.debug('\n--- Convert Dex to Jar ---')
            subprocess.run(
                    [TOOLS_PATH + '/dex2jar/d2j-dex2jar.sh', TMP_DIR + '/classes.dex',
                        '-o', TMP_DIR + '/classes.jar', '-d'])
            logger.debug('Convert finished')

            # JavaDecompiler
            if (args.jdcmd):
                logger.debug('\n--- Decompile using JavaDecompiler ---')
                subprocess.run(
                        [TOOLS_PATH + '/jd-cmd/jd-cli', '-od', outdir + '_jdcmd',
                            TMP_DIR + '/classes.jar', '-g', 'DEBUG'])
                logger.debug('Decompile finished')

            # Procyon Decompiler
            if (args.procyon):
                logger.debug('\n--- Decompile using Procyon Decompiler ---')
                subprocess.run(
                        ['java', '-jar', TOOLS_PATH + '/procyon/procyon.jar',
                            '-jar', TMP_DIR + '/classes.jar',
                            '-o', outdir + '_procyon' '-v', '3'])
                logger.debug('Decompile finished')

        logger.debug('\n--- Clean up ---')
        logger.debug('Remove directory \'{}\''.format(TMP_DIR))
        shutil.rmtree(TMP_DIR)

    # Decode
    if (args.apktool):
        logger.debug('\n--- Decode using Apktool ---')
        subprocess.run(
                ['apktool', 'decode', apk, '-o', outdir + '_apktool'])
        logger.debug('Decode finished')

    logger.debug('\nSuccess!')

if __name__ == '__main__':
    main()
