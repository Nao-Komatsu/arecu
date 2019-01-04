#!/bin/bash

DIR=`pwd`

echo -e "--- Install Arecu ---"

echo -e "sed -i -e \"s;<INIFILE>;$DIR/config.ini;g\" $DIR/modules/decompile.py"
sed -i -e "s;<INIFILE>;$DIR/config.ini;g" $DIR/modules/decompile.py

sudo rm -fv /usr/local/bin/arecu
sudo rm -fv /usr/local/bin/arecu_dir
sudo ln -sfv $DIR/arecu.py /usr/local/bin/arecu
sudo ln -sfv $DIR /usr/local/bin/arecu_dir

exit 0
