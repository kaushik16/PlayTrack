import pickle

class predictSongPair(object):


    def __init__(self):
        self.songMatrix=self.load_obj("Recommended_Songs_full")
        self.songsData =self.load_obj("Songs_Data")
        print "Recommendation Data Loaded for Song Pairs"

    def load_obj(self,name ):
        with open('obj/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)

    def save_obj(self, obj, name ):
        with open('obj/'+ name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


    def predict(self,songs):
        ans = []
        for song in range(len(songs)):
            if self.songMatrix.get(song,None)!=None:
                temp=[]
                pairs = self.songMatrix[song]
                sorted_pairs = sorted(pairs, key=lambda x: x[0], reverse=True)
                for idx in range(1,min(len(pairs),100)):
                    temp.append([sorted_pairs[idx][0],sorted_pairs[idx][1]])
                ans.append(temp)
            else:
                ans.append([])
        return ans
