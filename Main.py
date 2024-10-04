import pygame
import sys
import random
from movement import player_movement
from movement import grape_movement
from movement import blueberry_movement
from colision import apple_colision
from colision import grape_colision
from colision import blueberry_colision

# Initialize pygame
pygame.init()

# skærem størelse
screen_width = 1200
screen_height = 800

# player
player_pos_x = 600  # Initial player x-position
player_pos_y = 400  # Initial player y-position
player_width = 60
player_height = 60
player_speed = 3

# apple
apple_width = 60
apple_height = 60
apple_pos_y = (random.randint(0, screen_height-apple_height))
apple_pos_x = (random.randint(0, screen_width-apple_width))


# grape
grape_width = 60
grape_height = 60
grape_pos_y = (random.randint(0, screen_height-grape_height))
grape_pos_x = (random.randint(0, screen_width-grape_width))
grape_speed = 3
grape_bounce_x = (random.randint(0, 1))
grape_bounce_y = (random.randint(0, 1))

# blueberry
blueberry_width = 60
blueberry_height = 60
blueberry_pos_y = (random.randint(0, screen_height - blueberry_height))
blueberry_pos_x = (random.randint(0, screen_width - blueberry_width))
blueberry_speed = 2
blueberry_bounce_x = (random.randint(0, 1))
blueberry_bounce_y = (random.randint(0, 1))


# tid 
milisec = 0
sec = 10
blueberry_wait = 500

point = 0

# spil start stop 
stop_game = 0
start_game = 0

# scorre systemet
high_point = 0 
time_start = 0
total_time = 0
best_time = 0
grape_time = 0
milisec_grape_time = 0

#  cheat
automated = False
cheat = 0

# Create a window with a size of 1200x800
screen = pygame.display.set_mode((screen_width, screen_height))
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

    if time_start >= 1 or time_start == 1:
        if stop_game == 0:
            milisec -= 3
        if milisec <= 0:
            milisec += 1000
            sec -= 1
        if milisec >= 1000:
            milisec -= 1000
            sec += 1
        if sec <= 0:
            stop_game += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Luk spillet, hvis der trykkes på ESC-tasten
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_RETURN:
                if stop_game == 0:
                    time_start += 1
                    start_game += 1
                else:
                    milisec -= milisec
                    sec += 10
                    if point >= high_point:
                        high_point -= high_point
                        best_time -= best_time 
                        high_point += point
                        best_time += total_time
                    point -= point
                    stop_game -= stop_game 
                    start_game -= start_game
                    time_start -= time_start 
                    total_time -= total_time
                    grape_time -= grape_time
                    milisec_grape_time -= milisec_grape_time
                    player_pos_x = 600  # Initial player x-position
                    player_pos_y = 400  # Initial player y-position
                    apple_pos_y = (random.randint(0, screen_height-apple_height))
                    apple_pos_x = (random.randint(0, screen_width-apple_width))
                    grape_pos_y = (random.randint(0, screen_height-grape_height))
                    grape_pos_x = (random.randint(0, screen_width-grape_width))
                    grape_bounce_x = (random.randint(0, 1))
                    grape_bounce_y = (random.randint(0, 1))


            if event.key == pygame.K_t:
                if cheat == 1:
                    cheat -= 1
                else:
                    cheat += 1


    #check script movement.py
    player_movement()

    grape_movement()

    blueberry_movement()

    #check  script colision.py
    apple_colision()

    grape_colision()

    blueberry_colision()

            
    if cheat >= 1:
        automated = True
    else:
        automated = False


    # F.eks. kan du udfylde baggrunden med sort farve
    screen.fill((0, 0, 0))
    if start_game == 1:
        if stop_game == 0:
            # Tegner spilleren som et rektangel
            player_color = (0, 255, 0)  # Grøn farve
            pygame.draw.rect(screen, player_color, (player_pos_x, player_pos_y, player_width, player_height))

            # Tegner appel som et rektangel
            apple_color = (255, 0, 0)  # rød farve
            pygame.draw.rect(screen, apple_color, (apple_pos_x, apple_pos_y, apple_width, apple_height))


            # Tegner grape som et rektangel
            grape_color = (155, 0, 155)  # lila farve
            pygame.draw.rect(screen, grape_color, (grape_pos_x, grape_pos_y, grape_width, grape_height))

            
            # Tegner appel som et rektangel
            blueberry_color = (0, 0, 255)  # blå farve
            pygame.draw.rect(screen, blueberry_color, (blueberry_pos_x, blueberry_pos_y, blueberry_width, blueberry_height))


            display_text(f"point {point}", 20, 20)  
            display_text(f"gained time {total_time} sec", 20, 60)
            display_text(f"time taken by grape {grape_time}.{milisec_grape_time} sec", 20, 100)
            display_text(f"time: {sec}.{milisec}", 500, 20)
            display_text(f"high score: {high_point}", 20, 140) 
            display_text(f"best gained time: {best_time}", 20, 180)            

        else:
            display_big_text(f"your final points is {point}", 400, 360)
            display_big_text(f"the time you gaind is {total_time}sec", 400, 320)
            display_big_text(f"the time you lost to grape is {grape_time}.{milisec_grape_time} sec", 400, 280)
            display_big_text(f"press ENTER to try again", 400, 400)
    else: 
                    display_big_text(f"press ENTER to start", 400, 80)

    # Opdaterer skærmen
    pygame.display.flip()
    pygame.time.Clock().tick(1000)

# Afslutter Pygame
pygame.quit()
sys.exit()