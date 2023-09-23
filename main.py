# from pytube import YouTube

# # URL of the YouTube video
# video_url = 'https://www.youtube.com/watch?v=VIDEO_ID'

# # Create a YouTube object
# yt = YouTube(video_url)

# # Get the highest quality audio stream
# audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

# # Download the audio stream to a file
# audio_stream.download(output_path='path_to_save_audio', filename='output_file_name')

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials())

# playlist_uri = input("Copie e cole o link da playlist: ")

print('Buscando informações da playlist no Spotify')
playlist_uri = "https://open.spotify.com/playlist/608DCsUcleYBJcKuabMhNz?si=1e98521315fc4071"
playlist = spotify.playlist(
    playlist_uri, fields=None, market=None, additional_types=('track', ))

youtube_search_keys = list()

for track in playlist['tracks']['items']:
    song_name = track['track']['name']
    artists = ''
    for i, artist in enumerate(track['track']['artists']):
        artists += artist['name']
        if len(track['track']['artists']) > 1 and i != len(track['track']['artists']) - 1:
            artists += ', '
    search_key = song_name + " " + artists + " official audio"
    youtube_search_keys.append(search_key)

print('Playlist encontrada!')
print('Baixando músicas do youtube...')

print(youtube_search_keys)