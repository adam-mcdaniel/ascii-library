import sys, os
import curses, time
from threading import Thread
from collections import deque

block_getch = False
stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
curses.cbreak()

def char(c):
    try:
        return chr(c)
    except:
        return "-1"


class Sprite:
    def __init__(self, x, y, symbol):
        self.x, self.y = x, y
        self.symbol = symbol

    def update(self, *args):
        pass

    def move(self, dx, dy):
        stdscr.move(self.y, self.x)
        stdscr.addch(' ')
        self.x += dx
        self.y += dy
        self.draw()

    def goto(self, x, y):
        stdscr.move(self.y, self.x)
        stdscr.addch(' ')
        self.x, self.y = x, y
        self.draw()

    def draw(self):
        stdscr.move(self.y, self.x)
        stdscr.addch(self.symbol)

class Screen(deque):
    def __init__(self, blocking=False):
        global block_getch
        if not blocking:
            stdscr.nodelay(1)

    def update(self):
        list(map(lambda s: s.draw, self))

    def get_key():
        return stdscr.getch()

def run(f):
    while True:
        c = Screen.get_key()
        f(c)
