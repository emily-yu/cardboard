import curses

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    f=open("output.txt","w+")
    while True:
        # get keyboard input, returns -1 if none available
        c = int(stdscr.getch())
        if c != -1:
            f.write(chr(c))
            print(chr(c))
            # print numeric value
            stdscr.addstr(str(c) + ' ')
            stdscr.refresh()
            # return curser to start position
            stdscr.move(0, 0)

if _name_ == '_main_':
    curses.wrapper(main)
