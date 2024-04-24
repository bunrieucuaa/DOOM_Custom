import pygame as pg
import sys #thu vien builtin cua python
from settings import *


class Game:
    def __init__(self):
        pg.init() #Khởi tạo game
        self.screen = pg.display.set_mode(RES) #Tạo một cửa sổ trò chơi với kích thước được định nghĩa ở setting
        self.clock = pg.time.Clock() #Khởi tạo một đối tượng clock để theo dõi thời gian trong trò chơi


    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)