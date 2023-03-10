from time import sleep
from flask import Flask, jsonify, session, request, redirect, render_template
from flask_session import Session
from load_dotenv import load_dotenv
import spotipy
import spotipy_auth
import os

app = Flask(__name__, static_folder='static_files')
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)
load_dotenv()

@app.route('/')
@app.route('/player')
def index():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-read-currently-playing user-modify-playback-state user-read-playback-state',
                                               cache_handler=cache_handler,
                                               show_dialog=True)
    if request.args.get("code"):
        # Step 2. Being redirected from Spotify auth page
        auth_manager.get_access_token(request.args.get("code"))
        return redirect('/')
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        # Step 1. Display sign in link when no token
        auth_url = auth_manager.get_authorize_url()
        return f'<h2><a href="{auth_url}">Sign in</a></h2>'
    # Step 3. Signed in, display data
    return render_template('index.jinja')

@app.route('/track-info', methods=["GET"])
def track_info():
    for i in range(1): # Could increase to 10?
        sleep(1)
        spotify = spotipy_auth.get_spotify(session)
        track = spotify.current_user_playing_track()
        if track is not None:
            current_song = track['item']['name']
            print(current_song)
            current_song_data = { 
                            'track_title': track['item']['name'],
                            'artist': track['item']['artists'][0]['name'],
                            'track_progress': 20,
                            'album_cover': track['item']['album']['images'][0]['url'],
                            'duration_ms': track['item']['duration_ms'],
                            'progress_ms': track['progress_ms'],
            }
            return jsonify(current_song_data), 200
    return {}, 204

@app.route('/play_pause')
def play_pause():
    spotify = spotipy_auth.get_spotify(session)
    if spotify is None:
        return redirect('/')
    # User is authenticated
    if(spotify.current_playback()['is_playing']):
        spotify.pause_playback()
    else:
        spotify.start_playback()
    return redirect('/')

@app.route('/skip')
def skip():
    spotify = spotipy_auth.get_spotify(session)
    if spotify is None:
        return redirect('/')
    # User is authenticated
    if(spotify.current_playback()['is_playing']):
        spotify.next_track()
    return redirect('/')

@app.route('/previous')
def previous():
    spotify = spotipy_auth.get_spotify(session)
    if spotify is None:
        return redirect('/')
    # User is authenticated
    if(spotify.current_playback()['is_playing']):
        spotify.previous_track()
    return redirect('/')

@app.route('/sign_out')
def sign_out():
    session.pop("token_info", None)
    return redirect('/')


if __name__ == '__main__':
    app.run(threaded=True, port=int(os.environ.get("PORT", 
                                                   os.environ.get("SPOTIPY_REDIRECT_URI", 8080).split(":")[-1])))