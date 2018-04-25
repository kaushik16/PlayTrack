import pickle
from recommend_most_popular import RecommendPopular
from recommend_artist import RecommendArtist
from predictSongPair import RecommendSong
import json

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

Popular = RecommendPopular()
Artist = RecommendArtist()
Songs = RecommendSong()

most_popular_songs = Popular.get_most_popular()
fill_with_popular = {0 : 500, 1 : 350, 5 : 150, 10 : 50}
matches, total, total_recs = 0, 0, 0

slice = load_obj('Testing_Data')
count = 0

for playlist in slice:
    songs_to_include = 5 if len(playlist) == 25 else 30
    song_list = [elem[0] for elem in playlist]
    artists_to_indlude = [elem[1] for elem in playlist][:songs_to_include]
    training_songs, testing_songs = song_list[:songs_to_include], song_list[songs_to_include:]
    artist_list, unique_artists = [], set()
    recommendations, unique_recs = set(), set()
    for i in range(len(artists_to_indlude)):
        if artists_to_indlude[i] not in unique_artists: artist_list.append(artists_to_indlude[i])
        unique_artists.add(artists_to_indlude[i])
        unique_recs.add(song_list[i])

    common_artists, popular_for_artists, common_songs = [], [], []
    if len(artist_list) > 0: common_artists = Artist.get_nearest_artists(artist_list)
    common_artists = artists_to_indlude + list(set(common_artists))
    if len(common_artists) > 0: popular_for_artists = Popular.get_most_popular_by_artist(common_artists)
    if len(song_list) > 0: common_songs = Songs.get_songs(song_list)

    max_songs = 500 - fill_with_popular.get(len(song_list), 0)
    i = set()
    '''
    while len(recommendations) < max_songs and i < max(len(common_songs), len(popular_for_artists)):
        if i < len(common_songs) and common_songs[i][1] not in unique_recs:
            recommendations.append(common_songs[i][1])
            unique_recs.add(common_songs[i][1])
        if i < len(popular_for_artists) and popular_for_artists[i][1] not in unique_recs:
            recommendations.append(popular_for_artists[i][1])
            unique_recs.add(popular_for_artists[i][1])
        i += 1
    '''
    for i in range(len(common_songs)):
        recommendations.add(common_songs[i][1])
    for i in range(len(popular_for_artists)):
        recommendations.add(popular_for_artists[i][1])
    for i in range(len(most_popular_songs)):
        recommendations.add(most_popular_songs[i][1])

    for song in training_songs:
        if song in recommendations: matches += 1
    total += len(training_songs)
    total_recs += len(recommendations)
    count += 1
    if count % 1000 == 0: print count

print "percentage: " + str(float(matches)/ total)
print "average recs: " + str(float(total_recs)/ 4000)