import pygame
import sys
import random
from pygame import math

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
    player_position = pygame.Vector2()
    player_position.x = player_pos_x
    player_position.y = player_pos_y

    apple_position = pygame.Vector2(apple_pos_x, apple_pos_y)

    grape_position = (grape_pos_x, grape_pos_y)
    blueberry_position = pygame.Vector2(blueberry_pos_x, blueberry_pos_y)
    
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

    keys = pygame.key.get_pressed()

    if time_start == 1:
        if automated:
            

            player_pos_x += (pygame.math.Vector2.normalize(apple_position-player_position) * player_speed).x
            player_pos_y += (pygame.math.Vector2.normalize(apple_position-player_position) * player_speed).y

        # Flytter spilleren baseret på tastetryk
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Venstre bevægelse (A-tasten)
            player_pos_x -= player_speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Højre bevægelse (D-tasten)
            player_pos_x += player_speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:  # Opad bevægelse (W-tasten)
            player_pos_y -= player_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # Nedad bevægelse (S-tasten)
            player_pos_y += player_speed

    # Hold spilleren inden for skærmkanterne
    if player_pos_x < 0:
        player_pos_x = 0
    if player_pos_x + player_width > screen_width:
        player_pos_x = screen_width - player_width
    if player_pos_y < 0:
        player_pos_y = 0
    if player_pos_y + player_height > screen_height:
        player_pos_y = screen_height - player_height



    # follow the player and colison whit the  apple
    if start_game == 1:
        if grape_bounce_x == 0:
            grape_pos_x += grape_speed 
        else:
            grape_pos_x -= grape_speed

        if grape_bounce_y == 0:
            grape_pos_y += grape_speed
        else:
            grape_pos_y -= grape_speed
            
        if grape_pos_x >= 1140:
            grape_bounce_x += 1

        if grape_pos_x <= 0:
            grape_bounce_x -= 1

        if grape_pos_y >= 740:
            grape_bounce_y += 1
            
        if grape_pos_y <= 0:
            grape_bounce_y -= 1


        # blueberry follow apple
    if start_game == 1:
            if blueberry_wait <= 0:
                
                blueberry_pos_x += (pygame.math.Vector2.normalize(apple_position-blueberry_position)*blueberry_speed).x
                blueberry_pos_y += (pygame.math.Vector2.normalize(apple_position-blueberry_position)*blueberry_speed).y
                
                

                if blueberry_pos_x > apple_pos_x:
                    blueberry_pos_x -= blueberry_speed
                else:
                    blueberry_pos_x += blueberry_speed
                
                if blueberry_pos_y > apple_pos_y:
                    blueberry_pos_y -= blueberry_speed
                else:
                    blueberry_pos_y += blueberry_speed
                blueberry_wait -= blueberry_wait
            else:
                blueberry_wait -= 3


    #player colisont med appel
    if stop_game == 0:
        if (player_pos_x > (apple_pos_x-apple_width)) and (player_pos_x < (apple_pos_x + apple_width)) and (player_pos_y > (apple_pos_y-apple_height)) and (player_pos_y < (apple_pos_y + apple_height)):
            apple_pos_y = (random.randint(0, screen_height-apple_height))
            apple_pos_x = (random.randint(0, screen_width-apple_width))
            blueberry_wait -= blueberry_wait
            blueberry_wait += 500
            point += 1
            milisec  += 500
            total_time += 0.5

    #player colisont med grape
    if stop_game == 0:
        if (player_pos_x > (grape_pos_x-grape_width)) and (player_pos_x < (grape_pos_x + grape_width)) and (player_pos_y > (grape_pos_y-grape_height)) and (player_pos_y < (grape_pos_y + grape_height)):
                milisec -= 6
                milisec_grape_time += 6
                if milisec_grape_time >= 1000:
                    milisec_grape_time -= milisec_grape_time
                    grape_time += 1

    #blueberry colisont med apple
    if stop_game == 0:
            if (blueberry_pos_x > (apple_pos_x-apple_width)) and (blueberry_pos_x < (apple_pos_x + apple_width)) and (blueberry_pos_y > (apple_pos_y-apple_height)) and (blueberry_pos_y < (apple_pos_y + apple_height)):
                apple_pos_y = (random.randint(0, screen_height-apple_height))
                apple_pos_x = (random.randint(0, screen_width-apple_width))
                blueberry_wait -= blueberry_wait
                blueberry_wait += 500
            
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