# Spotipi Currently Playing

## Introduction
This web application displays the album art for your currently played song on spotify.
There are basic playback controls that are shown when the album cover is pressed.

I wrote this project so that I could have the music that I am listening to displayed on a raspberry pi display.
This will work on any device that can run python 3 - not just a raspberry pi.

This project uses python's Flask web framework and queries the Spotipi API.

#### Screenshots
[![HXx9YIR.md.png](https://iili.io/HXx9YIR.md.png)](https://freeimage.host/i/HXx9YIR)

[![HXx9Xpf.md.png](https://iili.io/HXx9Xpf.md.png)](https://freeimage.host/i/HXx9Xpf)

[![HXx911t.md.png](https://iili.io/HXx911t.md.png)](https://freeimage.host/i/HXx911t)

## Setup
#### Prerequisites
- You must have a spotify dev account (this is free for non comercial projects)
- Make a new project in the spotify dev online dashboard
- Flask python package should be installed using pip: ```pip install flask```
- Create an envrionment variables (as shown below)

#### Environment
- Create a file called ```load_dotenv.py```
- Inside this file include the following (be sure to replace the values in capital letters):
```
import os

def load_dotenv():
    os.environ['FLASK_APP'] = 'app'
    os.environ['FLASK_ENV'] = 'development'  # This is only while debugging as developing
    os.environ['SPOTIPY_CLIENT_ID'] = CLIENT_ID  # This can be found on the spotify dev dashboard
    os.environ['SPOTIPY_CLIENT_SECRET'] = CLIENT_SECRET  # This can be found on the spotify dev dashboard
    os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:5000'  # This MUST be added to the spotify dev dashboard in the project settings
```

#### New features
There is now a new variable called "experimental_pi_display_mode". When this is set to true, the server's HDMI display will be disabled if there are no tracking
currently playing (and enabled when a track is playing). This has been implemented so that a Raspberry Pi can always be connected to a monitor and only display
information when it needs to.
LEAVE THIS AS FALSE IF YOU DO NOT UNDERSTAND IT.
