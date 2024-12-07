import pygame 
from input_box import InputBox, Button
from question_answer import all_qr
from absolute_path import get_resource_path

class Mode:
    def __init__(self, screen, mode):
        # load the background for questions and final menu
        self.bg_image = pygame.image.load(get_resource_path(f'assets/{mode}/{mode}_questions.png'))
        self.final_image = pygame.image.load(get_resource_path(f'assets/{mode}/{mode}_final.png'))
        self.bg_w, self.bg_h = self.bg_image.get_size()
        self.mode = mode
        # game is playing
        self.is_playing = False
        # number of the question
        self.question_nb = 1
        self.question_font = pygame.font.Font(get_resource_path('assets/fonts/DejaVuSans.ttf'), 50)
        self.question = ''
        self.qr = all_qr(f'{mode}')
        self.change_question = True
        # answer 
        self.prec_answer = 0
        self.answer = ''
        self.is_answer_correct = None
        # define the input box
        self.input_box = InputBox(708, 650, 200, 50, screen)
        self.input_box_active = True
        # define the menu button
        self.menu_btn = Button(1250, 830, 300, 80, (255, 255, 255))
        # final score
        self.reset_time = False
        self.stock_score = False
        self.stocked_score = False
        self.current_score = ''
        self.record = ''



    #----------------------------------------------------------------------------------------------------------differents funtions to display the elements on the screen-----------------------------------------------------------------------------------------------

    # print the question number on the top-left corner of the screen
    def print_question_number(self, screen):
        font_number = pygame.font.Font(get_resource_path('assets/fonts/NotoSans.ttf'), 35)
        if self.question_nb <= 20:
            text_number = font_number.render(f'{self.question_nb}', 1, (255, 255, 255))
        else:
            text_number = font_number.render('20', 1, (255, 255, 255))
        screen.blit(text_number, (72, 89))



    # event management
    def handle_event(self, event):
        # pass the event to the input box to avoid conflicts with the main loop events
        self.input_box.handle_event(event)


    # load and print the question on the screen
    def load_question(self, screen):
        self.question = self.qr[0]
        self.answer = self.qr[1]
        text_question = self.question_font.render(f'{self.question}', True, (255, 255, 255))
        text_w, text_h = text_question.get_size()
        x = (self.bg_w - text_w) // 2
        y = (self.bg_h - text_h) // 2
        screen.blit(text_question, (x, y))

    def check_answer(self):
        try:
            if round(self.answer, 2) == round(float(self.input_box.answer), 2):
                self.is_answer_correct = True

            elif self.answer != float(self.input_box.answer) and float(self.input_box.answer) != float(self.prec_answer):
                self.is_answer_correct = False

        except:
            pass
        
    


    # print the correct message in green
    def correct_message(self, screen):
        cmsg_font = pygame.font.Font(None, 50)
        cmsg_text = cmsg_font.render('Correct!', 1, (15, 208, 113))
        screen.blit(cmsg_text, (750, 800))

    # print the false message in red:
    def false_message(self, screen):
        fmsg_font = pygame.font.Font(None, 50)
        fmsg_text = fmsg_font.render('False!', 1, (177, 48, 65))
        screen.blit(fmsg_text, (750, 800))


    # display final messages 
    def final_score_message(self, screen):
        final_font = pygame.font.Font(None, 50)
        final_score = final_font.render(f'{self.current_score}', 1, (255, 255, 255))
        screen.blit(final_score, (755, 445))



    # SCORE STORAGE SYSTEME

    # convert 'XX:YY' type to second
    def time_to_seconds(self, time_str):
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds
    
    def seconds_to_time(self, seconds):
        minutes = seconds // 60
        seconds_i = seconds % 60
        return f'{minutes:02}:{seconds_i:02}'


    def stock_best_score(self, file_path):
        cr_score = self.current_score
        current_score_sec = self.time_to_seconds(cr_score)

        try:
            with open(file_path, 'r') as file:
                scores = file.readlines()
                scores = [s.strip() for s in scores if s.strip()]

                scores_sec = [self.time_to_seconds(score) for score in scores]

        except FileNotFoundError:
            scores_sec = []
        
        if not scores_sec or current_score_sec < min(scores_sec):
            self.record = self.current_score
            with open(file_path, 'a') as file:
                file.write(self.record + '\n')

        else:
            record_sec = min(scores_sec)
            self.record = self.seconds_to_time(record_sec)


    def display_record(self, screen):
        record_font = pygame.font.Font(None, 50)
        record_msg = record_font.render(f'{self.record}', 1, (255, 255, 255))
        screen.blit(record_msg, (760, 630))




    # ------------------------------------------------------------------------------------------------------main method to run the easy mode with its own event management--------------------------------------------------------------------------------------------
    def play(self, screen):

        # DISPLAY THE ELEMENTS ON THE SCREEN

        # display the easy mode background
        screen.blit(self.bg_image, (0, 0))

        # display the question number 
        self.print_question_number(screen)


        # 'display' the menu button -> EASY text
        self.menu_btn.draw(screen); self.menu_btn.active = True


        # display the input_box
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu_btn.is_clicked(event.pos) and self.menu_btn.active:
                    self.is_playing = False
                    self.reset_time = True
                    self.question_nb = 1
                    self.input_box_active = True
                    self.stock_score = False
                    self.stocked_score = False
                return
            self.input_box.handle_event(event)

                
        if self.input_box_active:
            self.input_box.update(pygame.time.Clock().tick(60))
            self.input_box.draw()





        # MANAGE THE ANSWERS AND GAME EVOLUTION
        # display the questions

        if self.question_nb <= 20:
            self.load_question(screen)
            #print(f'{self.answer}, {self.input_box.answer}, {self.is_answer_correct}, {self.prec_answer}')
            self.check_answer()
            if self.is_answer_correct:
                self.prec_answer = self.answer
                self.qr = all_qr(f'{self.mode}')
                self.correct_message(screen)
                self.is_answer_correct = None
                self.question_nb += 1
            elif self.is_answer_correct == False:
                self.false_message(screen)
        
        else:
            # display final messages
            self.input_box_active = False
            self.stock_score = True
            screen.blit(self.final_image, (0, 0))
            self.menu_btn.draw(screen)
            self.final_score_message(screen)
            if self.stocked_score:
                self.stock_score = False



        
        



        



    


        