import pygame
import math
import colorsys

# Initialize Pygame
pygame.init()
width, height = 710, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def branch(x, y, length, angle, level, max_angle):
    if length < 2:
        return

    # Color by level (simulate HSB)
    color = hsv2rgb((level * 0.1) % 1, 1, 1)
    end_x = x + length * math.sin(math.radians(angle))
    end_y = y - length * math.cos(math.radians(angle))

    pygame.draw.line(screen, color, (x, y), (end_x, end_y), 2)

    # Recursive calls
    branch(end_x, end_y, length * 0.66, angle + max_angle, level + 1, max_angle)
    branch(end_x, end_y, length * 0.66, angle - max_angle, level + 1, max_angle)

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))

    # Get mouse x to calculate angle
    mouse_x, _ = pygame.mouse.get_pos()
    angle = min((mouse_x / width) * 90, 90)

    # Draw initial trunk
    start_x, start_y = width // 2, height
    trunk_length = 100
    end_y = start_y - trunk_length
    pygame.draw.line(screen, (0, 255, 255), (start_x, start_y), (start_x, end_y), 2)

    # Start recursion
    branch(start_x, end_y, trunk_length, 0, 0, angle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(6)

pygame.quit()
