all: linux win osx html5 winuniversal

linux:
	godot --export "Linux/X11" exports/RedBullQuiz.x86_64

win:
	sleep 2
	godot --export "Windows Desktop" exports/RedBullQuiz-win.exe

android:
	sleep 2
	godot --export "RedBullAndroid" exports/redbullquizandroid.zip

osx:
	sleep 2
	godot --export "Mac OSX" exports/RedBullQuiz-osx.zip

winuniversal:
	sleep 2
	godot --export "Windows Universal" exports/RedBullQuiz.appx

html5:
	sleep 2
	godot --export "HTML5" exports/index.html
