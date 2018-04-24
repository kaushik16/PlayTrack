import pickle

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

class RecommendPopular(object):
    def __init__(self):
        self.most_popular = load_obj('MostPopularSongs_1000')
        self.most_popular_by_artist = load_obj('MostPopularSongsByArtist_100')

    def get_most_popular(self):
        return self.most_popular[:650]

    def get_most_popular_by_artist(self, artists):
        combined_songs = []
        for artist in artists:
            if artist in self.most_popular_by_artist:
                combined_songs.append(self.most_popular_by_artist[artist])

        retVal = []
        for i in range(len(combined_songs[0])):
            for j in range(len(combined_songs)):
                if i < len(combined_songs[j]):
                    retVal.append(combined_songs[j][i])
                    if len(retVal) >= 500: break
            if len(retVal) >= 500: break

        return retVal
