# BrYOUno
###### The in-dorm personal assistant
###### Features, demos, and partial dependency list below
![BrYOUno main setup](https://lh3.googleusercontent.com/jAE1QA25SvL6YfqY-jTqnHvQ5rLyk_wp83soyXtteHmFeDP7UCK2zBD2hZSqito6JAGdpP9yoIoOcryw_lC3AATTdL3KwQrQymM-MdBBAToZ-h09NVnLKDElR82jU1uKBKkwv3cLLrIYMuaEmErlkhFp1KTdFGa0xIcPwNceaENxQZ5OyMtAheHATBAg8H6prRXHW_5GU01PeYvRPvhsg4y7SkEBeZ3_IuWTHUJHZj448u7_yXnVVm9LramI8v28coFTNsfGTn6C8rnxnyoO2CzfWTKpWh5S_nFFbwNnwwjh3s0w2n9Fya3GrSRQ9w53ARudT2KyXdsO9PW-qiXJA7KSqwW2Pul5qq9qL13jXffne--kH51fo4dkqZcLUPKuQ_Mo8IqOf3SgDp-3TKimzzv8tcDJJhGabFgfWnL03BZSsuHVUJrexEPBehtG1YV0eyK13qkoR4e7MYsgIGCt7DACCtmJt5NLHkTFe1bz2RmiQ6AJaHkcsEcTCdFPh22WRjXgDk1geaQUEdSg6OtdztRnUEpcEzswwAvU7IwMWSA_0jKeWu2GfYX7_F9IodS-KdAf0YXQn0v-zMeoPYCOQLyg0Z1Ajs1Pvgn7Rd1LZmbjI-Xolzc4=w713-h950-no)
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

![Lights setup](https://lh3.googleusercontent.com/_ie9Slhlfo_YYEGuuShZ5oDIjq6hxA-9uXqlCm0jvN6K6O8lDJT7DSPz4csbehlahgql35OvFdR91cFMkD-iz0mWdy4iQugAzJLgy2CfjhWKn00Mo2_ZJe43pUfTvt20ocHnjNL1IpdbaiEfgo8CFPj1EovZ1ittCLJiNik1f7d3-xiYKKq2Q05Khckfn1sFT3u3ZmWuzXwM2V09hgKXfuSe2RywUyvGwogEBmZCO7doXeHX4BiQiDMsFOCCcSxGZoRxBzi7iSY8yMAt9AJ7iKvayAA5yB3CwLGxeu8Df_nuKeHD9EwSvTDUxmKb9TGErq8hUHG928AWbAzrG1pDPrHosTXMF-5E_zl38vJ_KzzlYL22ihB8bKz7m5uAWXk6SuPQLiix3wPlrTFeQnbtKE7Tb_gDmNnWVbVnTbtG-MORoGK-1EUw4I25hvnvCDVjnxxVF1QpEDCLbRUS-MszU8-mN-vKRxUSa1H7wRW4sUdLaZeX6CqdOcYbF8KS-xVoAt1RfJ-Ut43-TuozSBaxqlaug8yvkLu97d5wQJAZ2A0VnQJv7lxNRqjyxDsarCJN0t1p77X6fTKt7YkjICDkRzcx5nYv2knxOOkhAPRq4AV5V8GZ0e1p=w713-h950-no)

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
