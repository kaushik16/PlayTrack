from Load_Data import loadData

obj = loadData(False,False,True)
nearbyArtist=obj.near_Artist()


print "Linkin Park :" + ' ,'.join(nearbyArtist["Linkin Park"])
print "Miley Cyrus :" + ' ,'.join(nearbyArtist["Miley Cyrus"])
print "Akon :" + ' ,'.join(nearbyArtist["Akon"])
print "Adele :" + ' ,'.join(nearbyArtist["Adele"])
print "Maroon 5 :" + ' ,'.join(nearbyArtist["Maroon 5"])
print "Eminem :" + ' ,'.join(nearbyArtist["Eminem"])