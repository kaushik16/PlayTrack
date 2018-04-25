import json
import pickle

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

challengeSongs={}
with open('/Users/Mragank/Desktop/challenge.v1/challenge_set.json') as f:
    slice = json.load(f)
    for playlist in slice['playlists']:
        for song in playlist['tracks']:
            challengeSongs[song['track_uri']]=True

print(len(challengeSongs))
save_obj(challengeSongs,"Challenge_Songs")
print "Challenge Set Pickled"
