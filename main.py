import pygame
import os
from tile import Tile
from point import Point
from board import Board
import random

x = int(input("Enter the number of columns: "))
y = int(input("Enter the number of rows: "))
numMines = int(input("Enter the number of mines: "))
boardSize = (x,y)
board = Board(boardSize,numMines)



BGColor = (38,50,56)
FPS = 60

border = 8
tileSize = 32
winWidth = x*tileSize + border*2
winHeight = y*tileSize + border*2
pygame.display.set_caption("Minesweeper")
pygame.display.set_icon(pygame.image.load('Assets/icon.png'))
win = pygame.display.set_mode((winWidth,winHeight))

def loadImages():
    images = {}
    for fileName in os.listdir("Assets"):
        if (not fileName.endswith(".png")):
            continue
        image = pygame.image.load(os.path.join("Assets",fileName))
        image = pygame.transform.scale(image,(tileSize,tileSize))
        images[fileName.split(".")[0]] = image
    return images

images = loadImages()


def draw():
    win.fill(BGColor)
    for t in board.tiles:
        if t.isFlagged and not (t.isMine and board.gameState == "lost" or t.isClear):
            image = images["flag"]
        elif not t.isMine and t.isClear and not t.isFlagged:
            image = images[str(t.minesAround)]
        else:
            if not t.isMine and not t.isClear:
                image = images["tile"]
            elif t.isMine and board.gameState == "lost":
                image = images["bomb"]
            else:
                image = images["tile"]
            
        tilePos = (tileSize*(t.coordinates.x) + border, tileSize*(y-t.coordinates.y-1) + border)
        win.blit(image,tilePos)


def handleClick(mousePos,Click):
    print("Called handleClick()")
    retTilePos = ((mousePos[0]-border)//tileSize, y-1-(mousePos[1]-border)//tileSize)
    if not (retTilePos[0] in range(0,x) and retTilePos[1] in range(0,y)):
        return
    tilePoint = Point(retTilePos[0],retTilePos[1])

    for t in board.tiles:
        if t.coordinates == tilePoint:
            if board.gameState == "lost":
                return
            if Click[0]:
                if board.gameState == "NotStarted":
                    board.setMines(t)
                if not t.isFlagged:
                    if not t.isMine:
                        print(f'Clicked on {t.name} {tilePoint}')
                        board.ClearTiles(t)
                    else:
                        print(f'Clicked on {t.name} {tilePoint}')
                        board.setGameState("lost")
            elif Click[2]:
                t.isFlagged = not t.isFlagged if not t.isClear else t.isFlagged

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Click = pygame.mouse.get_pressed()
                mousePos = pygame.mouse.get_pos()
                handleClick(mousePos,Click)
        draw()

        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
