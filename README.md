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

### Apk file decompile

- Using JavaDecompiler

```
$ arecu -j base.apk
Target apk: base.apk
basename: base.apk
name: base
ext: .apk
outdir: ./base
--- Make temprary directory ---
/tmp/arecu_tmp
--- Unzip apk file ---
--- Dex to Jar ---
dex2jar /tmp/arecu_tmp/classes.dex -> /tmp/arecu_tmp/classes.jar
--- JavaDecompiler ---
18:24:50.349 INFO  jd.cli.Main - Decompiling /tmp/arecu_tmp/classes.jar
18:24:50.354 INFO  jd.core.output.DirOutput - Directory output will be initialized for path ./base_jdcmd
Undefined type catch
18:24:50.992 INFO  jd.core.output.DirOutput - Finished with 8 class file(s) and 0 resource file(s) written.
--- Remove temporary directory ---
/tmp/arecu_tmp
```

- Using Procyon Decompiler

```
$ arecu -p base.apk
Target apk: base.apk
basename: base.apk
name: base
ext: .apk
outdir: ./base
--- Make temprary directory ---
/tmp/arecu_tmp
--- Unzip apk file ---
--- Dex to Jar ---
dex2jar /tmp/arecu_tmp/classes.dex -> /tmp/arecu_tmp/classes.jar
--- Procyon / Java Decompiler ---

...

Decompiling com/test/util/Configuration...

...

--- Remove temporary directory ---
/tmp/arecu_tmp
```
