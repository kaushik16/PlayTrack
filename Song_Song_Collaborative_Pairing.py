import json
import pickle
import pprint
from collections import defaultdict
import heapq
def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


start=0
songIndex=0
songMatrix={}
print "Loading Object Files..."
songsData=load_obj("Songs_Data")
print len(songsData)
challengeSet= load_obj("Challenge_Songs")
print "Loading Complete"

for i in range(1000):
    end=start+999
    with open('data/mpd.slice.'+str(start)+'-'+str(end)+'.json') as f:
        slice=json.load(f)
    start=end+1

    for playlist in slice['playlists']:
        for song in playlist['tracks']:
            index = songsData[song['track_uri']]
            if song['track_uri'] in challengeSet:
                if index not in songMatrix:
                    songMatrix[index]=defaultdict(int)
                for ssong in playlist['tracks']:
                    songMatrix[index][songsData[ssong['track_uri']]]+=1
    print("Slice"+str(i)+"Parsed")

recommendation={}
c=0

for song,value in challengeSet.iteritems():
    idx = songsData[song]
    recommendation[idx] = []
    if idx in songMatrix:
        for k,v in songMatrix[idx].iteritems():
            if len(recommendation[idx])<100:
                heapq.heappush(recommendation[idx],(v,k))
            elif recommendation[idx][0][0]<v:
                heapq.heappushpop(recommendation[idx],(v,k))
    c+=1
    if c%1000==0:
        print c
for k,v in recommendation.iteritems():
    print k,
    print v


print "Evaluation Done.now saving pickle"
save_obj(recommendation,"Recommended_Songs_100")
print "Pickle Saved"

with open('rec_data.json', 'w') as fp:
    json.dump(recommendation, fp)