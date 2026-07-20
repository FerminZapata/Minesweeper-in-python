import pygame,random,os

# HAY 3 MODOS DE JUEGO
# Tablero 9 x 9 con 10 minas -- easy
# Tablero 16 x 16 con 40 minas -- normal
# Tablero 32 x 32 con 99 minas -- hard

mode = "easy"

if mode == "easy":
    scale = 64
    boardsize = (9,9)
    mineamount = 10
    flagamout = 10
    flags = []
elif mode == "normal":
    scale = 36
    boardsize = (16,16)
    mineamount = 40
    flagamout = 40
    flags = []
elif mode == "hard":
    scale = 18
    boardsize = (32,32)
    mineamount = 99
    flagamout = 99
    flags = []
else:
    mode = "easy"
    scale = 64
    boardsize = (9,9)
    mineamount = 10
    flagamout = 10
    flags = []

height = 576
width = 576
Clock = pygame.time.Clock()

def create_board(): # Creates the board and the lines
    tablero = []
    minas = []
    for x in range(0,boardsize[1]):
        temp = []
        for i in range(0,boardsize[0]):
            temp.append(0)
        tablero.append(temp)
    for i in range(0,mineamount):
        while True:
            try:
                X = random.randint(0,boardsize[0]-1)
                Y = random.randint(0,boardsize[0]-1)
                if tablero[Y][X] == 9:
                    raise IndexError
            except Exception:
                continue
            else:
                rng = random.randint(0,1)
                if rng == 1:
                    break
        tablero[Y][X] = 9
        while i > 9:
            i -= 10
        if i == 0: # rojo anaranjado ig
            minas.append((X,Y,255,205,0))
        elif i == 1: # verde
            minas.append((X,Y,0,0,128))
        elif i == 2: # celeste
            minas.append((X,Y,30,136,229))
        elif i == 3: # naranja
            minas.append((X,Y,255,111,0))
        elif i == 4: # mustard
            minas.append((X,Y,255,179,0))
        elif i == 5: # purpura
            minas.append((X,Y,123,31,162))
        elif i == 6: # amarillo
            minas.append((X,Y,255,238,88))
        elif i == 7: # idk
            minas.append((X,Y,191,54,12))
        elif i == 8: # cyan
            minas.append((X,Y,0,172,193))
        elif i == 9: # rojo 
            minas.append((X,Y,216,27,96))
    return tablero, minas

def create_cover(): # Creates the cover
    tablero = []
    for x in range(0,boardsize[1]):
        temp = []
        for i in range(0,boardsize[0]):
            temp.append(0)
        tablero.append(temp)
    return tablero

def check_tiles(board, mines): #Adds the mines to the Board
    for tile in mines:
        for y in range(-1,2):
            for x in range(-1,2):
                try:
                    if tile[1]+y == -1 or tile[0]+x == -1:
                        raise IndexError
                    elif board[tile[1]+y][tile[0]+x] == 0:
                        board[tile[1]+y][tile[0]+x] = 1
                    elif board[tile[1]+y][tile[0]+x] != 9:
                        board[tile[1]+y][tile[0]+x] += 1
                except IndexError:
                    continue
    return board

board, mines = create_board()

cover = create_cover()

board = check_tiles(board,mines)

pygame.init()
Window = pygame.display.set_mode((width, height),)
pygame.display.set_caption("BuscaMIERDAS")
Window.fill("white")

def draw_board(): # draws the mines
    font = pygame.font.SysFont(None, scale)
    for y in range(0,boardsize[1]):
        for x in range(0,boardsize[0]):
            if y % 2 == 0 and x % 2 == 0:
                pygame.draw.rect(Window, (228,193,161), (x*scale,y*scale,scale,scale))
            elif y % 2 == 1 and x % 2 == 1:
                pygame.draw.rect(Window, (228,193,161), (x*scale,y*scale,scale,scale))
            else:
                pygame.draw.rect(Window, (215, 184, 153), (x*scale,y*scale,scale,scale))
            if board[y][x] == 9:
                for i in mines:
                    if i[0] == x and i[1] == y:
                        pygame.draw.rect(Window, (i[2], i[3], i[4]), (x*scale,y*scale,scale,scale))
                        color = [i[2]-30, i[3]-30, i[4]-30]
                        for i in range(0,3):
                            if color[i] < 0:
                                color[i] = 0
                        color = (color[0],color[1],color[2])
                        pygame.draw.circle(Window, color, (x*scale+scale/2,y*scale+scale/2),scale/4)
            elif board[y][x] != 0:
                if board[y][x] == 1:
                    color = (25,118,210)
                elif board[y][x] == 2:
                    color = (56,142,60)
                elif board[y][x] == 3:
                    color = (211,47,47)
                elif board[y][x] == 4:
                    color = (123,31,162)
                elif board[y][x] == 5:
                    color = (255,111,0)
                elif board[y][x] == 6:
                    color = (0,151,167)
                elif board[y][x] == 7:
                    color = (0,0,0)
                elif board[y][x] == 8:
                    color = (117,117,117)
                text = font.render(str(board[y][x]),True,color)
                Window.blit(text, (x*scale+scale/3,y*scale+scale/5))

