import curses
import random
import time

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(False)
stdscr.keypad(True)
stdscr.nodelay(True)

maxl = curses.LINES -1
maxc = curses.COLS -1
score = 0
world = []

player_l = player_c = 0
player_char = u"\u2639"
food_char = "🍍"
enemy_char = "⛄"
food = []
enemy = []
def random_place():
    a = random.randint(0,maxl)
    b = random.randint(0,maxc)
    while world[a][b] != ' ':
        a = random.randint(0,maxl)
        b = random.randint(0,maxc)

    return a ,b

def check_food():
    global score
    for i in range(len(food)):
        fl, fc, fa  = food[i]
        fa -=1
        if fl == player_l and fc == player_c:
            score+=10
            fl,fc = random_place()
            fa = random.randint(1000,10000)
        if fa <= 0:
            fl,fc = random_place()
            fa = random.randint(1000,10000)
        food[i] = (fl,fc,fa)

def init():
    global player_c,player_l
    for i in range(-1, maxl+1):
        world.append([])
        for j in range(-1, maxc+1):
            world[i].append(" " if random.random() > 0.1 else '.')

    for i in range(10):
        fl,fc = random_place()
        fa = random.randint(1000,10000)
        food.append((fl, fc, fa))

    for i in range(3):
        el, ec =random_place()
        enemy.append((el,ec))
    
    player_l,player_c = random_place()

def in_range(a, min, max):  
    if a > max:
        return max 
    if a < min:
        return min
    return a

def draw():
    
    
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i,j, world[i][j])
    stdscr.addstr(1,1,f"score:{score}")
    # showing the food
    for f in food :
        fl,fc,fa = f
        stdscr.addch(fl,fc,food_char)

    for e in enemy :
        el,ec = e
        stdscr.addch(el,ec,enemy_char)
    
    # showing the player
    stdscr.addch(player_l,player_c,player_char)
    stdscr.refresh()  

def move(c):
    global player_l,player_c
    if c == 'w' and world[player_l-1][player_c] != '.':
        player_l -= 1
    elif c == 's'  and world[player_l+1][player_c] != '.':
        player_l += 1
    elif c == 'a' and world[player_l][player_c-1] != '.':
        player_c -=1
    elif c== 'd' and world[player_l-1][player_c+1] != '.':
        player_c +=1
    
    player_l = in_range(player_l,0,maxl-1)
    player_c = in_range(player_c,0,maxc-1)

def move_enemy():
    global playing
    for i in range(len(enemy)):
        l,c = enemy[i]
        if random.random()>0.8:
            l += random.choice([0, 1, -1])
            c += random.choice([0, 1, -1])
            l = in_range(l,0 ,maxl -1)
            c = in_range(c,0, maxc -1)
            enemy[i] = (l,c)
        if l == player_l and c ==player_c:
            stdscr.addstr(maxl//2,maxc//2, "you died!")
            stdscr.refresh()
            time.sleep(3)
            playing = False


init()
playing = True
while playing:
    try :
        c = stdscr.getkey()
    except :
        c = ''
    if c in 'asdw':
        move(c)
    elif c == 'q':
        playing = False

    check_food()
    move_enemy()
    time.sleep(0.1)
    draw()


stdscr.clear()
stdscr.refresh()
