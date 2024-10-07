import pygame
import confik

#this is the movement script all movement is inside here

player_position = pygame.Vector2()
player_position.x = confik.player_pos_x
player_position.y = confik.player_pos_y

apple_position = pygame.Vector2(confik.apple_pos_x, confik.apple_pos_y)

grape_position = (confik.grape_pos_x, confik.grape_pos_y)
blueberry_position = pygame.Vector2(confik.blueberry_pos_x, confik.blueberry_pos_y)

def player_movement():
    keys = pygame.key.get_pressed()

    if confik.time_start == 1:
        if confik.cheat:
            confik.player_pos_x += (pygame.math.Vector2.normalize(apple_position-player_position) * confik.player_speed).x
            confik.player_pos_y += (pygame.math.Vector2.normalize(apple_position-player_position) * confik.player_speed).y

        # Move player based on key press
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Left movement (A key)
            confik.player_pos_x -= confik.player_speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Right movement (D key)
            confik.player_pos_x += confik.player_speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:  # Upward movement (W key)
            confik.player_pos_y -= confik.player_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # Downward movement (S key)
            confik.player_pos_y += confik.player_speed

    # Keep the player within screen boundaries
    if confik.player_pos_x < 0:
        confik.player_pos_x = 0
    if confik.player_pos_x + confik.player_width > confik.screen_width:
        confik.player_pos_x = confik.screen_width - confik.player_width
    if confik.player_pos_y < 0:
        confik.player_pos_y = 0
    if confik.player_pos_y + confik.player_height > confik.screen_height:
        confik.player_pos_y = confik.screen_height - confik.player_height

def grape_movement():
    # Follow the player and check for collision with the apple
    if confik.start_game == 1:
        if confik.grape_bounce_x == 0:
            confik.grape_pos_x += confik.grape_speed 
        else:
            confik.grape_pos_x -= confik.grape_speed

        if confik.grape_bounce_y == 0:
            confik.grape_pos_y += confik.grape_speed
        else:
            confik.grape_pos_y -= confik.grape_speed
            
        if confik.grape_pos_x >= 1140:
            confik.grape_bounce_x += 1

        if confik.grape_pos_x <= 0:
            confik.grape_bounce_x -= 1

        if confik.grape_pos_y >= 740:
            confik.grape_bounce_y += 1
            
        if confik.grape_pos_y <= 0:
            confik.grape_bounce_y -= 1

def blueberry_movement():
    # Blueberry follows the apple
    if confik.start_game == 1:
        if confik.blueberry_wait <= 0:
            confik.blueberry_pos_x += (pygame.math.Vector2.normalize(apple_position-blueberry_position) * confik.blueberry_speed).x
            confik.blueberry_pos_y += (pygame.math.Vector2.normalize(apple_position-blueberry_position) * confik.blueberry_speed).y
        else:
            confik.blueberry_wait -= 3
