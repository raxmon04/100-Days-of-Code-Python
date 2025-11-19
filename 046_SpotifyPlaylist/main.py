from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
billboard_url = "https://www.billboard.com/charts/hot-100/"
response = requests.get(url=billboard_url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# print(song_names)

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id="",
        client_secret="",
        show_dialog=True,
        cache_path=r"C:\Git\100-Days-of-Code-Python\046_SpotifyPlaylist\token.txt"
    )
)
user_id = sp.current_user()["id"]
# print(user_id)

# Searching Spotify for songs by title
song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name="Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
