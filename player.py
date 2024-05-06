from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0

        #Important
        #Nếu muốn tốc độ di chuyển của người chơi độc lập với 
        #tốc độ khung hình thì cần sử dụng delta time để lấy cho mỗi khung hình

        #delta time là khoảng thời gian giữa khung hình cuối cùng và khung hình hiện tại

        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a


        #Tạo cái phím di chuyển
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.x += dx
        self.y += dy

        #Áp dụng để quay bằng phím left và right
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

        #tau = 2pi 
        # Đây thường được sử dụng để đảm bảo rằng góc hướng được biểu diễn trong khoảng từ 0 đến 2π



    #Hàm draw được sử dụng để vẽ người chơi lên màn hình của trò chơi
    def draw(self):
        #Hàm line để vẽ đường thẳng đại diện cho hướng nhìn của người chơi
        pg.draw.line(self.game.screen, #
                    'yellow',
                    (self.x * 50, self.y * 50), #Điểm bắt đầu của đường thẳng,
                     #vị trí của người chơi trên màn hình.
                     # Vị trí này được nhân với 50 để chuyển đổi từ tọa độ logic sang tọa độ pixel trên màn hình
                    (self.x * 50 + WIDTH * math.cos(self.angle), self.y * 50 + WIDTH * math. sin(self.angle)),
                    2)

        pg.draw.circle(self.game.screen, 'green', (self.x * 50, self.y * 50), 15)


    def update(self):
        self.movement()


    #Tạo 2 thuộc tính cho player 
    #pos:
    #Phương thức này trả về một bộ (tuple) chứa tọa độ x và y của người chơi
    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)