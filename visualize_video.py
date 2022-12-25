#import game library
import pygame
import cv2
import time
from threading import Thread

from image_to_ascii import *

# Define screen object and dimensions
screen = pygame.display.set_mode((700,700))

# Set window title
pygame.display.set_caption("Title")

pygame.init()

font = pygame.font.SysFont('Courier', 7)

BACKGROUND_COLOR = (0,0,0)

image_filepath = r"C:\Users\lesli\OneDrive\Desktop\Hack Everything\Image-to-ASCII\gumball.jpg"
image_array = cv2.imread(image_filepath)

ascii_array = generate_ascii_art(image_array)

def process_video():
    global ascii_array
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture("people.mp4")
    cap.set(cv2.CAP_PROP_FPS, 5)
    
    # Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video file")

    frame_rate = 10
    prev = 0
    
    # Read until video is completed
    while(cap.isOpened()):
        
    # Capture frame-by-frame
        time_elapsed = time.time() - prev
        ret, frame = cap.read()

        if ret == True:
            # if time_elapsed > 1./frame_rate:
            #     prev = time.time()

            #     # Do something with your image here.
            ascii_array = generate_ascii_art(frame)

    # Break the loop
        else:
            break
    
    # When everything done, release
    # the video capture object
    cap.release()

thread = Thread(target = process_video)
thread.start()

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

