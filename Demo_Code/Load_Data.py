import pickle

class loadData(object):

    def __init__(self,a=False,b=False,c=False):
        self.songsData=self.load_obj("Songs_Data")
        self.uritoname = self.load_obj("SongURI_to_SongName")

        if a:
            self.mostPopularSongs=self.load_obj("MostPopularSongs_1000")
        if b:
            self.mostPopularSongsByArtist=self.load_obj("MostPopularSongsByArtist_100")
        if c:
            self.nearbyArtist = self.load_obj("NearestArtists_20")


    def load_obj(self,name ):
        with open('../obj/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)


    def mps(self):
        return self.mostPopularSongs

    def mpswa(self):
        return self.mostPopularSongsByArtist

    def songData(self):
        return self.songsData

    def uri_name(self):
        return self.uritoname

    def near_Artist(self):
        return self.nearbyArtist