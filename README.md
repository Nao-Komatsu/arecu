# Arecu

Android Application Reverse Engineering Commandline Utility

## Description

Arecu is reverse engineering tool fot Android applications.

### What works?

- Decompile the apk file using JavaDecompiler
- Decompile the apk file using Procyon Decompiler
- Unzip the apk file

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
