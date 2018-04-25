import pickle
from recommend_most_popular import RecommendPopular
from recommend_artist import RecommendArtist
from predictSongPair import RecommendSong
import json

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

songsData = load_obj('Songs_Data')
print songsData[0]
inv_songsData = {v:k for k,v in songsData.items()}
Popular = RecommendPopular()
Artist = RecommendArtist()
Songs = RecommendSong()

output = open('submission.csv', 'w')
output.write("team_info,Itachi_Uchiha,main,kaushik.raju@tamu.edu\n")

most_popular_songs = Popular.get_most_popular()
fill_with_popular = {0 : 500, 1 : 350, 5 : 150, 10 : 50}

slice = json.load(open('challenge_set.json'))
print "length: " + str(len(slice['playlists']))
count = 0
for playlist in slice['playlists']:
    song_list = []
    artist_list, unique_artists = [], set()
    recommendations, unique_recs = [], set()
    recommendations.append(str(playlist['pid']))
    for song in playlist['tracks']:
        if song['artist_name'] not in unique_artists: artist_list.append(song['artist_name'])
        unique_artists.add(song['artist_name'])
        song_list.append(songsData[song['track_uri']])
        unique_recs.add(songsData[song['track_uri']])

    common_artists, popular_for_artists, common_songs = [], [], []
    if len(artist_list) > 0: common_artists = Artist.get_nearest_artists(artist_list)
    if len(common_artists) > 0: popular_for_artists = Popular.get_most_popular_by_artist(common_artists)
    if len(song_list) > 0: common_songs = Songs.get_songs(song_list)

    max_songs = 500 - fill_with_popular.get(len(song_list), 0)
    i = set()
    while len(recommendations) < max_songs and i < max(len(common_songs), len(popular_for_artists)):
        if i < len(common_songs) and common_songs[i][1] not in unique_recs:
            recommendations.append(inv_songsData[common_songs[i][1]])
            unique_recs.add(common_songs[i][1])
        if i < len(popular_for_artists) and popular_for_artists[i][1] not in unique_recs:
            recommendations.append(inv_songsData[popular_for_artists[i][1]])
            unique_recs.add(popular_for_artists[i][1])
        i += 1

    j = 0
    while len(recommendations) <= 500:
        if most_popular_songs[j][1] not in unique_recs:
            recommendations.append(inv_songsData[most_popular_songs[j][1]])
        j += 1

    output.write(','.join(recommendations)+'\n')
    count += 1
    if count % 1000 == 0: print count
output.close()
