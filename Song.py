class Song(object):
    """stores song information"""

    def __init__(self, name, id, liked):
        self.name = name
        self.id = id
        self.liked = liked

    def getName(self):
        return self.name

    def getID(self):
        return self.id
    
    def getLiked(self):
        return self.liked

    def setLiked(self, liked):
        self.liked = liked

