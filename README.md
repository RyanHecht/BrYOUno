# BrYOUno v1.0
###### The in-dorm personal assistant
###### Features, demos, and partial dependency list below
![BrYOUno main setup](http://image.prntscr.com/image/14fe8130ba3242df84988aa42b56f602.png)

## Background

A personal automation assistant for my dorm room is something I've planned on making before even coming to college, and luckily for me,
an automation class gave me an excuse to make it sooner than I'd expected! Armed with a Raspberry Pi, some electronics, an Arduino Uno,
and a whole 'lotta Python, I've created version 1.0 of BrYOUno (Bruno to his friends). [Ask him how he's doing!](https://www.youtube.com/watch?v=kiSEGOG-h4Y)

## Features
*Automates dorm lightswitch

*Plays Google Play Music

*Plays audio from MCParks Audio Server (a personal project of mine)

*Lists, adds, and completes Todoist tasks

*Queries Brown Dining API (or it will, when the API is updated)

*Logs all actions/errors to SQLite database

*Voice activated, or controllable from web dashboard

### Control flow
![Control flow](http://image.prntscr.com/image/f37542d9f26e4c5d81d84b339b8dd7d7.png)

### Lights
*GPIO digital output to infrared transmitter circuit

*Sends signal to infrared receiver, which inputs to an Arduino Uno

*Arduino Uno switches the state of a servo, which turns a piece of wood housing the lightswitch

![Lights setup](http://image.prntscr.com/image/628352542cf04f69b2a97b3b1361054a.png)

#####Lights Demo Video

<a href="http://www.youtube.com/watch?feature=player_embedded&v=AEW0pxpv7_A
" target="_tab"><img src="http://img.youtube.com/vi/AEW0pxpv7_A/0.jpg"
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

### Google Play Music
*GMusicProxy, open source locally hosted Google Play Music API

*User chooses between song, artist, playlist, or station, system obtains necessary information, then fetches the M3U playlist file

*M3U file is handed off to mplayer subprocess, which plays the audio

*Stopped with Flask API call, “/music/stop”

#####Google Play Music Demo Video

<a href="http://www.youtube.com/watch?feature=player_embedded&v=0sgMwBeWgmk
" target="_tab"><img src="http://img.youtube.com/vi/0sgMwBeWgmk/0.jpg"
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

### Task Management
*ToDoist API/Python wrappers

*User is orally prompted whether they’d like to list, add, or complete a task

*Process is looped, so you can perform multiple operations at a time

#####Todoist Demo Video

<a href="http://www.youtube.com/watch?feature=player_embedded&v=vsCGVdoejL4
" target="_tab"><img src="http://img.youtube.com/vi/vsCGVdoejL4/0.jpg"
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

### Alternative input

In addition to voice commands, system may be controlled through web dashboard (Made with Google's Materialize CSS library)
I have this one running on a tablet mounted above my bed.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=T9fPB6J6O5I
" target="_tab"><img src="http://img.youtube.com/vi/T9fPB6J6O5I/0.jpg"
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

### Data logging

All actions and errors are logged in an SQLite database, which is viewable online with sqllite-web

![database-viewer](http://image.prntscr.com/image/003e053aae6d47f589fc428ad6336862.png)

### Hardware Dependencies

+Raspberry Pi (model 3 used)

+Microphone with onboard sound card

+Speakers

+Electronics for IR transmitter circuit (transmitter/LED, PNP transistor, resistor)

+Electronics for IR receiver (receiver, servo)

+Arduino (Uno used)

+Tablet/Phone/Computer for web interface

### Software Dependencies on Raspberry Pi (partial list, I'm more than likely forgetting stuff)

+Raspian 8

+Python 2.7

+[Snowboy](http://docs.kitt.ai/snowboy/)

+[SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition/)

+[PyAudio 0.2.9+](https://pypi.python.org/pypi/PyAudio)

+[Websocket client](https://pypi.python.org/pypi/websocket-client/)

+[pyttsx](https://pypi.python.org/pypi/pyttsx)

+[Flask](http://flask.pocoo.org/)

+[WSGI webserver](https://wsgi.readthedocs.io/en/latest/)

+[sqlite-web](https://github.com/coleifer/sqlite-web)

+[GMusicProxy](http://gmusicproxy.net/)

+[pytodoist](http://pytodoist.readthedocs.io/en/latest/)

+[urllib](https://docs.python.org/2/library/urllib.html)

That's all I can think of, if I'm missing anything, feel free to open an issue!
