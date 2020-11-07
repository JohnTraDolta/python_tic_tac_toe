import time

import pygame as pg
from pygame import display


class Game:
    def __init__(self):
        self.ScreenX = 600
        self.ScreenY = 600
        self.display = pg.display.set_mode((self.ScreenX, self.ScreenY))
        self.IsCrossTurn = False

    def PlaceMaker(self, ClickX, ClickY, Mark):
        font = pg.font.Font('NotoSansJP-Regular.otf', 100)
        text = font.render(Mark, True, "#ffffff", "#000000")
        textRect = text.get_rect()

        X1 = 100
        if ClickX < 200:
            X1 = 100
        elif ClickX > 200 and ClickX < 400:
            X1 = 300
        elif ClickX > 400:
            X1 = 500
        Y1 = 100
        if ClickY < 200:
            Y1 = 100
        elif ClickY > 200 and ClickY < 400:
            Y1 = 300
        elif ClickY > 400:
            Y1 = 500
        textRect.center = (X1, Y1)
        self.display.blit(text, textRect)
        pg.display.update()

    def Run(self):

        pg.init()

        done = False

        self.display.fill("#AA0000")
        pg.display.update()
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True

            if pg.mouse.get_pressed()[0]:
                if self.IsCrossTurn:
                    x, y = pg.mouse.get_pos()
                    print("x: " + str(x) + " y: "+str(y))
                    self.PlaceMaker(x, y, "X")
                    self.IsCrossTurn = False
                    time.sleep(1)
                elif not self.IsCrossTurn:
                    x, y = pg.mouse.get_pos()
                    print("x: " + str(x) + " y: "+str(y))
                    self.PlaceMaker(x, y, "O")
                    self.IsCrossTurn = True
                    time.sleep(1)
                # pg.display.update()


spil = Game()
spil.Run()
