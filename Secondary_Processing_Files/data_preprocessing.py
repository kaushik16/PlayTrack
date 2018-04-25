import json
from pprint import pprint
import pickle

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

playlist_count=0
song_count=0
total_songs=0
songsData={}
playlistInfo = {}
start=0
for i in range(1000):
    end=start+999
    slice = json.load(open('/Users/Mragank/Desktop/mpd.v1/data/mpd.slice.'+str(start)+'-'+str(end)+'.json'))
    start=end+1


    for playlist in slice['playlists']:
        playlist_count+=1
        playlistInfo[playlist_count]={}
        playlistInfo[playlist_count]['name']=playlist['name']
        playlistInfo[playlist_count]['trackCount'] = playlist['num_tracks']
        playlistInfo[playlist_count]['followers'] = playlist['num_followers']
        playlistInfo[playlist_count]['tracks']=[]
        for song in playlist['tracks']:
            if songsData.get(song['track_uri'],None)==None:
                song_count += 1
                songsData[song['track_uri']]=song_count

            playlistInfo[playlist_count]['tracks'].append(song['track_uri'])

    print("Slice"+str(i)+"Parsed")
# pprint (playlistInfo)

#dump parsed data in file to prevent parsing again and again
save_obj(songsData,"Songs")
save_obj(playlistInfo, "Playlists")

