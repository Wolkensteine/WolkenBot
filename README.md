# WolkenBot
Just a small discord bot for myself and my friends<br>
This is just the newest fully functional version of the bot.<br>

# Feature list (This might be out of date when I don't remember to add the features here!)
Hello bot => Sends you back a hello and reacts with a wave hand on your message<br><br>
!help => Gives you help to the bot (may be out of date sometimes)<br><br>
!friend => Will send you a random message<br><br>
!vote => Lets you create a poll for others and yourself. More description is given when you execute the command. !Attention! While a vote is running no commands can be executed.<br><br>
!info => This will just return some general information about the bot, that you don't need (also might be out of date sometimes) because you have this repository.<br><br>
!pin => Will pin the following messag (Details: Will resend the message as embed and pin that. Your original message will get deleted)<br><br>
!math => Do !math.help for more information (basically just some small math functions)<br><br>
!bot => Is just to see if the bot is there but hasn't actually a usefull usecase.<br><br>
!gif + input => This will search via the Tenor API a fitting gif for you keyword/-s. (Update 2.0.0 - You will now get one random one of ten found ones everytime)<br><br>
!play => Do !play.help for more information (Basically just playing short audios to the channel you are currently connected to)<br><br>
!g => A fun command I won't explain here. Use it to find out.<br><br>
!rate + text => Lets you rate your text<br><br>
!randomname => Will return a random name out of the name array. If you use this by yourself you may want to add some of your friend names.<br><br>
!dadjoke (requested by BinMalKurzImWald) => Will spit out a horrible bad joke (List was also created by binMalKurzImWald)<br><br>



# ToDo before using
<br>
You will need to replace the file names for the audio files you can play with file names of files on your system.<br><br>
You will need to put in your discord bot client secret<br><br>
You will need to have installed some sort of ffmpeg or replace the path in the file to ffmpeg.exe<br><br>
You will need to replace the API key for the google tenor api with your owns.<br>

## Hardware requirements
<br>
This bot is easily running on a raspberry pi 4b 8gb (on raspberian), I wouldn't recomend this hardware for use on many servers but for a youple of servers it should be enough.

## Other requirements
<br>
You will need Python (just get the newest version it should work fine) and pip<br>
Some sort of ffmpeg (as an .exe file on windows or installed on linux)<br>
A lot of librarys. When you execute the main.py file you'll get some error messages so just follow those but you should at least have python.py installed.<br>
