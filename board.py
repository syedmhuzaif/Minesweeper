import random
from tile import Tile
from point import Point

class Board(object):
    def __init__(self,size,numMines):
        self.size = size
        self.numMines = numMines
        self.gameState = "NotStarted"
        self.setBoard()
    
    def setBoard(self):
        self.tiles = []
        self.arrayedTiles = []
        for i in range(0,self.size[0]):
            for j in range(0,self.size[1]):
                self.tiles.append(Tile(False,Point(i,j)))
        
        for i in range(0,self.size[0]):
            row = []
            for j in range(0,self.size[1]):
                for t in self.tiles:
                    if t.coordinates == Point(i,j):
                        row.append(t)
            self.arrayedTiles.append(row)
        
        print("Check! Check!...")
        for i in self.tiles:
                i.CheckTilesAround(self.arrayedTiles)
        print("board set!!!")
        

    def setMines(self,firstClicked):
        tileSet = set(self.tiles) - set(firstClicked.tilesAround) - set([firstClicked])
        self.mines = random.sample(list(tileSet),self.numMines)
        
        self.gameState = "OnGoing"
        
        for i in self.tiles:
            for j in self.mines:
                if(i.coordinates == j.coordinates):
                    i.isMine = True
                    i.name = "Mine"
        
        for i in self.tiles:
                i.CheckMinesAround()
                
        print("mines set!!!")

    def ClearTiles(self,tile):

        tile.isClear = True
        if tile.minesAround == 0:
            for t in tile.tilesAround:
                if not t.isClear:
                    self.ClearTiles(t)


    def setGameState(self,state):
        self.gameState = state