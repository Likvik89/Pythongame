import pygame
import sys
import random
from movement import player_movement
from movement import grape_movement
from movement import blueberry_movement
from colision import apple_colision
from colision import grape_colision
from colision import blueberry_colision
import confik

# Initialize pygame
pygame.init()


# Create a window with a size of 1200x800
screen = pygame.display.set_mode((confik.screen_width, confik.screen_height))
pygame.display.set_caption("CUBE OF DEATH")

font = pygame.font.Font(None, 50)
big_font = pygame.font.Font(None, 50)

# Function to display text on the screen
def display_text(text, x, y):
    label = font.render(text, True, (255, 255, 255))
    screen.blit(label, (x, y))

# Function to display text on the screen
def display_big_text(text, x, y):
    label = big_font.render(text, True, (255, 255, 255))
    screen.blit(label, (x, y))

# Spil-løkke
running = True
while running:

    if confik.time_start >= 1 or confik.time_start == 1:
        if confik.stop_game == 0:
            confik.milisec -= 3
        if confik.milisec <= 0:
            confik.milisec += 1000
            confik.sec -= 1
        if confik.milisec >= 1000:
            confik.milisec -= 1000
            confik.sec += 1
        if confik.sec <= 0:
            confik.stop_game += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Luk spillet, hvis der trykkes på ESC-tasten
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_RETURN:
                if confik.stop_game == 0:
                    confik.time_start += 1
                    confik.start_game += 1
                else:
                    confik.milisec -= confik.milisec
                    confik.sec += 10
                    if confik.point >= confik.high_point:
                        confik.high_point -= confik.high_point
                        confik.best_time -= confik.best_time 
                        confik.high_point += confik.point
                        confik.best_time += confik.total_time
                    confik.point -= confik.point
                    confik.stop_game -= confik.stop_game 
                    confik.start_game -= confik.start_game
                    confik.time_start -= confik.time_start 
                    confik.total_time -= confik.total_time
                    confik.grape_time -= confik.grape_time
                    confik.milisec_grape_time -= confik.milisec_grape_time
                    confik.player_pos_x = 600  # Initial player x-position
                    confik.player_pos_y = 400  # Initial player y-position
                    confik.apple_pos_y = (random.randint(0, confik.screen_height-confik.apple_height))
                    confik.apple_pos_x = (random.randint(0, confik.screen_width-confik.apple_width))
                    confik.grape_pos_y = (random.randint(0, confik.screen_height-confik.grape_height))
                    confik.grape_pos_x = (random.randint(0, confik.screen_width-confik.grape_width))
                    confik.grape_bounce_x = (random.randint(0, 1))
                    confik.grape_bounce_y = (random.randint(0, 1))


            if event.key == pygame.K_t:
                if confik.cheat == 1:
                    confik.cheat -= 1
                else:
                    confik.cheat += 1


    #check script movement.py
    player_movement()

    grape_movement()

    blueberry_movement()

    #check  script colision.py
    apple_colision()

    grape_colision()

    blueberry_colision()

            
    if confik.cheat >= 1:
        automated = True
    else:
        automated = False

    screen.fill((0, 0, 0))
    if confik.start_game == 1:
        if confik.stop_game == 0:
            # Draw the player as a rectangle
            player_color = (0, 255, 0)  # Green color
            pygame.draw.rect(screen, player_color, (confik.player_pos_x, confik.player_pos_y, confik.player_width, confik.player_height))

            # Draw the apple as a rectangle
            apple_color = (255, 0, 0)  # Red color
            pygame.draw.rect(screen, apple_color, (confik.apple_pos_x, confik.apple_pos_y, confik.apple_width, confik.apple_height))

            # Draw the grape as a rectangle
            grape_color = (155, 0, 155)  # Purple color
            pygame.draw.rect(screen, grape_color, (confik.grape_pos_x, confik.grape_pos_y, confik.grape_width, confik.grape_height))

            # Draw the blueberry as a rectangle
            blueberry_color = (0, 0, 255)  # Blue color
            pygame.draw.rect(screen, blueberry_color, (confik.blueberry_pos_x, confik.blueberry_pos_y, confik.blueberry_width, confik.blueberry_height))

            # Display points and time information
            display_text(f"point {confik.point}", 20, 20)  
            display_text(f"gained time {confik.total_time} sec", 20, 60)
            display_text(f"time taken by grape {confik.grape_time}.{confik.milisec_grape_time} sec", 20, 100)
            display_text(f"time: {confik.sec}.{confik.milisec}", 500, 20)
            display_text(f"high score: {confik.high_point}", 20, 140) 
            display_text(f"best gained time: {confik.best_time}", 20, 180)            

        else:
            display_big_text(f"your final points is {confik.point}", 400, 360)
            display_big_text(f"the time you gained is {confik.total_time}sec", 400, 320)
            display_big_text(f"the time you lost to grape is {confik.grape_time}.{confik.milisec_grape_time} sec", 400, 280)
            display_big_text(f"press ENTER to try again", 400, 400)
    else: 
            display_big_text(f"press ENTER to start", 400, 80)

    # Update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(1000)

# Quit Pygame
pygame.quit()
sys.exit()
