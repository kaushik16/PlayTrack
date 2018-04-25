import pickle
import numpy as np

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

songMatrix = load_obj("Song_Matrix")
print "Loaded"
print len(songMatrix)

def predict(songs):
    ans = []
    for song in range(len(songs)):
        if songMatrix.get(song,None)!=None:
            temp=[]
            pairs = songMatrix[song]
            sorted_pairs = sorted(pairs.items(), key=lambda x: x[1], reverse=True)
            for idx in range(min(len(pairs),100)):
                temp.append(sorted_pairs[idx][0])
            ans.append(temp)
        else:
            ans.append([])
    return ans
