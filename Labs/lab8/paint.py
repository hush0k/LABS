import pygame

shape = ['circle', 'rectangles']


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    eraser_points = []
    points = []
    shape_index = 0
    draw_mode = 'circle'

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_SPACE:
                    if shape_index < len(shape) - 1:
                        shape_index += 1
                    else:
                        shape_index = 0
                    draw_mode = shape[shape_index]

                # determine if a letter key was pressed
                if event.key == pygame.K_e:
                    mode = 'eraser'
                elif event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_y:
                    mode = 'yellow'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # right click shrinks radius
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                if mode != 'eraser':
                    points = points + [position]
                    points = points[-256:]
                    eraser_points.clear()
                else:
                    eraser_points += [position]
                    points.clear()

        # draw all points
        i = 0
        if mode != 'eraser':
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, draw_mode)
                i += 1
        else:
            while i < len(eraser_points) - 1:
                erasor(screen, i, eraser_points[i], eraser_points[i + 1], radius, draw_mode)
                i += 1

        pygame.display.flip()

        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode, draw_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'yellow':
        color = (c2, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if draw_mode == shape[0]:
            pygame.draw.circle(screen, color, (x, y), width)
        elif draw_mode == shape[1]:
            pygame.draw.rect(screen, color, pygame.Rect(x - width, y - width, width * 2, width * 2))


def erasor(screen, index, start, end, width, draw_mode):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if draw_mode == shape[0]:
            pygame.draw.circle(screen, (0, 0, 0), (x, y), width)
        elif draw_mode == shape[1]:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x - width, y - width, width * 2, width * 2))


main()