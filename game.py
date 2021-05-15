''' 
    Game name - Dodge Cool
    Rule - Keep distance from coming cars and beat your highest score
'''
import pygame
import random
import time
pygame.init()
pygame.mixer.init() #for music
#colors
white = (255, 255, 255)
black = (0 , 0, 0)
red = (255, 0 , 0)
green = (0 , 255 , 0)
blue = (0, 0 , 255)
yellow = (255, 255, 0)
#making a window
gameWindow = pygame.display.set_mode((500,500))
pygame.display.set_caption("Dodge Cool")
pygame.display.update()
#definng fonts
Font = pygame.font.SysFont(None ,40)
Font1 = pygame.font.SysFont(None, 30)
Font2 = pygame.font.SysFont(None, 22)
#gameover image
overimg = pygame.image.load('res\gover.jpg')
overimg = pygame.transform.scale(overimg, (500, 500)).convert_alpha()
#bike image
bikeimg = pygame.image.load("res\cbike.png").convert_alpha()
bikeimg = pygame.transform.scale(bikeimg, (50, 100))
#enemy car 1 image
en1img = pygame.image.load('res\en1.png').convert_alpha()
en1img = pygame.transform.scale(en1img, (50, 100))
#enemy car 2 image
en2img = pygame.image.load('res\en2.png').convert_alpha()
en2img = pygame.transform.scale(en2img, (50, 100))
#defining clock variable to control FPS of game
clock = pygame.time.Clock()
fps = 40

#thankyou image 
tq = pygame.image.load('res\Thankyou.jpg').convert_alpha()
#welcome function for instructions
def welcome():
    exit_game = False
    while not exit_game:
        #welcome page image
        welcimg = pygame.image.load('res\Welcome.gif').convert_alpha()
        gameWindow.blit(welcimg, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame. mixer. music. stop()
                gameWindow.blit(tq, (0,0))
                pygame.display.update()
                time.sleep(1)
                exit_game = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_i:
                    #welcome page audio 2  (instructions)
                    pygame.mixer.music.load('res\instruction.mp3')                        
                    pygame.mixer.music.play()
                if event.key == pygame.K_s:
                    gameloop()
                    exit_game = True
                if event.key == pygame.K_ESCAPE:
                    pygame. mixer. music. stop()
                    gameWindow.blit(tq, (0,0))
                    pygame.display.update()
                    time.sleep(1)
                    exit_game = True
def gameloop():
    #background music
    pygame.mixer.music.load('res\cbgm.mp3')
    pygame.mixer.music.play()
    exit_game = False
    game_over = False
    car_x = 225
    car_y = 400
    size = 50
    m1y1 = 250
    m1y2 = 300 #length of marking 1 = 50 
    m2y1 = 50
    m2y2 = 100 #length of marking 2 = 50
    m3y1 = 350
    m3y2 = 400 #length of marking 3 = 50
    m4y1 = -50
    m4y2 = 0   #length of marking 4 = 50
    en2x = random.choice([150, 225, 300])
    en2y = 200
    en1x = random.choice([150, 225, 300])
    en1y = -100
    v = 0
    s = 0
    score = 0
    with open("res\highscore.txt", "r") as f:
        hiscore = f.read()  #string
    while not exit_game:
        
        if game_over == True:
            with open("res\highscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(red)
            gameWindow.blit(overimg , (0, 0))
            hscr = Font2.render("High score: " + str(hiscore), True, black)
            hscr_rect = hscr.get_rect(center = (63, 250))
            gameWindow.blit(hscr, hscr_rect)
            text_score = Font1.render("Score: " + str(score), True, black)
            scr_rect = text_score.get_rect(center = (437, 250))
            gameWindow.blit(text_score , scr_rect)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        gameloop()
                    if event.key == pygame.K_ESCAPE:
                        pygame. mixer. music. stop()
                        gameWindow.blit(tq, (0,0))
                        pygame.display.update()
                        time.sleep(1)
                        exit_game = True
                if event.type == pygame.QUIT:
                    pygame. mixer. music. stop()
                    gameWindow.blit(tq, (0,0))
                    pygame.display.update()
                    time.sleep(1)
                    exit_game = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame. mixer. music. stop()
                    gameWindow.blit(tq, (0,0))
                    pygame.display.update()
                    time.sleep(1)
                    exit_game = True
                    #movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        car_x = car_x + 75
                        v = 5
                    if event.key == pygame.K_LEFT:
                        car_x = car_x - 75
                        v = 5
                    if event.key == pygame.K_UP:
                        car_y = car_y - 100
                        v = 5
                    if event.key == pygame.K_DOWN:
                        car_y = car_y + 100
                        v = 5
            if car_y > 400:
                car_y = 400
            if car_y < 0:
                car_y = 0
            if car_x < 150:
                car_x = 150
            if car_x > 300:
                car_x = 300
            if (en1y > (500-v-s)) or (en2y > (500 - v - s)):
                score = score + 1
                s += 0.2
                if score > int(hiscore):
                    hiscore = score 
            #road image
            roadimg = pygame.image.load('res\croad.jpg')
            roadimg = pygame.transform.scale(roadimg, (500,500)).convert_alpha()
            gameWindow.blit(roadimg, (0,0))
            #Printing Highest Score
            hscr = Font2.render("High score: " + str(hiscore), True, black)
            hscr_rect = hscr.get_rect(center = (63, 100))
            gameWindow.blit(hscr, hscr_rect)
            #Printing Current Score
            text_score = Font1.render("Score: " + str(score), True, black)
            scr_rect = text_score.get_rect(center = (63, 50))
            gameWindow.blit(text_score , scr_rect)
            #moving objects
            m1y1 += v + s
            m1y2 += v + s
            m2y1 += v + s
            m2y2 += v + s 
            m3y1 += v + s
            m3y2 += v + s
            m4y1 += v + s
            m4y2 += v + s
            en2y += v + s
            en1y += v + s
            #if the cars or markings go out of surface
            if m4y1 > 500:
                m4y2 = 0
                m4y1 = -50
            if m3y1 > 500:
                m3y2 = 0
                m3y1 = -50
            if m2y1 > 500:
                m2y2 = 0
                m2y1 = -50
            if m1y1 > 500:
                m1y2 = 0  
                m1y1 = -50
            if en2y > 500:
                en2x = random.choice([150, 225, 300])
                en2y = -100
            if en1y > 500:
                en1x = random.choice([150, 225, 300])
                en1y = -100
            #drawing markings
            pygame.draw.line(gameWindow, white, (212.5, m1y1), (212.5, m1y2)) #draw m1
            pygame.draw.line(gameWindow, white, (282.5, m2y1), (282.5, m2y2)) 
            pygame.draw.line(gameWindow, white, (282.5, m3y1), (282.5, m3y2)) 
            pygame.draw.line(gameWindow, white, (212.5, m4y1), (212.5, m4y2)) 
            gameWindow.blit(bikeimg, (car_x, car_y))
            gameWindow.blit(en2img, (en2x, en2y))
            gameWindow.blit(en1img, (en1x, en1y))
            if (car_x == en1x and abs(car_y - en1y) < 100) or (car_x == en2x and abs(car_y - en2y) < 100):
                v = 0
                s = 0
                pygame.mixer.music.load("res\gameover.mp3")
                pygame.mixer.music.play()
                game_over = True
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
        pygame.display.update()
        clock.tick(fps)
welcome()
pygame.quit()
quit()