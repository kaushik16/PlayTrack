import json
import pickle
from collections import defaultdict

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

print "Loading Object Files..."
songsData=load_obj("Songs_Data")
challengeSet= load_obj("Challenge_Songs")
print "Loading Complete"

recommend={}
for k,v in challengeSet.iteritems():
    recommend[songsData[k]]=defaultdict(int)
for i in range(100,1100,100):
    current= load_obj("Recommended_Songs_"+str(i))
    for k,v in current.iteritems():
        for j in range(len(v)):
            recommend[k][v[j][1]]+=v[j][0]

print "Combination Done. Now Saving.."
for k,v in recommend.iteritems():
    print k,
    print v
save_obj(recommend, "Full_Recommend")


