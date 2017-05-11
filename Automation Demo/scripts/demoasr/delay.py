#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals, with_statement
import time
import sys

def backspace(n):
    # print((b'\x08' * n).decode(), end='') # use \x08 char to go back
    print('\r' * n, end='')                 # use '\r' to go back

def delay(long):
    print('This is going to take %s mins' % (int(long*100/60)))
    for i in range(101):                        # for 0 to 100
        s = str(i) + '%'                        # string for output
        print(s, end='')                        # just print and flush
        sys.stdout.flush()                    # needed for flush when using \x08
        backspace(len(s))                       # back for n chars
        time.sleep(long)                         # sleep for provided number of Sec
    return
	
def main():
	delay(2)

if __name__ == "__main__":
    main()
