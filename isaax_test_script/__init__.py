# coding: utf-8

import sys
import os
import datetime
import time
from uuid import getnode

def daemon():
    sys.stdout.write("Arguments {0}\n".format(' '.join(sys.argv)))
    sys.stdout.write("--- environs:\r\n")
    for e in os.environ.items():
        sys.stdout.write("{0}: {1}\r\n".format(*e))

    sys.stdout.write("--- done.\r\n")

    while True:
        sys.stdout.write(datetime.datetime.now().isoformat())
        sys.stdout.write("\r\n")
        time.sleep(3)

def command():
    sys.stdout.write("HELLO !\n")
    sys.stdout.write("time {0}\n".format(datetime.datetime.now().isoformat()))
    sys.stdout.write("mac {0}\n".format(getMyMac()))
    sys.stdout.write("Version {0}\n".format(getCurrentVersion()))
    sys.stdout.write("Arguments {0}\n".format(' '.join(sys.argv)))
    sys.stdout.write("CurrentPath {0}\n".format(os.path.realpath('')))
    sys.stdout.write("FilePath {0}\n".format(os.path.realpath(__file__)))
    sys.stdout.write("ResourceCodeA {0}\n".format(getResourceCode('a')))

    sys.stdout.write("EOS\n")

def getMyMac():
    from uuid import getnode
    node = getnode()
    return ':'.join([hex(node >> i & 0xff)[2:] for i in reversed(range(0, 48, 8))])

def getCurrentVersion():
    return "abcde"

def getResourceCode(name):
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources', name)
    with open(filename, 'r') as f:
        return f.read()
