
;@Ahk2Exe-SetName LCLPy GUI
;@Ahk2Exe-SetDescription GUI for Lunar Client Lite Python
;@Ahk2Exe-SetVersion 1.0.0
;@Ahk2Exe-SetOrigFilename LCLPy_GUI.ahk
Files()
FileInstall, lclpy.exe, files/lclpy.exe, 1
FileInstall, logo.png, files/logo.png, 1 
#NoEnv
#NoTrayIcon
#SingleInstance, Force
#Warn
SendMode Input
SetWorkingDir %A_ScriptDir%

; GUI
Gui, New
Gui, Font, s10
Gui, Add, Tab3, Top +Background +0x400 -TabStop w380 h285, Launch|Settings

; Launch
Gui, Tab, 1
Gui, Font, s10
Gui, Add, Picture, x128 y50, files/logo.png
Gui, Add, Button, vLaunch w100 h50 x280 y230 +Default gLaunch, Launch
Gui, Font, s8
Gui, Add, CheckBox, x140 y265 vDebug, Debug
Gui, Add, ListBox, vVersionList h90 w100 x23 y197 gVersionWrite, 1.7|1.8|1.12|1.16|1.17|1.18
VersionSelect()

; Settings
Gui, Tab, 2
Gui, Add, Text,, Edit LCLPy's Settings:
Gui, Add, Button, w50 h25 vEdit gEdit, Edit
Gui, Add, Text,, Reset LCLPy's Settings:
Gui, Add, Button, w50 h25 vReset gReset, Reset
;Gui, Add, Text,, Manage your installation of LCLPy:
;Gui, Add, Button, w50 h25 vManage, Manage

; Window Size
Gui, Show, w400 h300, LCLPy

;Functions

; Version List
VersionWrite(){
    GuiControlGet, Selected_Version,, VersionList
	IniWrite, %Selected_Version%, cache.ini, Main, Version
}

VersionSelect(){
    IniRead, Selected_Version, cache.ini, Main, Version
	If (Selected_Version = 1.7) 
	{
		GuiControl, Choose, VersionList, 1
	}	
	Else If (Selected_Version = 1.8) 
	{
		GuiControl, Choose, VersionList, 2
	}
	Else If (Selected_Version = 1.12) 
	{
		GuiControl, Choose, VersionList, 3
	}
	Else If (Selected_Version = 1.16) 
	{
		GuiControl, Choose, VersionList, 4
	}
	Else If (Selected_Version = 1.17) 
	{
		GuiControl, Choose, VersionList, 5
	}
    Else If (Selected_Version = 1.18) 
	{
		GuiControl, Choose, VersionList, 6
	}
	return
}

; Files
Files(){
    IfNotExist, files
        FileCreateDir, files
    IfNotExist, cache.ini
        IniWrite, 1.8, cache.ini, Main, Version    
}

; Launch
Launch(){
	GuiControlGet, Version,, VersionList
	GuiControlGet, Debug,, Debug
	If (Debug = 1){
		Run, "files/lclpy.exe" -d %Version%
	}
	Else {
		Run, "files/lclpy.exe" -v %Version%,, Hide
		ExitApp
	}
}

; Settings
Edit(){
	Run, files/lclpy.exe -edit,, hide
}

Reset(){
	FileDelete, %A_APPDATA%\LCLPy\Options.ini
	MsgBox, 64, Settings Reset, LCLPy's settings are now reset., 2
}

; Window
GuiClose(){
	ExitApp
}
