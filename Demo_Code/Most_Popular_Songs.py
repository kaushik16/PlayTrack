from Load_Data import loadData

obj = loadData(True,False,False)
mostPopularSongs= obj.mps()
songsData=obj.songData()
uritoname=obj.uri_name()

print "Most Popular Songs in Spotify Dataset"
revsongsData= {v:k for k,v in songsData.items()}
for i in range(25):
    print uritoname[revsongsData[mostPopularSongs[i][1]-1]]

