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
        pg.display.flip() #Cập nhật màn hình với những thay đổi đã được vẽ.
        self.clock.tick(FPS) # Điều chỉnh tốc độ của trò chơi để đảm bảo rằng nó chạy với FPS mong muốn.
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()