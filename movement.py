import pygame
import sys
import random

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

screen = (screen_width, screen_height)

player_position = pygame.Vector2()
player_position.x = player_pos_x
player_position.y = player_pos_y

apple_position = pygame.Vector2(apple_pos_x, apple_pos_y)

grape_position = (grape_pos_x, grape_pos_y)
blueberry_position = pygame.Vector2(blueberry_pos_x, blueberry_pos_y)

def player_movement():
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

def grape_movement():
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

def blueberry_movement():
         # blueberry follow apple
    if start_game == 1:
            if blueberry_wait <= 0:
                
                blueberry_pos_x += (pygame.math.Vector2.normalize(apple_position-blueberry_position)*blueberry_speed).x
                blueberry_pos_y += (pygame.math.Vector2.normalize(apple_position-blueberry_position)*blueberry_speed).y
                
                

           #     if blueberry_pos_x > apple_pos_x:
            #        blueberry_pos_x -= blueberry_speed
             #   else:
              #      blueberry_pos_x += blueberry_speed
               # 
         #       if blueberry_pos_y > apple_pos_y:
          #          blueberry_pos_y -= blueberry_speed
           #     else:
            #        blueberry_pos_y += blueberry_speed
            #    blueberry_wait -= blueberry_wait
            else:
                blueberry_wait -= 3