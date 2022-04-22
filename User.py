import random
class User(object):
    """Holds a user and their liked songs"""

    def __init__(self, listOfSongs, name):
        self.listOfSongs = listOfSongs
        self.name = name
        self.ratingAverage = -1

    def getName(self):
        return self.name

    def getListOfSongs(self):
        return self.listOfSongs

    def initAverage(self):
        likedSum = 0
        for x in self.listOfSongs:
            likedSum += x.getLiked()

        self.ratingAverage = likedSum / len(self.listOfSongs)

    def printSongs(self):
        for x in self.listOfSongs:
            if(x.getLiked() == 1):
                print(self.name + "likes " + x.getName())
            else:
                print(self.name + " does not like " + x.getName())

    def getAverage(self):
        return self.ratingAverage

    def setLikedSongsFromFile(self,filepath):
        file = open(filepath,"r")
        
        for x in self.listOfSongs:
            x.setLiked(int(file.readline()))

        file.close()

    def setRandomLikedSongs(self):
         for x in self.listOfSongs:
            x.setLiked(random.randrange(2) + 1)