def draw_cover(): # draws the cover of the mineland
    for y in range(0,boardsize[1]):
        for x in range(0,boardsize[0]):
            if cover[y][x] == 0 or cover[y][x] == 3:
                if y % 2 == 0 and x % 2 == 0:
                    pygame.draw.rect(Window, (171,216,89), (x*scale,y*scale,scale,scale))
                elif y % 2 == 1 and x % 2 == 1:
                    pygame.draw.rect(Window, (171,216,89), (x*scale,y*scale,scale,scale))
                else:
                    pygame.draw.rect(Window, (160,209,81), (x*scale,y*scale,scale,scale))
                if cover[y][x] == 3:
                    pygame.draw.rect(Window, (0,0,0), (x*scale+scale/8*2,y*scale+scale/4*3,scale/4,scale/16)) # base
                    pygame.draw.rect(Window, (0,0,0), (x*scale+scale/8*2.75,y*scale+scale/4,scale/16,scale - scale/2)) # pole
                    pygame.draw.rect(Window, (255,0,0), (x*scale+scale/8*3.25,y*scale+scale/4,scale/2.5,scale/3)) # red

def get_readable_data(x,y): # Turns mouse position into a position located in the grid
    while x % scale != 0:
        x -= 1
    while y % scale != 0:
        y -= 1
    x = int(x / scale)
    y = int(y / scale)
    return x,y

def show_all_zeros(x,y):
    used = []
    zero = [(x,y)]
    for Pos in zero:
        if Pos not in used:
            for Y in range(-1,2):
                for X in range(-1,2):
                    try:
                        if Pos[1]+Y < 0 or Pos[0]+X < 0:
                            raise IndexError
                        elif board[Pos[1]+Y][Pos[0]+X] == 0:
                            cover[Pos[1]+Y][Pos[0]+X] = 1
                            if (Pos[0]+X,Pos[1]+Y) not in used:
                                zero.append((Pos[0]+X,Pos[1]+Y))
                        else:
                            cover[Pos[1]+Y][Pos[0]+X] = 1
                    except IndexError:
                        continue
        used.append(Pos)
    return cover

def draw_end_screen(X):
    if X == 0:
        color = (0,0,0)
        font = pygame.font.SysFont(None, int(width/8))
        text = font.render("Ganaste w!",True,color)
        Window.blit(text, (width/3 - width/15,width/2 - width/25))
    elif X == 1:
        color = (0,0,0)
        font = pygame.font.SysFont(None, int(width/8))
        text = font.render("Perdiste w!",True,color)
        Window.blit(text, (width/3 - width/15,width/2 - width/25))

def check_end():
    if flagamout == 0:
        won = False
        for minepos in mines:
            won = False
            for flagpos in flags:
                if flagpos[0] == minepos[0] and flagpos[1] == minepos[1]:
                    won = True
                    break
            if won == False:
                break
        if won == False:
            return
        elif won == True:
            counter = 0
            for y in range(boardsize[1]):
                for x in range(boardsize[1]):
                    if cover[y][x] == 1:
                        counter += 1
            if counter == (boardsize[0]*boardsize[1]) - mineamount:
                draw_end_screen(0)

def update_flagcount():
    counter = 0
    for y in range(boardsize[1]):
        for x in range(boardsize[1]):
            if cover[y][x] == 3:
                counter += 1
    return 10 - counter

losed = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and losed == False:
            mouse_pos = pygame.mouse.get_pos()
            type = pygame.mouse.get_pressed(num_buttons=3)
            x = mouse_pos[0]
            y = mouse_pos[1]

            x, y = get_readable_data(x,y)

            if type[2] == True:
                if cover[y][x] == 0:
                    cover[y][x] = 3
                    flags.append((x,y))
                elif cover[y][x] == 3:
                    cover[y][x] = 0
                    flags.remove((x,y))
            elif type[0] == True:
                if cover[y][x] == 0:
                    cover[y][x] = 1
                    if board[y][x] == 0:
                        show_all_zeros(x,y)
                    elif board[y][x] == 9:
                        losed = True
    draw_board()
    if losed == False:
        draw_cover()
        check_end()
        os.system("cls")
        flagamout = update_flagcount()
        print("Flags lef:",flagamout)
    elif losed == True:
        draw_end_screen(1)
    pygame.display.update()
    Clock.tick(30)