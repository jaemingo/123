import random
import sys
import time

import pygame
from pygame.locals import *

FPS = 5000
상자크기 = 640
높이 = 480
게임상자 = 20
게임상자가로 = 10
게임상자세로 = 20
BLANK = 'ㅋ'

MOVESIDEWAYSFREQ = 5
MOVEDOWNFREQ = 2

XMARGIN = int((상자크기 - 게임상자가로 * 게임상자) / 2)
TOPMARGIN = 높이 - (게임상자세로 * 게임상자) - 5

#        (빨강 ,초록, 파랑)
WHITE = (255, 255, 255)
GRAY = (185, 185, 185)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
LIGHTRED = (175, 20, 20)
GREEN = (0, 155, 0)
LIGHTGREEN = (20, 175, 20)
BLUE = (0, 0, 155)
LIGHTBLUE = (20, 20, 175)
YELLOW = (155, 155, 0)
LIGHTYELLOW = (175, 175, 20)

BORDERCOLOR = LIGHTBLUE
BGCOLOR = WHITE
TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = GRAY
COLORS = (BLUE, GREEN, RED, YELLOW)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

S_SHAPE_TEMPLATE = [['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ',
                     'ㅋㅋOOㅋ',
                     'ㅋOOㅋㅋ',
                     'ㅋㅋㅋㅋㅋ'],
                    ['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋOㅋㅋ',
                     'ㅋㅋOOㅋ',
                     'ㅋㅋㅋOㅋ',
                     'ㅋㅋㅋㅋㅋ']]

Z_SHAPE_TEMPLATE = [['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ',
                     'ㅋOOㅋㅋ',
                     'ㅋㅋ00ㅋ',
                     'ㅋㅋㅋㅋㅋ'],
                    ['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋ00ㅋㅋ',
                     'ㅋ0ㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ']]

I_SHAPE_TEMPLATE = [['ㅋㅋ0ㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋㅋㅋㅋ'],
                    ['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ',
                     '0000ㅋ',
                     'ㅋㅋㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ']]

O_SHAPE_TEMPLATE = [['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ',
                     'ㅋ00ㅋㅋ',
                     'ㅋ00ㅋㅋ',
                     'ㅋㅋㅋㅋㅋ']]

J_SHAPE_TEMPLATE = [['ㅋㅋㅋㅋㅋ',
                     'ㅋ0ㅋㅋㅋ',
                     'ㅋ000ㅋ',
                     'ㅋㅋㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ'],
                    ['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋ00ㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋㅋㅋㅋ'],
                    ['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ',
                     'ㅋ000ㅋ',
                     'ㅋㅋㅋ0ㅋ',
                     'ㅋㅋㅋㅋㅋ'],
                    ['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋ00ㅋㅋ',
                     'ㅋㅋㅋㅋㅋ']]

L_SHAPE_TEMPLATE = [['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋㅋ0ㅋ',
                     'ㅋ000ㅋ',
                     'ㅋㅋㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ'],
                    ['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋ00ㅋ',
                     'ㅋㅋㅋㅋㅋ'],
                    ['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ',
                     'ㅋ000ㅋ',
                     'ㅋ0ㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ'],
                    ['ㅋㅋㅋㅋㅋ',
                     'ㅋ00ㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋㅋㅋㅋ']]

T_SHAPE_TEMPLATE = [['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋ000ㅋ',
                     'ㅋㅋㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ'],
                    ['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋ00ㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋㅋㅋㅋ'],
                    ['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋㅋㅋㅋ',
                     'ㅋ000ㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋㅋㅋㅋ'],
                    ['ㅋㅋㅋㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋ00ㅋㅋ',
                     'ㅋㅋ0ㅋㅋ',
                     'ㅋㅋㅋㅋㅋ']]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}


def aa():
    global 프레임시간, 화면, 기본글자, 큰글자
    pygame.init()
    프레임시간 = pygame.time.Clock()
    화면 = pygame.display.set_mode((상자크기, 높이))
    기본글자 = pygame.font.Font(None, 30)
    큰글자 = pygame.font.Font(None, 200)
    pygame.display.set_caption('game')

    while True:
        bb()


