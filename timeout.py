import queue as Queue
import curses
import threading
import datetime as dt

stdscr = curses.initscr()
stdscr.nodelay(1)

while True:
    k = stdscr.getch()
    stdscr.addstr('p')
    stdscr.addstr(str(k))
    stdscr.move(0,0)

curses.endwin()
# # help(stdscr)
