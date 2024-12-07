# test to create a function with PYGAME which create an input box which is able to return the response written inside.


import pygame 


pygame.init()
class InputBox:
    def __init__(self, x, y, width, height, screen):
        self.rect = pygame.Rect(x, y, width, height)
        self.text_color = (255, 255, 255)
        self.bd_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)
        self.text = ""
        self.answer = None
        self.font = pygame.font.SysFont('Arial', 30)
        self.active = True
        self.cursor_visible = True
        self.cursor_timer = 0
        self.cursor_color = (255, 255, 255)
        self.cursor_width = 2
        self.cursor_height = 20
        self.screen = screen

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state if the box is clicked
            self.active = self.rect.collidepoint(event.pos)

        self.active = True
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.answer = self.text
                self.text=''
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def update(self, dt):
        if self.active:
            self.cursor_timer += dt
            if self.cursor_timer >= 150:  # Toggle cursor 
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = 0

    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self.rect)
        pygame.draw.rect(self.screen, self.bd_color, self.rect, 1)

        # Render text and handle clipping
        text_surface = self.font.render(self.text, True, self.text_color)
        text_offset_x = max(0, text_surface.get_width() - self.rect.width + 10)
        clip_rect = self.rect.copy()
        self.screen.set_clip(clip_rect)
        self.screen.blit(text_surface, (self.rect.x + 5 - text_offset_x, self.rect.y + (self.rect.height - text_surface.get_height()) // 2))
        self.screen.set_clip(None)

        # Draw cursor
        if self.active and self.cursor_visible:
            cursor_x = self.rect.x + 5 + text_surface.get_width() - text_offset_x
            pygame.draw.rect(self.screen, self.cursor_color, (cursor_x, self.rect.y + (self.rect.height - self.cursor_height) // 2, self.cursor_width, self.cursor_height))



class Button():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.active = False
        self.was_clicked = False
        self.stay_active = False

    def draw(self, screen):
        #pygame.draw.rect(screen, self.color, self.rect)    # fonction drawing the button visibly to place it
        pygame.Rect(self.rect)                              # fonction to transform the button in a invisible one

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


