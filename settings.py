#Lưu trữ các cài đặt của trò chơi

import math

RES = WIDTH, HEIGHT = 800, 450
FPS = 0

#Setting khởi tạo cho player

PLAYER_POS = 1.5, 5  # mini_map lần đầu xuất hiện
PLAYER_ANGLE = 0 #góc nhìn nhân vật
PLAYER_SPEED = 0.004 #tốc độ di chuyển
PLAYER_ROT_SPEED = 0.002 #tốc độ quay rotation


#Xác định hướng nhìn của nhân vật

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20