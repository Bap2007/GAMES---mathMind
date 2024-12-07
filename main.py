import pygame 
import sys
import time
from modes import Mode
from input_box import Button
from absolute_path import get_resource_path

# pygame intialisation
pygame.init()
clock = pygame.time.Clock()
FPS = 60

# define window's incon
icon_path = get_resource_path("assets/icons/icon_app.png") 
icon = pygame.image.load(icon_path)
icon = pygame.transform.scale(icon, (64, 64))
pygame.display.set_icon(icon)

# load background image
img_menu = pygame.image.load(get_resource_path("assets/principal_menu/principal_menu.png"))
img_explanation = pygame.image.load(get_resource_path('assets/principal_menu/game_explanation.png'))
img_countdown_1 = pygame.image.load(get_resource_path("assets/countdown/countdown_1.png"))
img_countdown_2 = pygame.image.load(get_resource_path("assets/countdown/countdown_2.png"))
img_countdown_3 = pygame.image.load(get_resource_path("assets/countdown/countdown_3.png"))

# classes buttons definitions + four menu buttons definition

easy_btn = Button(745, 245, 130, 43, (255, 255, 255))
medium_btn = Button(716, 330, 180, 45, (255, 255, 255))
hard_btn = Button(745, 425, 125, 45, (255, 255, 255))
extreme_btn = Button(705, 515, 210, 45, (255, 255, 255))

help_btn = Button(50, 820, 100, 100, (255, 255, 255))

menu_btn = Button(530, 72, 610, 80, (255, 255, 255))

     
    

# define the screen size
screen = pygame.display.set_mode(img_menu.get_size())

# load the different modes
easy_mode = Mode(screen, 'easy')
medium_mode = Mode(screen, 'medium')
hard_mode = Mode(screen, 'hard')
extreme_mode = Mode(screen, 'extreme')

# function to create a countdown before the game start 
countdown_i = True
def countdown(cn_1, cn_2, cn_3):
    global countdown_i
    if countdown_i:
        liste = [cn_3, cn_2, cn_1]
        for i in liste:
            screen.blit(i, (0, 0))
            pygame.display.flip()
            time.sleep(1)
        
# function to create a chronometer on each mode
time_font_i = pygame.font.Font(None, 50)
start_time_i = time.time()




