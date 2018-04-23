import pickle

class RecommendSong(object):

    def load_obj(self,name ):
        with open('obj/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)

    def __init__(self):
        self.songMatrix=self.load_obj("Recommended_Songs_full")
        self.songsData =self.load_obj("Songs_Data")
        print "Recommendation Data Loaded for Song Pairs"

    def get_songs(self,songs):
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

        retVal = []
        for i in range(99):
            for j in range(len(ans)):
                if j < len(ans[j]): retVal.append(ans[j][i])
                if len(retVal) >= 500: break
            if len(retVal) >= 500: break
        return retVal
