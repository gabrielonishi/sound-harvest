from typing import List

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube, Search

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials())

playlist_uri = input("Copie e cole o link da playlist: ")

print('Buscando informações da playlist no Spotify')
playlist = spotify.playlist(
    playlist_uri, fields=None, market=None, additional_types=('track', ))


class Song():
    def __init__(self, title: str, artist: str, youtube_query: str) -> None:
        self.title = title
        self.artist = artist
        self.youtube_query = youtube_query


songs: List[Song] = list()


for track in playlist['tracks']['items']:
    title = track['track']['name']
    artists = ''
    for i, artist in enumerate(track['track']['artists']):
        artists += artist['name']
        if len(track['track']['artists']) > 1 and i != len(track['track']['artists']) - 1:
            artists += ', '
    youtube_query = title + " " + artists + " official audio"

    songs.append(Song(title, artists, youtube_query))


print('Playlist encontrada!')
print('Baixando músicas do youtube...')

for song in songs:
    search_object = Search(song.youtube_query)
    results = search_object.results
    possible_urls = list()
    for result in results:
        possible_urls.append(result.watch_url)

    print("Urls encontradas")
    print("Tentando baixar...")
    audio_stream = None
    i = 0
    while audio_stream is None and i < len(possible_urls):
        print(f"Tentando baixar do link {i}")
        youtube_object = YouTube(possible_urls[i])
        max_res = youtube_object.streams.get_highest_resolution().resolution
        audio_stream = youtube_object.streams.filter(
            only_audio=True, file_extension='mp4').first()
        i+=1
    audio_stream.download(output_path='downloaded_songs',
                        filename=f"{song.title.replace(' ', '_').lower()}.mp3")
        
print('Músicas baixadas!')
# print(youtube_search_keys)
