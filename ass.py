#!/home/nao/.pyenv/shims/python

import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(
        prog='ass.py',
        usage='ass.py [options...]',
        description='Command line Android Screenshot using Android Debug Bridge (adb command)',
        epilog='This program is developed by Nao Komatsu.',
        add_help=True,
        )

parser.add_argument('-o', '--out',
        help='Output file name (default: ss.png)',
        default='ss.png',
        )

parser.add_argument('-v', '--version',
        version='%(prog)s 1.0.0',
        action='version',
        default=False
        )

def main():
    args = parser.parse_args()
    path = "/storage/emulated/0/Download/" + args.out
    print("Get screenshot...")
    res = subprocess.run(["adb", "shell", "screencap", "-p", path], stdout=subprocess.PIPE)
    sys.stdout.buffer.write(res.stdout)
    print("Download screenshot...")
    res = subprocess.run(["adb", "pull", path], stdout=subprocess.PIPE)
    sys.stdout.buffer.write(res.stdout)
    res = subprocess.run(["adb", "shell", "rm", path], stdout=subprocess.PIPE)
    sys.stdout.buffer.write(res.stdout)

if __name__ == '__main__':
    main()
