#!/usr/bin/env python
import os
import glob
import subprocess

po_files = glob.glob(os.path.join( os.path.abspath('.'), 'po', '*.po'))
for pof in po_files:
    print 'processing:', os.path.basename(pof)
    taf = os.path.expanduser(os.path.join(
            '~',
            'Activities',
            'TurtleArt.activity',
            'po',
            os.path.basename(pof)))
    if os.path.exists(taf):
        command_line = ['msgcat', pof, taf, '-o', taf]
        if subprocess.call(command_line) > 0:
            print 'error processing', pof
    else:
        print 'skipping', taf


