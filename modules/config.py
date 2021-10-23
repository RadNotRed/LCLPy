import os
import configparser
USERPROFILE=os.environ['USERPROFILE']
APPDATA=os.environ['APPDATA']

def ConfigExist():
    if os.path.isfile("Options.ini") is False:
        ConfigCreate()
    
def ConfigCreate():
    config = configparser.ConfigParser()
    config['Minecraft'] = {'1.7 Directory': APPDATA+"\\.minecraft",
                           '1.8 Directory': APPDATA+"\\.minecraft",
                           '1.12 Directory': APPDATA+"\\.minecraft",
                           '1.16 Directory': APPDATA+"\\.minecraft",
                           '1.17 Directory': APPDATA+"\\.minecraft",
                           '1.18 Directory': APPDATA+"\\.minecraft"
                           }
    config['Java'] = {'Arguments': "-Xms3G -Xmx3G -Xmn1G -XX:+DisableAttachMechanism",
                      '1.7 Java': USERPROFILE+"\\.lunarclient\\jre\\zulu16.30.15-ca-fx-jre16.0.1-win_x64\\bin\\javaw.exe",
                      '1.8 Java': USERPROFILE+"\\.lunarclient\\jre\\zulu16.30.15-ca-fx-jre16.0.1-win_x64\\bin\\javaw.exe",
                      '1.12 Java': USERPROFILE+"\\.lunarclient\\jre\\zulu16.30.15-ca-fx-jre16.0.1-win_x64\\bin\\javaw.exe",
                      '1.16 Java': USERPROFILE+"\\.lunarclient\\jre\\zulu16.30.15-ca-fx-jre16.0.1-win_x64\\bin\\javaw.exe",
                      '1.17 Java': USERPROFILE+"\\.lunarclient\\jre\\zulu16.30.15-ca-fx-jre16.0.1-win_x64\\bin\\javaw.exe",
                      '1.18 Java': USERPROFILE+"\\.lunarclient\\jre\\zulu16.30.15-ca-fx-jre16.0.1-win_x64\\bin\\javaw.exe",
                      }
    config['Optimizations'] = {'Minecraft Launcher Optimizations' : "Off",
                               'LC Cosmetics' : "On"
                               }
    with open('Options.ini', 'w') as configfile:
        config.write(configfile)
        
def ConfigRead(Version, Value):
    ConfigExist()
    config = configparser.ConfigParser()
    config.read('Options.ini')
    Arguments_String=config['Java']["Arguments"]
    Arguments_List=Arguments_String.split()

    if Version=="1.7":
        Java_Path=config['Java']["1.7 Java"]
        Directory=config['Minecraft']["1.7 Directory"]
        Cosmetics=config['Optimizations']['LC Cosmetics']
    elif Version=="1.8":
        Java_Path=config['Java']["1.8 Java"]
        Directory=config['Minecraft']["1.8 Directory"]
        Cosmetics=config['Optimizations']['LC Cosmetics']
    elif Version=="1.12":
        Java_Path=config['Java']["1.12 Java"]
        Directory=config['Minecraft']["1.12 Directory"]
        Cosmetics=config['Optimizations']['LC Cosmetics']
    elif Version=="1.16":
        Java_Path=config['Java']["1.16 Java"]
        Directory=config['Minecraft']["1.16 Directory"]
        Cosmetics=config['Optimizations']['LC Cosmetics']
    elif Version=="1.17":
        Java_Path=config['Java']["1.17 Java"]
        Directory=config['Minecraft']["1.17 Directory"]
        Cosmetics=config['Optimizations']['LC Cosmetics']
    elif Version=="1.18":
        Java_Path=config['Java']["1.18 Java"]
        Directory=config['Minecraft']["1.18 Directory"]
        Cosmetics=config['Optimizations']['LC Cosmetics']
    if Value=="Java_Path":    
        return Java_Path
    elif Value=="Directory":
        return Directory
    elif Value=="Cosmetics":
        return Cosmetics
    elif Value=="Arguments_List":
        return Arguments_List
