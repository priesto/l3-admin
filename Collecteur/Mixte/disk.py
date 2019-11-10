#! /usr/bin/env python

import sys

data = sys.stdin.read()
data = data.splitlines()[1].split('%')[0]

print data
