#! python3

from pathlib import Path
import sys
import subprocess


#My generic system command interpreter
args = sys.argv
args = args[1:len(args)]

def sysCommand(args):
    return subprocess.run(args,capture_output=True)

path = Path((sysCommand('pwd').stdout).decode()) #find current dir
sysCommand(['cd'])
if len(args) == 2:
    pathName = args[1] +'/'+ args[0]
    sysCommand(['mkdir',pathName])
    print(pathName)
    print('Made folder {}'.format(args[0]))
elif len(args) == 1:
    sysCommand(['mkdir',args[0]])
    print('Made folder {}'.format(args[0]))
else:
    print('Format Error')
    print('Use: python3 filewriter.py [foldername] [optional:path]')
