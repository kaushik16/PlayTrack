from Load_Data import loadData
import pickle


def load_obj( name):
    with open('../obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

obj = loadData(False,False,False)
uritoname=obj.uri_name()
songsData=obj.songData()
revsongsData= {v:k for k,v in songsData.items()}
songMatrix=load_obj("Recommended_Songs_full")
names=["In The End by Linken Park","Party In The U.S.A. by Miley Cyrus", "Hello by Adele","Sugar by Maroon 5","Loose yourself by Eminem"]
songs=["spotify:track:60a0Rd6pjrkxjPbaKzXjfq","spotify:track:5Q0Nhxo0l2bP3pNjpGJwV1","spotify:track:4sPmO7WMQUAf45kwMOtONw","spotify:track:494OU6M7NOf4ICYb4zWCf5","spotify:track:7w9bgPAmPTtrkt2v16QWvQ"]
for i in range(len(songs)):
    print names[i]+" : ",
    pairs=songMatrix[songsData[songs[i]]]
    for j in range(25):
        print uritoname[revsongsData[pairs[j][1]]],
        print ",",
    print
