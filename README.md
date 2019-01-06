# Arecu

Android Application Reverse Engineering Commandline Utility

## Description

Arecu is reverse engineering tool fot Android applications.

### What works?

- Decompile & Decode
  - Unzip the apk file
  - Decompile the apk file using JavaDecompiler
  - Decompile the apk file using Procyon Decompiler
  - Decode the apk file using Apktool
- Screenshot
  - Take a screenshot of a device
  - Save a screenshot to your development machine

## Installation

### Prerequisites

My scripts were tested on Ubuntu16.04.

1. [Python3.6](https://www.python.org/)

	```
	$ python -V
	Python 3.6.5
	```

2. [openjdk-8-jdk](https://openjdk.java.net/)

	```
	$ sudo apt install openjdk-8-jdk
	$ java -version
	openjdk version "1.8.0_191"
	OpenJDK Runtime Environment (build 1.8.0_191-8u191-b12-0ubuntu0.16.04.1-b12)
	OpenJDK 64-Bit Server VM (build 25.191-b12, mixed mode)
	```

3. [Apktool](https://ibotpeaches.github.io/Apktool/)

	```
	$ wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool
	$ wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.3.4.jar
	$ sudo mv apktool_2.3.4.jar /usr/local/bin/apktool.jar
	$ sudo mv apktool /usr/local/bin/
	$ sudo chmod 755 /usr/local/bin/apktool*
	$ apktool --version
	2.3.3
	```

4. [Android Debug Bridge](https://developer.android.com/studio/command-line/adb)

	```
	$ sudo apt install android-tools-adb
	$ adb version
	Android Debug Bridge version 1.0.32
	```

### Installing

```
cd ~
git clone https://github.com/nsecdevs/arecu.git
cd arecu/
./install.sh
```

## Usage

### Decompile & Decode for apk file

The decompile option on Arecu can be invoked either from `dec` or `decompile` like shown below.

```
# Unzip foo.apk to foo_unzip folder
$ arecu dec -u foo.apk

# Decompile foo.apk to foo_jdcmd folder using JavaDecompiler
$ arecu decompile -j foo.apk

# Decompile foo.apk to foo_procyon folder using Procyon Decompiler and Output logs in verbose
$ arecu dec -v -p foo.apk

# Decode foo.apk to foo_apktool folder using Apktool and Output logs in verbose
$ arecu dec -v -a foo.apk

# Unzip, Decompile and Decode foo.apk to foo_unzip, foo_jdcmd, foo_procyon, foo_apktool in bar folder
$ arecu dec -A foo.apk -o bar
```

### Take a screenshot

The screenshot option on Arecu can be invoked either from `ss` or `screenshot` like shown below.

```
# Take a screenshot and save it
$ arecu ss xxx.xxx.xxx.xxx:5555

# Take a screenshot and save it bar folder
$ arecu screenshot -o bar xxx.xxx.xxx.xxx:5555

# Take a screenshot and save it and Output logs in verbose
$ arecu ss -v xxx.xxx.xxx.xxx:5555
```

## Advanced
