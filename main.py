#Modules
import sys
sys.path.insert(1, 'modules')
import argparse
import launch
import config
import subprocess
import os

try:
    os.mkdir(os.getenv("HOME")+"/LCLPy")
except:
    pass
os.chdir(os.getenv("HOME")+"/LCLPy")

#Checks if Options.ini exists or not.
config.ConfigExist()

#CLI Arguments
parser=argparse.ArgumentParser(prog="Lunar Client Lite Python (LCLPy)",
                               description="A debloated, feature rich and CLI based launcher for Lunar Client. Made in Python.",
                               usage="\nLCLPy -v <Version>\nLCLPy -s <Version> <Server IP>")
command=parser.add_mutually_exclusive_group(required=True)
command.add_argument('-v','-version',
                     action="store",
                     nargs=1,
                     metavar=("<Version>"),
                     help="Version => 1.7/1.8/1.12/1.16/1.17/1.18")
command.add_argument('-d','-debug',
                     action="store",
                     nargs=1,
                     metavar=("<Version>"),
                     help="Displays the selected version, JRE path, launch directory, arguments and launch command.")

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
    launch.Launch(str(args.v[0]), " ", False)
elif args.edit == True:
    subprocess.run(["nano Options.ini"], shell=True)
elif args.s != None:
    launch.Launch(str(args.s[0]), "-server "+args.s[1], False)
elif args.d != None:
    launch.Launch(str(args.d[0]), " ", True)
    
