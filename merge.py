#!/usr/bin/env python3
import os
import sys
import glob
import subprocess
DEFAULT = True

print('Merging strings of turtle-extras with turtleblocks')

n = len(sys.argv)
if n == 2 or n == 3:
    if sys.argv[1] == 'turtlebots':
        print('Using TurtleBots-style paths')
        DEFAULT = False
        path = os.path.join(
                os.path.abspath('..'),
                'mainline',
                'po')
        if n == 3:
            p = sys.argv[2]
            if p == 'tmp':
                path_tmp = os.path.join(
                    os.path.abspath('..'),
                    'tmp',
                    'po')
            else:
                path_tmp = os.path.join(p, 'po')
else:
    print('Using default paths')
    path = os.path.join(
                '~',
                'Activities',
                'TurtleBlocks.activity',
                'po')

po_files = glob.glob(os.path.join( os.path.abspath('.'), 'po', '*.po'))
for pof in po_files:
    print('processing:', os.path.basename(pof))
    taf = os.path.expanduser(os.path.join(
            path,
            os.path.basename(pof)))
    taf_output = taf

    if not(DEFAULT):
            taf_output = os.path.expanduser(os.path.join(
            path_tmp,
            os.path.basename(pof)))

    if os.path.exists(taf):
        command_line = ['msgcat', pof, taf, '-o', taf_output]
        if subprocess.call(command_line) > 0:
            print('error processing', pof)
    else:
        print('skipping', taf)

