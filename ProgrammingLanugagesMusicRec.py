import pandas as pd
from Song import Song
from User import User
import math

listOfUsers = []

defaultPlaylistPath = "DataFiles/playlist.csv"

def createListOfItems(pathName):
    df = pd.read_csv(pathName, on_bad_lines='skip')

    df = df.reset_index()
    
    listOfItems = []

    for index, row in df.iterrows():
    
        listOfItems.append(row)

    return createSongs(listOfItems)


def createSongs(listOfItems):
   

    listOfSongs = []
    listOfIDs = []
    listOfNames = []
    listOfCleanIDs = []
    listOfCleanNames = []

   


    for x in listOfItems:
        y = x.to_string()
        if(y.find("\"id\"") != -1):
            listOfIDs.append(y)
        if(y.find("\"name\"") != -1):
            listOfNames.append(y)


    idString = ""

    for x in listOfNames:
        x = x.split(":")
        x = x[1]
        x = x.replace("\"","")
        listOfCleanNames.append(x)
     

    for x in listOfIDs:
        x = x.split(":")
        x = x[1]
        x = x.replace("\"","")
        x = x.replace(" ", "")
        listOfCleanIDs.append(x)
        idString += x + ","


    for x in range(len(listOfNames)):
            listOfSongs.append(Song(listOfCleanNames[x], listOfCleanIDs[x],0))
        
        
    

    return listOfSongs


Luke = User(createListOfItems(defaultPlaylistPath),"Luke")
Luke.setLikedSongsFromFile("DataFiles/LukesSongs.txt")
listOfUsers.append(Luke)


Claudia = User(createListOfItems(defaultPlaylistPath),"Claudia")
Claudia.setLikedSongsFromFile('DataFiles/ClaudiasSongs.txt')
listOfUsers.append(Claudia)

Tri = User(createListOfItems(defaultPlaylistPath),"Tri")
Tri.setRandomLikedSongs()
listOfUsers.append(Tri)

Gordon = User(createListOfItems(defaultPlaylistPath),"Gordon")
Gordon.setRandomLikedSongs()
listOfUsers.append(Gordon)

for x in listOfUsers:
    x.initAverage()

def similarityRating(userOne, userTwo):

    simRating = 0

    dotproductNum = 0
    userOneDenom = 0
    userTwoDenom = 0

    userOneSongs = userOne.getListOfSongs()
    userTwoSongs = userTwo.getListOfSongs()

    for x in range(len(userOneSongs)):
        dotproductNum += (userOneSongs[x].getLiked() - userOne.getAverage()) * (userTwoSongs[x].getLiked() - userTwo.getAverage())
        userOneDenom += (userOneSongs[x].getLiked() - userOne.getAverage()) * (userOneSongs[x].getLiked() - userOne.getAverage())
        userTwoDenom += (userTwoSongs[x].getLiked() - userTwo.getAverage()) * (userTwoSongs[x].getLiked() - userTwo.getAverage())
        userOneDenom = math.sqrt(userOneDenom)
        userTwoDenom = math.sqrt(userTwoDenom)
       


    simRating = (dotproductNum / (userOneDenom * userTwoDenom)) 
    ###Because this is a binary function rather than a range of ratings for songs, we are stuck on a much larger bound than with range

    return simRating

def printRatings():
    for x in listOfUsers:
        for y in listOfUsers:
            if(x.getName() != y.getName()):
                print(x.getName() + " and " + y.getName() + " have a similarity rating of " + str(round(similarityRating(x,y),2)))
                

printRatings()