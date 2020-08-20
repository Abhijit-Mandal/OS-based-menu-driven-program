import os
import pyttsx3

pyttsx3.speak("Hello!")
pyttsx3.speak("I hope you're doing well in this pandemic.")
while True:
	print("How may I help you?")

	x=input()

	if("dont" in x) or ("don't" in x) or ("do not" in x) or ("exit" in x) or ("quit" in x) or ("terminate" in x):
		break
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("chrome" in x):
		if("search" in x):
			p=input("What do you want to search: ")
			q=p.replace(" ","+")
			site="\"chrome https://www.google.com/search?q="+ q +"\""
			os.system(site)
		else:
			os.system("chrome")
	elif("open" in x or "launch" in x or "start" in x or "go to" in x) and ("website" in x):
			p=input("What website do you want to open: ")
			site="\"chrome "+ p +"\""
			os.system(site)
	elif ("open" in x or "launch" in x or "execute" in x or "start" in x or "run" in x) and ("youtube.com" in x or "youtube" in x):
			if("play" in x or "search" in x or "video" in x):
				p=input("Please enter what you want to search in youtube: ")
				q=p.replace(" ","+")
				site="\"chrome https://www.youtube.com/results?search_query="+q+"\""
				os.system(site)
			else:
				os.system("chrome youtube.com")
	elif("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("device manager" in x):
			os.system("devmgmt.msc")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("task manager" in x):
			os.system("taskmgr")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("calculator" in x):
			os.system("calc")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("control panel" in x):
			os.system("control panel")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("file explorer" in x):
			os.system("explorer")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("microsoft store" in x):
			os.system("start ms-windows-store:")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("msconfig" in x):
			os.system("msconfig")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("notepad" in x or "text editor" in x):
			os.system("notepad")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("media player" in x or "windows media player" in x):
			os.system("wmplayer")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("vlc" in x or "vlc media player" in x):
			os.system("vlc")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("paint" in x):
			os.system("mspaint")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("ms word" in x or "microsoft word" in x):
			os.system("WINWORD")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("ms excel" in x or "microsoft excel" in x):
			os.system("EXCEL")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("ms powerpoint" in x or "microsoft powerpoint" in x):
			os.system("POWERPNT")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("ms outlook" in x or "microsoft outlook" in x):
			os.system("OUTLOOK")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("jupyter" in x):
			os.system("jupyter notebook")
	elif("tell" in x or "show" in x or "display" in x or "what" in x) and ("time" in x):
			os.system("time /t")
	elif("tell" in x or "show" in x or "display" in x or "what" in x) and ("date" in x):
			os.system("date /t")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("on screen keyboard" in x or "screen keyboard" in x):
			os.system("osk")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x) and ("camera" in x or "webcam" in x):
			os.system("start microsoft.windows.camera:")
	elif("show" in x or "open" in x or "display" in x or "want" in x) and ("wifi" in x or "networks" in x or "wifi networks" in x or "wifi network" in x) and ("details" in x or "detail" in x): 
			p=input("Enter your wifi or network's name: ")
			q="\"netsh wlan show profile \""+p+"\" "+"key=clear\""
			os.system(q)
	elif("show" in x or "open" in x or "list" in x) and ("wifi" in x or "networks" in x or "wifi networks" in x or "wifi network" in x):
			os.system("netsh wlan show profile")
	elif("shutdown" in x) :
			os.system("shutdown /s")
	elif("restart" in x):
			os.system("shutdown /r")
	elif("display" in x) and ("gui" in x or "graphical interface" in x or "graphical user interface" in x):
			os.system("shutdown /i")
	elif("abort" in x) and ("shutdown" in x):
			os.system("shutdown /a")
	elif("help" in x ):
			os.system("shutdown /?")
	elif("log off" in x):
			os.system("shutdown /l")
	elif ("open" in x or "launch" in x or "execute" in x or "start"in x or "run" in x or "show" in x ) and ("controls" in x or "settings" in x or "setting" in x):
		if("display" in x):
			os.system("Start ms-settings:display")
		elif("sound" in x):
			os.system("Start ms-settings:sound")
		elif("notifications" in x or "actions" in x):
			os.system("Start ms-settings:notifications")
		elif("focus assist" in x):
			os.system("Start ms-settings:quiethours")
		elif("power" in x or "sleep" in x):
			os.system("Start ms-settings:powersleep")
		elif("battery" in x):
			os.system("Start ms-settings:batterysaver")
		elif("storage" in x):
			os.system("Start ms-settings:storagesense")
		elif("tablet mode"in x):
			os.system("Start ms-settings:tabletmode")
		elif("multitasking" in x):
			os.system("Start ms-settings:multitasking")
		elif("projecting" in x):
			os.system("Start ms-settings:project")
		elif("shared experiences" in x):
			os.system("Start ms-settings:crossdevice")
		elif("clipboard" in x):
			os.system("Start ms-settings:clipboard")
		elif("about" in x):
			os.system("Start ms-settings:about")
		elif("bluetooth" in x):
			os.system("Start ms-settings:bluetooth")
		elif("printers"in x or "scanners" in x):
			os.system("Start ms-settings:printers")
		elif("mouse" in x):
			os.system("Start ms-settings:mousetouchpad")
		elif("touchpad" in x):
			os.system("Start ms-settings:devices-touchpad")
		elif("typing"in x):
			os.system("Start ms-settings:typing")
		elif("pen" in x and "windows ink" in x):
			os.system("Start ms-settings:pen")
		elif("autoplay" in x):
			os.system("Start ms-settings:autoplay")
		elif("usb" in x):
			os.system("Start ms-settings:usb")
		elif("phone" in x):
			os.system("Start ms-settings:mobile-devices")
		elif("status"in x or "network status" in x):
			os.system("Start ms-settings:network-status")
		elif("cellular" in x or "sim" in x):
			os.system("Start ms-settings:network-cellular")
		elif("wifi" in x):
			os.system("Start ms-settings:network-wifi")
		elif("wifi calling" in x):
			os.system("Start ms-settings:network-wificalling")
		elif("ethernet" in x):
			os.system("Start ms-settings:network-ethernet")
		elif("dial up" in x or "dialup" in x):
			os.system("Start ms-settings:network-dialup")
		elif("vpn" in x):
			os.system("Start ms-settings:network-vpn")
		elif("Airplane mode" in x):
			os.system("Start ms-settings:network-airplanemode")
		elif("mobile hotspot" in x or "hotspot" in x):
			os.system("Start ms-settings:network-mobilehotspot")
		elif("data usage" in x):
			os.system("Start ms-settings:datausage")
		elif("proxy" in x):
			os.system("Start ms-settings:network-proxy")
		elif("background" in x):
			os.system("Start ms-settings:personalization-background")
		elif("colors" in x or "colours" in x):
			os.system("Start ms-settings:colors")
		elif("lock screen" in x):
			os.system("Start ms-settings:lockscreen")
		elif("themes" in x):
			os.system("Start ms-settings:themes")
		elif("fonts" in x):
			os.system("Start ms-settings:fonts")
		elif("start" in x):
			os.system("Start ms-settings:personalization-start")
		elif("taskbar" in x):
			os.system("Start ms-settings:taskbar")
		elif("apps" in x or "features" in x):
			os.system("Start ms-settings:appsfeatures")
		elif("default apps"in x):
			os.system("Start ms-settings:defaultapps")
		elif("offline maps" in x):
			os.system("Start ms-settings:maps")
		elif("apps for websites" in x):
			os.system("Start ms-settings:appsforwebsites")
		elif("video playback" in x):
			os.system("Start ms-settings:videoplayback")
		elif("startup" in x):
			os.system("Start ms-settings:startupapps")
		elif("your info" in x):
			os.system("Start ms-settings:yourinfo")
		elif("email" in x or "accounts" in x):
			os.system("Start ms-settings:emailandaccounts")
		elif("sign in options" in x):
			os.system("Start ms-settings:signinoptions")
		elif("access work" in x or " access school" in x):
			os.system("Start ms-settings:workplace")
		elif("family" in x or "other people" in x):
			os.system("Start ms-settings:otherusers")
		elif("sync" in x and "settings" in x):
			os.system("Start ms-settings:sync")
		elif("date" in x or "time" in x):
			os.system("Start ms-settings:dateandtime")
		elif("region" in x or "language" in x):
			os.system("Start ms-settings:regionlanguage")
		elif("speech" in x):
			os.system("Start ms-settings:speech")
		elif("game bar" in x):
			os.system("Start ms-settings:gaming-gamebar")
		elif("game dvr" in x):
			os.system("Start ms-settings:gaming-gamedvr")
		elif("broadcasting" in x ):
			os.system("Start ms-settings:gaming-broadcasting")
		elif("game mode" in x):
			os.system("Start ms-settings:gaming-gamemode")
		elif("trueplay" in x):
			os.system("Start ms-settings:gaming-trueplay")
		elif("xbox networking" in x):
			os.system("Start ms-settings:gaming-xboxnetworking")
		elif("display" in x and "ease of access" in x):
			os.system("Start ms-settings:easeofaccesss-display")
		elif("magnifier" in x and "ease of access" in x):
			os.system("Start ms-settings:easeofaccess-magnifier")
		elif("color filters" in x or "colour filters" and "ease of access" in x):
			os.system("Start ms-settings:easeofaccess-colorfilter")
		elif("high contrast" in x and "ease of access" in x):
			os.system("Start ms-settings:easeofaccesss-highcontrast")
		elif("narrator" in x and " ease of access" in x):
			os.system("Start ms-settings:easeofaccess-narrator")
		elif("audio" in x and "ease of access" in x ):
			os.system("Start ms-settings:easeofaccess-audio")
		elif("closed captions" in x and "ease of access" in x):
			os.system("Start ms-settings:easeofaccess-closedcaptioning")
		elif("speech" in x and "ease of access" in x):
			os.system("Start ms-settings:easeofaccess-speechrecognition")
		elif("keyboard" in x and "ease of access" in x):
			os.system("Start ms-settings:easeofaccess-keyboard")
		elif("mouse" in x and "ease of access" in x):
			os.system("Start ms-settings:easeofaccess-mouse")
		elif("eye control" in x and "ease of access" in x):
			os.system("Start ms-settings:easeofaccess-eyegaze")
		elif("other controls" in x and "ease of access" in x):
			os.system("Start ms-settings:easeofaccess-otheroptions")
		elif("talk to cortana" in x):
			os.system("Start ms-settings:cortana")
		elif("permissions" in x or "history" in x and "cortana" in x):
			os.system("Start ms-settings:cortana-permissions")
		elif("notifications" in x and "cortana" in x):
			os.system("Start ms-settings:cortana-notifications")
		elif("more details" in x and "cortana" in x):
			os.system("Start ms-settings:cortana-moredetails")
		elif("general" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-general")
		elif("speech" in x or "inking" in x or "typing" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-speechtyping")
		elif("diagnostics" in x or "feeback" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-feedback")
		elif("activity" in x or "history" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-activityhistory")
		elif("location" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-location")
		elif("camera" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-webcam")
		elif("microphone" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-microphone")
		elif("notifications" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-notifications")
		elif("account info" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-accountinfo")
		elif("contacts" in x and "privacy" in x):
			os.system("Start ms-settings:cprivacy-contacts")
		elif("calendar" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-calendar")
		elif("messaging" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-messaging")
		elif("radios" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-radios")
		elif("other devices" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-customdevices")
		elif("background apps" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-backgroundapps")
		elif("app diagnostic" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-appdiagnostics")
		elif("automatic file downloads" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-automaticfiledownloads")
		elif("documents" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-documents")
		elif("pictures" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-pictures")
		elif("videos" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-videos")
		elif("file system" in x and "privacy" in x):
			os.system("Start ms-settings:privacy-broadfilesystemaccess")
		elif("windows update" in x):
			os.system("Start ms-settings:windowsupdate")
		elif("windows update" in x and "check for updates" in x):
			os.system("Start ms-settings:windowsupdate-action")
		elif("windows update" in x and "update history" in x):
			os.system("Start ms-settings:windowsupdate-history")
		elif("windowns update" in x and "restart options" in x):
			os.system("Start ms-settings:windowsupdate-restartoptions")
		elif("windows update" in x and "advanced options" in x):
			os.system("Start ms-settings:windowsupdate-options")
		elif("windows security" in x or "windows defender" in x):
			os.system("Start ms-settings:windowsdefender")
		elif("backup" in x):
			os.system("Start ms-settings:backup")
		elif("troubleshoot" in x ):
			os.system("Start ms-settings:troubleshoot")
		elif("recovery" in x):
			os.system("Start ms-settings:recovery")
		elif("activation" in x):
			os.system("Start ms-settings:activation")
		elif("find my device" in x):
			os.system("Start ms-settings:findmydevice")
		elif("for developers" in x):
			os.system("Start ms-settings:developers")
		elif("windows insider program" in x):
			os.system("Start ms-settings:windowsinsider")
		elif("audio" in x or "speech" in x and "mixed reality" in x):
			os.system("Start ms-settings:hologgraphic-audio")
		else :
			os.system("Start ms-settings:")
	
	else:
			print("Invalid choice")
	
		