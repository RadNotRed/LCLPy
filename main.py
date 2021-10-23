#Modules
import sys
sys.path.insert(1, 'modules')
import argparse
import time
import launch
import config
import subprocess
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
command.add_argument('-s','-server',
                     action="store",
                     nargs=2,
                     metavar=("<Version>", "<Server IP>"),
                     help="Version => 1.7/1.8/1.12/1.16/1.17/1.18")
command.add_argument('-edit',
                     action='store_true',
                     help="Edit LCLPy's Config File.")
command.add_argument('-about',
                     action="store_true",
                     help="View LCLPy & LCL's Github Repositories.")
command.add_argument('-ctt',
                     action="store_true",
                     help="Join CTT's Discord Server!")   
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
elif args.about == True:
    subprocess.Popen(["start",
                      "https://github.com/Aetopia/LCLPy"],
                     shell=True)
    time.sleep(0.1)
    subprocess.Popen(["start",
                      "https://github.com/Aetopia/Lunar-Client-Lite-Launcher"],
                     shell=True)
elif args.ctt == True:
    subprocess.Popen(["start",
                      "https://discord.com/invite/CTT"],
                     shell=True) 
