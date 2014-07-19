#!/usr/bin/python
#
# This program outputs the hex values needed to update the 'local
# name' of a Jaalee iBeacon transmitter module
import os, sys

if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Usage: %s <newname> [<password>]" % (sys.argv[0], ))
    print("If password is not specified, it defaults to 0x666666 (the default password)")
    exit(0)

newname = sys.argv[1]
passwd = '0x666666'

if len(sys.argv) == 3:
    passwd = sys.argv[2]
    if not passwd.startswith('0x'):
        passwd = '0x' + passwd

newname_hex = newname.encode('hex')
while len(newname_hex) < 30:
    newname_hex += '00'

print passwd + newname_hex

