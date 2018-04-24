import pickle

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

class RecommendArtist(object):
    def __init__(self):
        self.closest_artists = load_obj('NearestArtists_reduced')

    def get_nearest_artists(self, artist_list):
        combined_artists = []
        for artist in artist_list:
            if artist in self.closest_artists:
                combined_artists.append(self.closest_artists[artist])

        retVal = []
        if len(combined_artists) > 0:
            for i in range(len(combined_artists[0])):
                for j in range(len(combined_artists)):
                    retVal.append(combined_artists[j][i])

        if len(retVal) > 100: return retVal[:100]
        return retVal