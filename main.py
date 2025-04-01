from bsky import update_bio
import pylast
import time
import os
from dotenv import load_dotenv

load_dotenv()

LFM_KEY      = os.environ['LFM_KEY']
LFM_SECRET   = os.environ['LFM_SECRET']
LFM_USERNAME = os.environ['LFM_USERNAME']

network = pylast.LastFMNetwork(api_key=LFM_KEY, api_secret=LFM_SECRET)
user = network.get_user(LFM_USERNAME)

last_song_string = ""

def update_track(track, playing):
    global last_song_string
    
    if track is None:
        return

    if playing:
        song_string = f'🎶 '
    else:
        song_string = f'💿 '

    try:
        title  = track.get_title()
        artist = track.get_artist().get_name()
    except:
        print("fucked up something")
        return

    song_string += f'{title} - {artist}'

    if song_string != last_song_string:
        update_bio(song_string)
        last_song_string = song_string

def get_last():
    global last_song_string
    try:
        last_track = user.get_recent_tracks(limit=1)[0].track
        update_track(last_track, False)
    except:
        return

def get_status():
    global last_song_string
    try:
        last_track = user.get_now_playing()
        playing = True
        update_track(last_track, playing)
        if last_track is None:
            get_last()
    except:
        return

    return

if __name__ == '__main__':
    while True:
        get_status()
        time.sleep(15)
