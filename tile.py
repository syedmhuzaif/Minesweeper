from point import Point
class Tile (object):
    def __init__(self,isMine,coordinates):
        self.isMine = isMine
        self.isClear = False
        self.isFlagged = False
        self.name = "Tile"
        self.coordinates = coordinates
    def CheckTilesAround(self,tilelist):
        self.tilesAround = []
        for i in range(-1,2):
            for j in range(-1,2):
                if self.coordinates.x + i in range(0,len(tilelist)) and self.coordinates.y + j in range(0,len(tilelist[0])) and not(i == 0 and j ==0):
                    self.tilesAround.append(tilelist[self.coordinates.x + i][self.coordinates.y + j])

    def CheckMinesAround(self):
        count = 0
        self.minesList = []
        for k in self.tilesAround:
            for i in range(-1,2):
                for j in range(-1,2):
                    if (k.coordinates == self.coordinates + Point(i,j) and Point(i,j)!=Point(0,0)):
                        if k.isMine == True:
                            self.minesList.append(k)
                            count = count + 1
        self.minesAround = count
        