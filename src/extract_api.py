"""
Extract the raw data from Spotify,
clean and save in a .csv file to use in Tableau Public
"""

from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Get the variables to connect
load_dotenv()

# Authentication - without user
client_credentials_manager = SpotifyClientCredentials(
    client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET")
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_link = "https://open.spotify.com/playlist/37i9dQZF1DX18jTM2l2fJY"

playlist_URI = playlist_link.split("/")[-1].split("?")[0]
# track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

# Test the API
for track in sp.playlist_tracks(playlist_URI)["items"][:1]:
    # URI
    track_uri = track["track"]["uri"]
    # Track name
    track_name = track["track"]["name"]
    # Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)

    # Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_pop = artist_info["popularity"]
    artist_genres = artist_info["genres"]
    artist_id = artist_info["id"]

    related_artist = sp.artist_related_artists(artist_id)
    top_co = sp.artist_top_tracks(artist_id, "CO")

    print("Artist!!! ", artist_name)

    # Album
    album = track["track"]["album"]["name"]

    # Popularity of the track
    track_pop = track["track"]["popularity"]
