#Modules
import sys
sys.path.insert(1, 'modules')
import argparse
import time
import launch
import config
import subprocess
import os

# Working Directory

# Working Directory as a script.
Script_Directory=os.getcwd()

# Working Directory when compiled.
os.chdir(os.path.dirname(sys.executable))

       
#Checks if Options.ini exists or not.
try:
    config.ConfigExist()
except:
    os.chdir(Script_Directory)
    config.ConfigExist()

# CLI Arguments
parser=argparse.ArgumentParser(prog="Lunar Client Lite Python (LCLPy)",
                               description="A debloated, feature rich and CLI based launcher for Lunar Client. Made in Python.",
                               usage="\nLCLPy -v <Version>\nLCLPy -s <Version> <Server IP>")
command=parser.add_mutually_exclusive_group(required=True)
command.add_argument('-v','-version',
                     action="store",
                     nargs=1,
                     metavar=("<Version>"),
                     help="Version => 1.7/1.8/1.12/1.16/1.17/1.18")
command.add_argument('-s','-server',
                     action="store",
                     nargs=2,
                     metavar=("<Version>", "<Server IP>"),
                     help="Version => 1.7/1.8/1.12/1.16/1.17/1.18")
command.add_argument('-edit',
                     action='store_true',
                     help="Edit LCLPy's Config File.") 
args = parser.parse_args()

#Arguments
if args.v != None:
    launch.Launch(str(args.v[0])," ")
elif args.edit == True:
    subprocess.Popen(["start",
                      "Options.ini"],
                     shell=True)
elif args.s != None:
    launch.Launch(str(args.s[0]),
                  "-server "+args.s[1])
