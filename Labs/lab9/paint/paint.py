import pygame, sys, math, os
from random import randint

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

directory = 'Lab9/screenshots'
if not os.path.exists(directory):
    os.makedirs(directory)

finished = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

def drawRect(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)

def drawCircle(color, pos, x, y):
    rad = math.sqrt(x ** 2 + y ** 2)
    pygame.draw.circle(screen, color, pos, rad, 4)

def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)

def drawSquare(color, pos, side_length):
    pygame.draw.rect(screen, color, (pos[0], pos[1], side_length, side_length), 4)

def drawRightTriangle(color, start, end):    
    points = [(start[0], start[1]), (start[0], end[1]), (end[0], end[1])]
    pygame.draw.polygon(screen, color, points, 4)

def drawEquilateralTriangle(color, start, end):
    # c_x = (start[0] + end[0]) / 2
    # c_y = (start[1] + end[1]) / 2

    # r = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) * math.sqrt(3) / 3

    # x3 = c_x + r * math.cos(math.radians(120))
    # y3 = c_y + r * math.sin(math.radians(120))

    del_x = end[0] - start[0]
    del_y = end[1] - start[1]
    x3 = end[0] + del_x / 2 + math.sqrt(3)/2 * del_y
    y3 = end[1] + del_y / 2 + math.sqrt(3)/2 * del_x
    points = [(start[0], start[1]), (x3, y3), (end[0], end[1])]
    pygame.draw.polygon(screen, color, points, 4)

def drawRhombus(color, pos, x, y):
    half_x = x / 2
    half_y = y / 2
    points = [
        (pos[0] + half_x, pos[1]),
        (pos[0], pos[1] + half_y),
        (pos[0] + half_x, pos[1] + y),
        (pos[0] + x, pos[1] + half_y)
    ]
    
    
    
    pygame.draw.polygon(screen, color, points, 4)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y + 90)
    pygame.draw.rect(surface, WHITE, (textrect.topleft, (textrect.width + 50, textrect.height + 5)))
    surface.blit(textobj, textrect)

font = pygame.font.SysFont(None, 36)

RAD = 30

drawing = False
color = BLACK
previous_color = BLACK

screen.fill(pygame.Color('white'))
rainbow = pygame.image.load('color.jpg')
rainbow = pygame.transform.scale(rainbow, (100, 100))
start_pos = 0
end_pos = 0

tri_points = []
rhombus_points = []

mode = 0
# 0 - Rect
# 1 - Circle
# 2 - Eraser
# 3 - Pencil

mode_name = ['rect', 'circle', 'eraser', 'pencil', 'square', 'right tri', 'equil tri', 'rhombus']

img_cnt = 0

while not finished:
    clock.tick(FPS)

    pos = pygame.mouse.get_pos()
    screen.blit(rainbow, (0, 0))
    draw_text('Mode: ' + str(mode_name[mode]), font, BLACK, screen, 10, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mode == 4:
                tri_points = []  # Clear previous points for triangle
                rhombus_points = []
            drawing = True
            start_pos = pos
            if pos[0] > 20 and pos[0] < 100 and pos[1] > 20 and pos[1] < 100:
                color = screen.get_at(pos)
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pos
            rect_x = abs(start_pos[0] - end_pos[0])
            rect_y = abs(start_pos[1] - end_pos[1])

            if mode == 0:
                drawRect(color, start_pos, rect_x, rect_y)
            elif mode == 1:
                drawCircle(color, start_pos, rect_x, rect_y)
            elif mode == 4:
                side_length = max(rect_x, rect_y)
                drawSquare(color, start_pos, side_length)
            elif mode == 5:
                drawRightTriangle(color, start_pos, end_pos)
            elif mode == 6:
                side_length = min(rect_x, rect_y)
                drawEquilateralTriangle(color, start_pos, end_pos)
            elif mode == 7:
                drawRhombus(color, start_pos, rect_x, rect_y)
                

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == 2:
                eraser(pos, RAD)
            elif mode == 3:
                if start_pos:
                    pygame.draw.line(screen, color, start_pos, pos, 2)
                start_pos = pos

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mode += 1
                mode %= 8
                if mode == 2:
                    previous_color = color
                    color = WHITE
                else:
                    color = previous_color
            if event.key == pygame.K_BACKSPACE:
                screen.fill(pygame.Color('white'))

            if event.key == pygame.K_s:
                pygame.image.save(screen, f'{directory}/photo{img_cnt}.jpg')
                img_cnt += 1     

    pygame.display.flip()

pygame.quit()
sys.exit()
