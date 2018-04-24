from Load_Data import loadData

obj = loadData(False,True,False)
mostPopularSongsWithArtist= obj.mpswa()
songsData=obj.songData()
uritoname=obj.uri_name()
count=0
revsongsData= {v:k for k,v in songsData.items()}


print "Most Popular Songs by every Artist"
print "----------------------------------"
artists= ["Linkin Park","Miley Cyrus","Akon","Adele","Maroon 5","Eminem"]
for artist in artists:
    print artist+" : ",
    for i in range(25):
        print uritoname[revsongsData[mostPopularSongsWithArtist[artist][i][1]-1]],
        print ",",
    print

