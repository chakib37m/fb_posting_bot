# fb_posting_bot

#### Video Demo:  https://youtu.be/zCDlx1P2H2o

#### Description:

YOU'LL NEED TO DOWNLOAD CHROME DRIVER BECAUSE IT USES SELENIUM.
https://chromedriver.chromium.org/downloads


This was my first python project since I wanted to learn by making stuff so that i Don't get caught up in basic.

basically all this project does is take posts/memes from reddit and post them to facebook, you can edit the subreddits in the file called 'source'. It also can get quotes from https://quotes.net and posts them into facebook.

this might be useful if you want to keep a page working or a keep a group from dying or something, I don't know.
or piss off people because why not.
or just keep it for search or send memes in a groupchat.

for now, this project can not deal with videos/gifs, only pictures and text or both.

I used FLask module to make it into a website now, using session and hashlib's sha256 to save the cookies using pickle into a file so that no one can find your cookies file unless they had access to the server.

I used sqlite3 for the database as well and saved the password and username as a single hash.

it will ask for your email and password only for the first time you use it, then generate a file to login by cookies (as it didn't even close the browser).
you can edit memebot.py to and change headless to false incase you wanted to see it working.

If you rollback into a version before adding flask, or even just change the code a little bit to execute it from the terminal (executing memebot.py as the main program alone and changing the source function not to have any arguments or set them as global variables in advance as they'd have a default value), you can use it as a messaging bot that I took from here and automated : https://www.elbot.com, you can also run it in a groupchat to send memes when someone says 'memebot' or send the first picture when someone uses the command 'search'.

I decided to reuse this project with what I learned in CS50 as the final project because I was still taking it the time, and this was my first time at all doing something remotely useful to be honest. This was CS50x.