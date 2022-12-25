#import game library
import pygame
import cv2

from image_to_ascii import *

# Define screen object and dimensions
screen = pygame.display.set_mode((700,700))

# Set window title
pygame.display.set_caption("Title")

pygame.init()

font = pygame.font.SysFont('Courier', 7)

BACKGROUND_COLOR = (0,0,0)

image_filepath = r"C:\Users\lesli\OneDrive\Desktop\Hack Everything\Image-to-ASCII\gumball.png"
image_array = cv2.imread(image_filepath)

ascii_array = generate_ascii_art(image_array)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(BACKGROUND_COLOR)

    y_pos = 0

    for i in range(len(ascii_array)):

        test_message = font.render(ascii_array[i][:-1], True, (0, 255, 0))

        screen.blit(test_message, (0, y_pos))
        y_pos += 6

    pygame.display.flip()

pygame.quit()