# ---------------------------------------------------------------------------------------------------------- Main Loop ------------------------------------------------------------------------------------------------------------------------------------------
running = True
while running:

    # INITIALISATION AND LOGISTIC
    dt = clock.tick(FPS)

    if easy_mode.reset_time or medium_mode.reset_time or hard_mode.reset_time or extreme_mode.reset_time:
        start_time_i = time.time()
        countdown_i = True
        easy_mode.reset_time = False; medium_mode.reset_time = False; hard_mode.reset_time = False; extreme_mode.reset_time = False

    def chronometer(start_time, time_font):
        elapsed_time = time.time() - start_time -3
        minutes = int(elapsed_time//60)
        seconds = int(elapsed_time%60)
        time_text = f'{minutes:02d}:{seconds:02d}'
        text_surface = time_font.render(time_text, 1, (255, 255, 255))
        screen.blit(text_surface, (1455, 107))
        return time_text


    # EASY MODE PLAYING
    if easy_mode.is_playing: # add elif medium_mode.is_playing and hard_mode.is_playing and extreme_mode.is_playing
        easy_mode.reset_time = False
        # event management in easy mode
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            easy_mode.handle_event(event)
        
        # logistic and display for the easy mode
        countdown(img_countdown_1, img_countdown_2, img_countdown_3)
        countdown_i = False
        easy_mode.play(screen)
        chronometer(start_time_i, time_font_i)
        if easy_mode.stock_score:
            easy_mode.current_score = chronometer(start_time_i, time_font_i)
            easy_mode.stocked_score = True

        if easy_mode.stocked_score:
            easy_mode.stock_best_score(get_resource_path('score/record_easy.txt'))
            easy_mode.display_record(screen)
            menu_btn.active = True


    # MEDIUM MODE PLAYING
    elif medium_mode.is_playing:
        medium_mode.reset_time = False
        #event management in medium mode
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            medium_mode.handle_event(event)
        
        # logistic and display for the easy mode
        countdown(img_countdown_1, img_countdown_2, img_countdown_3)
        countdown_i = False
        medium_mode.play(screen)
        chronometer(start_time_i, time_font_i)
        if medium_mode.stock_score:
            medium_mode.current_score = chronometer(start_time_i, time_font_i)
            medium_mode.stocked_score = True

        if medium_mode.stocked_score:
            medium_mode.stock_best_score(get_resource_path('score/record_medium.txt'))
            medium_mode.display_record(screen)
            menu_btn.active = True  


    # HARD MODE PLAYING
    elif hard_mode.is_playing:
        hard_mode.reset_time = False
        #event management in hard mode
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            hard_mode.handle_event(event)
        
        # logistic and display for the easy mode
        countdown(img_countdown_1, img_countdown_2, img_countdown_3)
        countdown_i = False
        hard_mode.play(screen)
        chronometer(start_time_i, time_font_i)
        if hard_mode.stock_score:
            hard_mode.current_score = chronometer(start_time_i, time_font_i)
            hard_mode.stocked_score = True

        if hard_mode.stocked_score:
            hard_mode.stock_best_score(get_resource_path('score/record_hard.txt'))
            hard_mode.display_record(screen)
            menu_btn.active = True  


    # EXTREME MODE PLAYING
    elif extreme_mode.is_playing:
        extreme_mode.reset_time = False
        #event management in hard mode
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            extreme_mode.handle_event(event)
        
        # logistic and display for the easy mode
        countdown(img_countdown_1, img_countdown_2, img_countdown_3)
        countdown_i = False
        extreme_mode.play(screen)
        chronometer(start_time_i, time_font_i)
        if extreme_mode.stock_score:
            extreme_mode.current_score = chronometer(start_time_i, time_font_i)
            extreme_mode.stocked_score = True

        if extreme_mode.stocked_score:
            extreme_mode.stock_best_score(get_resource_path('score/record_extreme.txt'))
            extreme_mode.display_record(screen)
            menu_btn.active = True  



    # GENERAL MENU
    else: 
        # Display the menu background
        screen.blit(img_menu, (0, 0))
        # Display the buttons
        easy_btn.draw(screen);    easy_btn.active = True
        medium_btn.draw(screen);  medium_btn.active = True
        hard_btn.draw(screen);   hard_btn.active = True
        extreme_btn.draw(screen);   extreme_btn.active = True

        help_btn.draw(screen); help_btn.active = True



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # verification if the mouse click the different buttons
                if easy_btn.is_clicked(event.pos) and easy_btn.active:
                    easy_mode.is_playing = True
                    easy_btn.active = False;medium_btn.active = False;hard_btn.active = False;extreme_btn.active = False; help_btn.active = False

                if medium_btn.is_clicked(event.pos) and medium_btn.active:
                    medium_mode.is_playing = True
                    easy_btn.active = False;medium_btn.active = False;hard_btn.active = False;extreme_btn.active = False; help_btn.active = False

                if hard_btn.is_clicked(event.pos) and hard_btn.active:
                    hard_mode.is_playing = True
                    easy_btn.active = False;medium_btn.active = False;hard_btn.active = False;extreme_btn.active = False; help_btn.active = False

                if extreme_btn.is_clicked(event.pos) and extreme_btn.active:
                    extreme_mode.is_playing = True
                    easy_btn.active = False;medium_btn.active = False;hard_btn.active = False;extreme_btn.active = False; help_btn.active = False

                if help_btn.is_clicked(event.pos) and help_btn.active:
                    easy_btn.active = False;medium_btn.active = False;hard_btn.active = False;extreme_btn.active = False; help_btn.active = False
                    help_btn.stay_active = True
                    while help_btn.stay_active:
                        screen.blit(img_explanation, (0, 0))

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                                help_btn.stay_active = False

                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if help_btn.is_clicked(event.pos):
                                    help_btn.stay_active = False


                        pygame.display.flip()


    

                




    # UPDATE SCREEN
    pygame.display.flip()





# Quit pygame
pygame.quit()
sys.exit()