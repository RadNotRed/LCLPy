# LCLPy for Windows
<b>[Lunar Client Lite](https://github.com/Aetopia/Lunar-Client-Lite-Launcher) rewritten in Python.
 
### Looking for the Linux Version?  
Check it out here: https://github.com/Aetopia/LCLPy/tree/linux</b>

# Information
Releases: https://github.com/Aetopia/LCLPy/releases    

Wiki/Documentation: https://github.com/Aetopia/LCLPy/wiki
## Build
### Using Nuitka (Recommended)
1. Install Nuitka and ZStandard.
> If using Python `3.9`:
```
pip install nuitka
pip install zstandard
```
2. Run `build_nuitka.bat`

### Using PyInstaller
1. Install PyInstaller.
```
pip install PyInstaller
```
 OR
 > If using Python `3.10`:
```
pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
```
2. Run `build_pyinstaller.bat`.
