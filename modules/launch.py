# Modules
import subprocess
import os
import config
import ctypes

# Variables
USERPROFILE=os.environ['USERPROFILE']
APPDATA=os.environ['APPDATA']

def Launch(Version, Server, Debug):
    # Read Values from Options.ini
    Server = Server.split()
    Config=config.ConfigRead(Version)
    # Set the Asset Index
    if Version=="1.7":
        AssetIndex="1.7.10"
    else:
        AssetIndex=Version
    # Cosmetics Toggle    
    if Config[0]=="On":
        Cosmetics_Path=USERPROFILE+"\\.lunarclient\\textures"
    else:
        Cosmetics_Path=" "
        
    # Launch Variable  
    Launch_1=[Config[1],
	"--add-modules",
	"jdk.naming.dns",
	"--add-exports",
	"jdk.naming.dns/com.sun.jndi.dns=java.naming",
	"-Djna.boot.library.path="+USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\natives",
	"--add-opens",
	"java.base/java.io=ALL-UNNAMED"]
    Launch_2=["-Djava.library.path="+USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\natives",
        "-XX:+DisableAttachMechanism",
	"-cp",
	USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\lunar-assets-prod-1-optifine.jar;"
	+USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\lunar-assets-prod-2-optifine.jar;"
	+USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\lunar-assets-prod-3-optifine.jar;"
	+USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\lunar-libs.jar;"
	+USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\lunar-prod-optifine.jar;"
	+USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\OptiFine.jar;"
	+USERPROFILE+"\\.lunarclient\\offline\\"+Version+"\\vpatcher-prod.jar",
	"com.moonsworth.lunar.patcher.LunarMain",
	"--version",
	str(Version),
	"--accessToken",
	"0", 
	"--assetIndex",
	str(AssetIndex),
	"--userProperties",
	"{}",
	"--gameDir",
	Config[2],
	"--width",
	"854",
	"--height",
	"480",
	"--texturesDir",
	Cosmetics_Path,
	"--assetsDir",
	APPDATA+"\\.minecraft\\assets"]

    Launch=Launch_1+Config[3]+Launch_2+Server
    
    # Launch
    subprocess.Popen(Launch)
    if Debug == True:
        print("Version:", Version+"\n")
        print("Java Executable:\n"+Config[1]+"\n")
        print("Launch Directory:\n"+Config[2]+"\n")
        print("Arguments:\n"+' '.join(map(str,Config[3]))+"\n")
        print("Launch Command:\n"+' '.join(map(str,Launch)))
        while True:
            print("")
            subprocess.run(["pause"],shell=True)
            exit()   
