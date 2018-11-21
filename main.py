import time
from Ascii import *

class Player(Sprite):
    def update(self, screen, key):
        key = char(key).lower()
        if key == 'w':
            self.move(0, -1)
        if key == 's':
            self.move(0, 1)
        if key == 'a':
            self.move(-1, 0)
        if key == 'd':
            self.move(1, 0)


class Enemy(Sprite):
    last_move = 0
    last_time = time.time()
    def update(self, screen, key):
        if time.time() - self.last_time > 0.2:
            if self.last_move == 0:
                self.last_move = 1
                self.move(0, 1)
            elif self.last_move == 1:
                self.last_move = 2
                self.move(-1, 0)
            elif self.last_move == 2:
                self.last_move = 3
                self.move(0, -1)
            elif self.last_move == 3:
                self.last_move = 0
                self.move(1, 0)
            self.last_time = time.time()


s = Screen(blocking=False)
s.append(Player(1, 1, "$"))
s.append(Enemy(10, 10, "E"))

def f(key):
    for sprite in s:
        sprite.update(s, key)
    s.update()

run(f)
