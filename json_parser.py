import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# Set up your client ID and client secret
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to retrieve track IDs from a playlist
def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return [track['track']['id'] for track in tracks if track['track'] is not None]

# Function to get track information
def get_track_info(track_id):
    track = sp.track(track_id)
    return {
        "Track Name": track['name'],
        "Artists": [artist['name'] for artist in track['artists']],
        "Album": track['album']['name'],
        "Release Date": track['album']['release_date'],
        "Spotify Link": track['external_urls']['spotify']
    }

# Example usage
playlist_id = '37i9dQZF1DX5cZuAHLNjGz'  # Replace this with the playlist ID you want to scrape
track_ids = get_playlist_tracks(playlist_id)

# Collect track information into a list of dictionaries
tracks_info = [get_track_info(track_id) for track_id in track_ids]

# Save track information to a JSON file
with open('spotify_playlist.json', 'w') as json_file:
    json.dump(tracks_info, json_file, indent=4)
