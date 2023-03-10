import spotipy

def get_spotify(session):
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return None
    # The user is signed in
    return spotipy.Spotify(auth_manager=auth_manager)