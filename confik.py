import random

#this is our conficoration and we putall our vaiablers into this script so that evry script can use them

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
cheat = False

