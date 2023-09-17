import curses
from curses import wrapper
from threading import Thread
key = ""
curses.initscr()
print(f"curses-color:" + str(curses.COLS))
bufferString = ""

curses.init_pair(0, curses.COLOR_CYAN, curses.COLOR_BLACK)
def handleKeys(stdscr):
    global key
    key = stdscr.getkey()
    stdscr.clear()
    stdscr.addstr("grize-alpha0 :: key ? " + str(key) + " :: Welcome to Grize!", curses.color_pair(1))

def main(stdscr):
    global key
    print("start")
    stdscr.nodelay(True)
    while True:
        try:

            handleKeys(stdscr)

            if key == "/":
                break

        except curses.error:
            pass

wrapper(main)