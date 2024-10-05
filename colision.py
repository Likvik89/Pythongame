
import random
import confik

#this is the colosiom script we put all things that hvad whit colision inot this script 

def apple_colision():
    # Player collision with apple
    if confik.stop_game == 0:
        if (confik.player_pos_x > (confik.apple_pos_x - confik.apple_width)) and (confik.player_pos_x < (confik.apple_pos_x + confik.apple_width)) and (confik.player_pos_y > (confik.apple_pos_y - confik.apple_height)) and (confik.player_pos_y < (confik.apple_pos_y + confik.apple_height)):
            confik.apple_pos_y = (random.randint(0, confik.screen_height - confik.apple_height))
            confik.apple_pos_x = (random.randint(0, confik.screen_width - confik.apple_width))
            confik.blueberry_wait -= confik.blueberry_wait
            confik.blueberry_wait += 500
            confik.point += 1
            confik.milisec += 500
            confik.total_time += 0.5

def grape_colision():
    # Player collision with grape
    if confik.stop_game == 0:
        if (confik.player_pos_x > (confik.grape_pos_x - confik.grape_width)) and (confik.player_pos_x < (confik.grape_pos_x + confik.grape_width)) and (confik.player_pos_y > (confik.grape_pos_y - confik.grape_height)) and (confik.player_pos_y < (confik.grape_pos_y + confik.grape_height)):
            confik.milisec -= 6
            confik.milisec_grape_time += 6
            if confik.milisec_grape_time >= 1000:
                confik.milisec_grape_time -= confik.milisec_grape_time
                confik.grape_time += 1

def blueberry_colision():
    # Blueberry collision with apple
    if confik.stop_game == 0:
        if (confik.blueberry_pos_x > (confik.apple_pos_x - confik.apple_width)) and (confik.blueberry_pos_x < (confik.apple_pos_x + confik.apple_width)) and (confik.blueberry_pos_y > (confik.apple_pos_y - confik.apple_height)) and (confik.blueberry_pos_y < (confik.apple_pos_y + confik.apple_height)):
            confik.apple_pos_y = (random.randint(0, confik.screen_height - confik.apple_height))
            confik.apple_pos_x = (random.randint(0, confik.screen_width - confik.apple_width))
            confik.blueberry_wait -= confik.blueberry_wait
            confik.blueberry_wait += 500
