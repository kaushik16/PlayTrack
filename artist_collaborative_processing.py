import collections
import json
import numpy as np
import heapq
from sklearn.feature_extraction import DictVectorizer
from scipy import sparse
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import pickle

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

start = 0
playlist_vs_artists, artist_name, unique_artists = [], [], set()
count = 0
for i in range(1000):
    end = start + 999
    with open('data/mpd.slice.'+str(start)+'-'+str(end)+'.json') as f:
        slice = json.load(f)

    for playlist in slice['playlists']:
        artist_name = []
        for song in playlist['tracks']:
            artist = song['artist_name']
            artist_name.append(artist)
            unique_artists.add(artist)
        playlist_vs_artists.append(collections.Counter(artist_name))

    print("Slice : " + str(i) + " - Parsed")
    start = end + 1

challenge_artists = set()
slice = json.load(open('challenge_set.json'))
for playlist in slice['playlists']:
    for song in playlist['tracks']:
        challenge_artists.add(song['artist_name'])

v = DictVectorizer(sparse=True)
X = csr_matrix.transpose(v.fit_transform(playlist_vs_artists))
print 'Vectorized!'
neighbor = NearestNeighbors(n_neighbors=21, metric='cosine')
neighbor.fit(X)
print X

unique_artists = list(unique_artists)
unique_artists.sort()
print(len(unique_artists))
print 'Training Done!'

nearest_artists = {}
for artist_index in range(len(unique_artists)):
    if unique_artists[artist_index] in challenge_artists:
        neighbors = neighbor.kneighbors([X[artist_index]], return_distance=False)
        neighbors = [unique_artists[i] for i in neighbors[0]][1:]
        nearest_artists[unique_artists[artist_index]] = neighbors
    if artist_index%2000 == 0: print artist_index

print 'Processing Complete!'
save_obj(nearest_artists, "NearestArtists_reduced")
