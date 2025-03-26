import pygame

pygame.init()
'''

Hot keys:
1 – Line

2 – Rectangle

3 – Circle

E –  Eraser

R – Red light

B – Blue light

K – Black light

+ – Increase thickness

- – Reduce thickness

'''

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


drawing = False
tool = "line" 
color = BLACK
thickness = 5
start_pos = (0, 0)

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(WHITE)

running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = "line"
            elif event.key == pygame.K_2:
                tool = "rect"
            elif event.key == pygame.K_3:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK
            elif event.key == pygame.K_EQUALS:
                thickness += 1
            elif event.key == pygame.K_MINUS and thickness > 1:
                thickness -= 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos
                if tool == "line":
                    pygame.draw.line(background, color,
                                     start_pos, end_pos, thickness)
                elif tool == "rect":
                    pygame.draw.rect(background, color, pygame.Rect(
                        *start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), thickness)
                elif tool == "circle":
                    radius = ((end_pos[0] - start_pos[0]) **
                              2 + (end_pos[1] - start_pos[1])**2) ** 0.5
                    pygame.draw.circle(background, color,
                                       start_pos, int(radius), thickness)
                elif tool == "eraser":
                    pygame.draw.circle(background, WHITE, start_pos, thickness)
                drawing = False

        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "eraser":
                pygame.draw.circle(background, WHITE, event.pos, thickness)

    pygame.display.flip()

pygame.quit()