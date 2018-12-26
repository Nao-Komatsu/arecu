# -*- coding: utf-8 -*-

import configparser
import modules
import os
import shutil
import subprocess
import zipfile
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

# Logging
logger = getLogger('arecu').getChild('decompile')

# Configuration
inifile = '<INIFILE>'
config = configparser.ConfigParser()
config.read(inifile, 'UTF-8')
tmp_dir = config.get('settings', 'tmp_dir')
lib_path = config.get('settings', 'lib_path')


##### Function Definition #####

def call_subprocess(cmd, level):
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


def main(args, level):

    # Initialization
    logger.debug('--- Initialization ---')
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

    apk = args.apk_file
    basename = os.path.basename(apk)
    logger.debug('Target apk file is \'{}\''.format(basename))
    name, ext = os.path.splitext(basename)
    outdir = os.path.join(args.outdir, name)
    logger.debug('Output directory is \'{}\''.format(args.outdir))

    if (os.path.exists(tmp_dir)):
        logger.debug('Remove directory \'{}\''.format(tmp_dir))
        shutil.rmtree(tmp_dir)

    # Decompile
    if (jdcmd or procyon or unzip):

        logger.debug('Create directory \'{}\''.format(tmp_dir))
        os.makedirs(tmp_dir, exist_ok = True)

        # Unzip
        logger.info('--- Unzip apk file ---')
        logger.debug('Unzip \'{}\' to \'{}\''.format(apk, tmp_dir))
        with zipfile.ZipFile(apk) as existing_zip:
            existing_zip.extractall(tmp_dir)

        if (unzip):
            logger.debug('Copy \'{}\' to \'{}_unzip\''.format(tmp_dir, outdir))
            shutil.copytree(tmp_dir, outdir + '_unzip')

        # Dex to Jar
        if (jdcmd or procyon):
            logger.info('--- Convert Dex to Jar ---')
            call_subprocess([lib_path + '/dex2jar/d2j-dex2jar.sh',
                tmp_dir + '/classes.dex', '-o', tmp_dir + '/classes.jar'], level)

            # JavaDecompiler
            if (jdcmd):
                logger.info('--- Decompile using JavaDecompiler ---')
                call_subprocess([lib_path + '/jd-cmd/jd-cli',
                    '-od', outdir + '_jdcmd', tmp_dir + '/classes.jar'], level)

            # Procyon Decompiler
            if (procyon):
                logger.info('--- Decompile using Procyon Decompiler ---')
                call_subprocess(['java', '-jar', lib_path + '/procyon/procyon.jar',
                    '-jar', tmp_dir + '/classes.jar', '-o', outdir + '_procyon'], level)

        logger.debug('--- Clean up ---')
        logger.debug('Remove directory \'{}\''.format(tmp_dir))
        shutil.rmtree(tmp_dir)

    # Decode
    if (apktool):
        logger.info('--- Decode using Apktool ---')
        call_subprocess(['apktool', 'decode', apk, '-o', outdir + '_apktool'], level)

    logger.info('Done!')
