# Facebook's postin bot

#### Video Demo:  https://youtu.be/zCDlx1P2H2o

#### Description:

YOU WILL NEED TO DOWNLOAD CHROME DRIVER BECAUSE IT USES SELENIUM.
https://chromedriver.chromium.org/downloads


This was my first python project since I wanted to learn by making stuff so that i Don't get caught up in basic. It was my way of learning it and I was doing CS50 at the time s I thought of keeping it as a final project.

basically all this project does is take posts/memes from reddit and post them to facebook, you can edit the subreddits in the file called 'source'. It also can get quotes from https://quotes.net and posts them into facebook.

this might be useful if you want to keep a page working or a keep a group from dying or something, I don't know.
or piss off people because why not.
or just keep it for search or send memes in a groupchat.

for now, this project can not deal with videos/gifs, only pictures and text or both.

I used FLask module to make it into a website now, added some HTML to it, mainly just used Bootstrap for the CSS because design wasn't so important to me, considering that it was at first attempted to be used from the terminal.
I used session with an sqlite3 database to save the user and that they're logged in.
I used hashlib's sha256 to save both the username and the password as one single hash from the database. To add some kind of a security layer.
It will ask for your Facebook's email and password only for the first time you use it, then generate a file to login by cookies (as it didn't even close the browser), I used pickle for saving the cookies into a file along with selenium that I used for the automating process.
Keep in mind that Selenium uses a real browser to be automated, and using something other than chrome/chromium will need you to actually change a few things in the code, like switching chromedriver to geckodriver for Firefox.
Also this project won't work unless you have a chromedriver, you can download it here : https://chromedriver.chromium.org/downloads
you can edit memebot.py to and change headless to false in case you wanted to see it working.
If you rollback into a version before adding flask, or even just change the code a little bit to execute it from the terminal (executing memebot.py as the main program alone and changing the source function not to have any arguments or set them as global variables in advance as they'd have a default value), you can use it as a messaging bot that I took from here and automated : https://www.elbot.com, you can also run it in a groupchat to send memes when someone says 'memebot' or send the first picture when someone uses the command 'search'.

I was still taking CS50 at the time I started learning python, and it's been quite a journey, I'm thankful to all of the staff to making this course accessible freely.

THIS WAS CS50X
