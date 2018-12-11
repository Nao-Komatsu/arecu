# Arecu

Android Application Reverse Engineering Commandline Utility

## Description

Arecu is reverse engineering tool fot Android applications.

### What works?

- Unzip the apk file
- Decompile the apk file using JavaDecompiler
- Decompile the apk file using Procyon Decompiler
- Decode the apk file using Apktool

## Installation

### Prerequisites

My scripts were tested on Ubuntu16.04.

1. [Python3.6](https://www.python.org/downloads/)

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

### Installing

```
cd ~
git clone https://github.com/nsecdevs/arecu.git
cd arecu/
./install.sh
```

## Usage

### Unzip

```
$ arecu -u base.apk
```

### Decompile

- Using JavaDecompiler

```
$ arecu -j base.apk
```

- Using Procyon Decompiler

```
$ arecu -p base.apk
```
