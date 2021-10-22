import sys
sys.path.insert(1, 'modules')
import argparse
import launch
import config
import subprocess
config.ConfigExist()
parser=argparse.ArgumentParser(prog="Lunar Client Lite Python (LCLPy)")
command=parser.add_mutually_exclusive_group(required=True)
command.add_argument('-v','-version',
                     action="store",
                     nargs=1,
                     metavar=("<Version>"),
                     help="1.7/1.8/1.12/1.16/1.17")
command.add_argument('-edit',
                     action='store_true',
                     help="Edit LCLPy's Config File.")
args = parser.parse_args()

if args.v != None:
    launch.Launch(str(args.v[0]))
elif args.edit == True:
    subprocess.Popen(["start","Config.ini"],shell=True)
    
