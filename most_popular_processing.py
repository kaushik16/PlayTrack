import json
import pickle
import math
import heapq
from collections import defaultdict

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

song_playlist_count, song_follower_count = defaultdict(int), defaultdict(int)
max_playlist_count, max_follower_count = 0, 0
song_to_artist = {}
start = 0
songsData = load_obj('Songs_Data')

for i in range(1000):
    end = start + 999
    with open('data/mpd.slice.'+str(start)+'-'+str(end)+'.json') as f:
        slice = json.load(f)

    for playlist in slice['playlists']:
        for song in playlist['tracks']:
            index = songsData[song['track_uri']]
            song_playlist_count[index] += 1
            song_follower_count[index] += playlist['num_followers']
            max_follower_count, max_playlist_count = max(max_follower_count, song_follower_count[index]), max(max_playlist_count, song_playlist_count[index])
            song_to_artist[index] = song['artist_name']
    start = end + 1
    print("Slice : " + str(i) + " - Parsed")

max_playlist_count, max_follower_count = math.log10(max_playlist_count), math.log10(max_follower_count)
song_score = {song: (0.5*math.log10(song_follower_count[song])/max_follower_count) + (0.5*math.log10(song_playlist_count[song])/max_playlist_count) for song in song_playlist_count}

most_popular_songs = []
most_popular_by_artist = defaultdict(list)
for i in range(1000):
    heapq.heappush(most_popular_songs, (0,''))
for k, v in song_score.items():
    if v > most_popular_songs[0][0]: heapq.heappushpop(most_popular_songs, (v,k))

    elem = most_popular_by_artist[song_to_artist[k]]
    if len(elem) >= 100 and elem[0][0] < v: heapq.heappushpop(elem, (v, k))
    else: heapq.heappush(elem, (v, k))

most_popular_songs.sort(key = lambda x: x[0], reverse=True)
for k,v in most_popular_by_artist.items():
    v.sort(key = lambda x: x[0], reverse = True)

print len(most_popular_by_artist)
print "Processed"
save_obj(most_popular_songs, "MostPopularSongs_1000")
save_obj(most_popular_by_artist, "MostPopularSongsByArtist_100")