def bb():
    global 시간
    board = kk()
    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    movingDown = False
    왼쪽으로 = False
    movingRight = False
    r = 0
    level, fall = hh(r)

    떨어지는조각 = ii()
    다음조각 = ii()

    while True:
        if 떨어지는조각 is None:
            떨어지는조각 = 다음조각
            다음조각 = ii()
            lastFallTime = time.time()

            if not nn(board, 떨어지는조각):
                return

        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_p:
                    화면.fill(BGCOLOR)
                    lastFallTime = time.time()
                    lastMoveDownTime = time.time()
                    lastMoveSidewaysTime = time.time()
                elif event.key == K_LEFT:
                    왼쪽으로 = False
                elif event.key == K_RIGHT:
                    movingRight = False
                elif event.key == K_DOWN:
                    movingDown = False

            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and nn(board, 떨어지는조각, adjX=-1):
                    떨어지는조각['x'] -= 1
                    왼쪽으로 = True
                    movingRight = False
                    lastMoveSidewaysTime = time.time()

                elif (event.key == K_RIGHT or event.key == K_d) and nn(board, 떨어지는조각, adjX=1):
                    떨어지는조각['x'] += 1
                    movingRight = True
                    왼쪽으로 = False
                    lastMoveSidewaysTime = time.time()

                elif event.key == K_UP:
                    떨어지는조각['rotation'] = (떨어지는조각['rotation'] + 1) % len(PIECES[떨어지는조각['shape']])
                    if not nn(board, 떨어지는조각):
                        떨어지는조각['rotation'] = (떨어지는조각['rotation'] - 1) % len(PIECES[떨어지는조각['shape']])
                elif event.key == K_q:
                    떨어지는조각['rotation'] = (떨어지는조각['rotation'] - 1) % len(PIECES[떨어지는조각['shape']])
                    if not nn(board, 떨어지는조각):
                        떨어지는조각['rotation'] = (떨어지는조각['rotation'] + 1) % len(PIECES[떨어지는조각['shape']])

                elif event.key == K_DOWN:
                    movingDown = True
                    if nn(board, 떨어지는조각, adjY=1):
                        떨어지는조각['y'] += 1
                    lastMoveDownTime = time.time()

                elif event.key == K_SPACE:
                    movingDown = False
                    왼쪽으로 = False
                    movingRight = False
                    for 시간 in range(1, 게임상자세로):
                        if not nn(board, 떨어지는조각, adjY=시간):
                            break
                    떨어지는조각['y'] += 시간 - 1

        if (왼쪽으로 or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if 왼쪽으로 and nn(board, 떨어지는조각, adjX=-1):
                떨어지는조각['x'] -= 1
            elif movingRight and nn(board, 떨어지는조각, adjX=1):
                떨어지는조각['x'] += 1
            lastMoveSidewaysTime = time.time()

        if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and nn(board, 떨어지는조각, adjY=1):
            떨어지는조각['y'] += 1
            lastMoveDownTime = time.time()

        if time.time() - lastFallTime > fall:
            if not nn(board, 떨어지는조각, adjY=1):
                jj(board, 떨어지는조각)
                r += oo(board)
                level, fall = hh(r)
                떨어지는조각 = None
            else:
                떨어지는조각['y'] += 1
                lastFallTime = time.time()

        화면.fill(BGCOLOR)
        rr(board)
        tt(다음조각)
        if 떨어지는조각 is not None:
            ss(떨어지는조각)
        pygame.display.update()
        프레임시간.tick(FPS)


def dd():
    pygame.quit()
    sys.exit()


def ee():

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None

    while ee() is None:
        pygame.display.update()
        프레임시간.tick()


def gg():
    for _ in pygame.event.get(QUIT):
        dd()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            dd()
        pygame.event.post(event)


def hh(r):
    level = int(r / 10) + 1
    fallFreq = 0.27 - (level * 0.02)
    return level, fallFreq


def ii():
    shape = random.choice(list(PIECES.keys()))
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(PIECES[shape]) - 1),
                'x': int(게임상자가로 / 2) - int(TEMPLATEWIDTH / 2),
                'y': -2,
                'color': random.randint(0, len(COLORS) - 1)}
    return newPiece


def jj(board, piece):
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']


def kk():
    board = []
    for ㅈ in range(게임상자가로):
        board.append([BLANK] * 게임상자세로)
    return board


def ll(x, y):
    return 0 <= x < 게임상자가로 and y < 게임상자세로


def nn(board, piece, adjX=0, adjY=0):
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            isAboveBoard = y + piece['y'] + adjY < 0
            if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            if not ll(x + piece['x'] + adjX, y + piece['y'] + adjY):
                return False
            if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                return False
    return True


def mm(안돼, y):
    for x in range(게임상자가로):
        if 안돼[x][y] == BLANK:
            return False
    return True


def oo(판):
    가로줄완성 = 0
    y = 게임상자세로 - 1
    while y >= 0:
        if mm(판, y):
            for 하강 in range(y, 0, -1):
                for 좌우 in range(게임상자가로):
                    판[좌우][하강] = 판[좌우][하강 - 1]
            for 좌우 in range(게임상자가로):
                판[좌우][0] = BLANK
            가로줄완성 += 1
        else:
            y -= 1
    return 가로줄완성


def pp(상자x, 상자y):
    return (XMARGIN + (상자x * 게임상자)), (TOPMARGIN + (상자y * 게임상자))


def qq(boxx, boxy, color, pixelx=None, pixely=None):
    if color == BLANK:
        return
    if pixelx is None and pixely is None:
        pixelx, pixely = pp(boxx, boxy)
    pygame.draw.rect(화면, COLORS[color], (pixelx + 1, pixely + 1, 게임상자 - 1, 게임상자 - 1))
    pygame.draw.rect(화면, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, 게임상자 - 4, 게임상자 - 4))


def rr(board):
    pygame.draw.rect(화면, BORDERCOLOR,
                     (XMARGIN - 3, TOPMARGIN - 7, (게임상자가로 * 게임상자) + 8, (게임상자세로 * 게임상자) + 8), 5)

    pygame.draw.rect(화면, BGCOLOR, (XMARGIN, TOPMARGIN, 게임상자 * 게임상자가로, 게임상자 * 게임상자세로))
    for x in range(게임상자가로):
        for y in range(게임상자세로):
            qq(x, y, board[x][y])


def ss(piece, pixelx=None, pixely=None):
    shapeToDraw = PIECES[piece['shape']][piece['rotation']]
    if pixelx is None and pixely is None:
        pixelx, pixely = pp(piece['x'], piece['y'])

    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if shapeToDraw[y][x] != BLANK:
                qq(None, None, piece['color'], pixelx + (x * 게임상자), pixely + (y * 게임상자))


def tt(piece):
    nextSurf = 기본글자.render('Next:', True, TEXTCOLOR)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (상자크기 - 120, 80)
    화면.blit(nextSurf, nextRect)
    ss(piece, pixelx=상자크기 - 220, pixely=300)


if __name__ == '__main__':
    aa()
