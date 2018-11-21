#!/usr/bin/env python

import curses

stdscr = curses.initscr()

curses.noecho()
#curses.echo()


begin_x = 0
begin_y = 0
height = 10
width = 10
win = curses.newwin(height, width, begin_y, begin_x)
# tb = curses.textpad.Textbox(win)
# text = tb.edit()
# curses.addstr(4,1,'a'.encode('utf_8'))
# hw = "Hello world!"
# while 1:
#    c = stdscr.getch()
#    if c == ord('p'): pass
#    elif c == ord('q'): break # Exit the while()
#    elif c == curses.KEY_HOME: x = y = 0

curses.endwin()
help(stdscr)



# import curses
#
# window = curses.initscr()
# curses.noecho()
# # window.keypad(True)  # Maybe not perfect, but a good start?
# # kbhit
# window.kbhit
#
# curses.endwin()
# print(window)
