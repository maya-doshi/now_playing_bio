from bsky import update_bio
from flask import Flask, request
from dotenv import load_dotenv
import os

load_dotenv()

username = os.environ['LASTFM_USERNAME']
# this is the api key that has to be passed to ?api_key=
api_key = os.environ['WEBHOOK_API_KEY']

def update_track(artist, track):
    now_playing = f'{artist} - {track}'
    print(f'Now playing: {now_playing}')

    update_bio(now_playing)


app = Flask(__name__)

@app.route('/now_playing', methods=['POST'])
def lastfm_endpoint():
    provided_api_key = request.args.get('api_key')
    
    if provided_api_key == api_key:
        artist = request.args.get('artist')
        track = request.args.get('track')
        update_track(artist, track)
        return "Success", 200
    else:
        return "Unauthorized", 401

if __name__ == '__main__':
    app.run(debug=False)
