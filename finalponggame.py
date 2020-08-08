import pygame
import time
import random
pygame.init()
w_w = 1100
w_h = 750
window = pygame.display.set_mode((w_w, w_h))
pygame.display.set_caption("FINAL PONG GAME")
icon = pygame.image.load('/Users/amitrajpal/Desktop/pong_game.png')
pygame.display.set_icon(icon)
x_1 = 5
y_1 = w_h/2
x_2 = w_w - 25
y_2 = w_h/2
x_3 = x_1 + 40
y_3 = y_1 + 47.5
vel_play = 5
vel_bul_x = 3.5
vel_bul_y = random.randint(-4, 4)
scoreone = 0
scoretwo = 0
counter = 0
run = True

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()
    #start instructions
    if keys[pygame.K_w]:
        y_1 -= vel_play
    if keys[pygame.K_s]:
        y_1 += vel_play
    if keys[pygame.K_UP]:
        y_2 -= vel_play
    if keys[pygame.K_DOWN]:
        y_2 += vel_play
    if y_1 < 0:
        y_1 = 0
    if y_2 < 0:
        y_2 = 0
    if y_1 > w_h - 115:
        y_1 = w_h - 115
    if y_2 > w_h - 115:
        y_2 = w_h - 115
    #end_instruction    
    if x_3 > w_w - 20:
        scoreone += 1
        vel_bul_x = -vel_bul_x
    if x_3 < 0:
        scoretwo += 1
        vel_bul_x = -vel_bul_x        
    if y_3 < 0 or y_3 > w_h - 20:
        vel_bul_y = -vel_bul_y
    
    if x_3 <= x_1 + 20 and x_3 >= x_1 and y_3 >= (y_1 - 20) and y_3 <= (y_1 + 115):
        vel_bul_x = -(vel_bul_x - 0.25)
        vel_bul_y = random.randint(-4, 4)
    
    if x_3 >= x_2 - 20 and x_3 <= x_2 and y_3 >= (y_2 - 20) and y_3 <= (y_2 + 115):  
        vel_bul_x = -(vel_bul_x + 0.25)
        vel_bul_y = random.randint(-4, 4)
        
    x_3 += vel_bul_x
    y_3 += vel_bul_y
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 255), (x_1, y_1, 20, 115))
    pygame.draw.rect(window, (255, 255, 255), (x_2, y_2, 20, 115))
    pygame.draw.rect(window, (255, 255, 255), (x_3, y_3, 20, 20))
    pygame.draw.rect(window, (255, 255, 255), (w_w/2-30, 0, 30, w_h))
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreone), 1, (255, 255, 255))
    window.blit(text, (400, 10))
    text = font.render(str(scoretwo), 1, (255, 255, 255))
    window.blit(text, (650, 10))
    player_font = pygame.font.Font(None, 60)
    text = player_font.render("Player 1", 1, (255, 255, 255))
    window.blit(text, (30, 10))
    text = player_font.render("Player 2", 1, (255, 255, 255))
    window.blit(text, (900, 10))
    newfont = pygame.font.Font(None, 40)
    if scoreone >= 5:
        counter += 1
        if counter == 6:
            scoreone = 0
            scoretwo = 0
            vel_bul_x = 3.5
            x_3 = x_2 - 40
            y_3 = y_2 + 47.5
            counter = 0
        else:
            text = newfont.render("Player 1 wins, player 2 to serve", 1, (255, 255, 255))
            window.blit(text, (75, 350))
            time.sleep(0.5)
            
    if scoretwo >= 5:
        counter += 1
        if counter == 6:
            scoreone = 0
            scoretwo = 0
            vel_bul_x = 3.5
            x_3 = x_1 + 40
            y_3 = y_1 + 47.5            
            counter = 0
        else:
            text = newfont.render("Player 2 wins, player 1 to serve", 1, (255, 255, 255))
            window.blit(text, (600, 350))
            time.sleep(0.5)            
    pygame.display.update()
    
pygame.quit()    




