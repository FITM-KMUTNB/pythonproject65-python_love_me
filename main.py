import pygame
import random
import button
pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")
menu_state = "start"
font2 = pygame.font.Font("freesansbold.ttf", 32)
TEXT_COL = (0, 0, 0)
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)
success_count = 0
def load_words_file(filename):
    word_file = open(filename, "r")
    lines_read = word_file.readlines()
    word_file.close()
    return lines_read
def render_text(display_surface, font, text_content, color, position):
    text = font.render(text_content, True, color)
    display_surface.blit(text, position)
def release_wave(count,lines_read,words_on_screen):#count : how many words will be spawned
    for i in range(count):
        random_y = random.randint(50, 450)
        randomed = random.randrange(0,len(lines_read)) 
        randomed_word = lines_read[randomed].replace("\n","")
        words_on_screen.append({"word": randomed_word,"coordinate": (0,random_y)})
def is_word_on_screen(words_on_screen,word):
    for i in range(len(words_on_screen)):
        if word == words_on_screen[i]["word"]:
            return i 
    return -1
def scoreboard():
    pass
def tutorial():
    pass
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
run = True
while run:
    screen.fill((255, 255, 255))
    if menu_state == "start":
        if resume_button.draw(screen):
            menu_state = 'game'
        if options_button.draw(screen):
            menu_state = "options"
        if quit_button.draw(screen):
            run = False
    if menu_state == "game":
        lines_read = load_words_file("english_words.txt")# load words from the file
        pygame.init()
        display_surface = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Typing game")
        ended = False
        words_on_screen = []
        font = pygame.font.Font("freesansbold.ttf", 32)
        dx = 1 # moving speed for texts
        countdown_timer = 60 
        word_spawn_timer = pygame.time.get_ticks()# used for spawning words
        typing_buffer = []
        current_text = ""
        success_count = 0
        rungame = True
        pytime = pygame.time.get_ticks()/1000
        while rungame:
            countdown_timer = (60+pytime) - (pygame.time.get_ticks() / 1000)
            if float(countdown_timer) <= 0.00:#end game
                display_surface.fill((255,255,255))
                ended = True
                rungame = False
            if not ended:
                display_surface.fill((255,255,255))
                if(pygame.time.get_ticks()-word_spawn_timer > 700):
                    word_spawn_timer = pygame.time.get_ticks()
                    release_wave(1,lines_read,words_on_screen)
                for word_info in words_on_screen:
                    word_info["coordinate"] = (word_info["coordinate"][0] + dx,word_info["coordinate"][1])
                    render_text(display_surface,font,word_info["word"],(0,0,0),word_info["coordinate"])
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if pygame.key.name(event.key) == "return":
                            index_found = is_word_on_screen(words_on_screen,current_text)
                            if index_found != -1:
                                words_on_screen.pop(index_found)
                                success_count += 1
                            else:
                                print("wrong")
                            typing_buffer = []
                        else:
                            if pygame.key.name(event.key) == "backspace": #if backspace then delete last element of typing buffer
                                if len(typing_buffer) != 0:
                                    typing_buffer.pop(len(typing_buffer)-1)
                            else:
                                typing_buffer.append(pygame.key.name(event.key))
                        current_text = "".join(typing_buffer)
                render_text(display_surface,font,current_text,(0,0,0),(20,450))
                render_text(display_surface,font,str('%.2f'%(countdown_timer)),(0,0,0),(675,450))
                render_text(display_surface,font,str('%d'%(success_count)),(0,0,0),(750,27))
                render_text(display_surface,font,'Score:',(0,0,0),(640,25))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()
            clock.tick(60)
        menu_state = 'end'
    if menu_state == "options":
        if video_button.draw(screen):
            print("Video Settings")
        if audio_button.draw(screen):
            print("Audio Settings")
        if keys_button.draw(screen):
            print("Change Key Bindings")
        if back_button.draw(screen):
            menu_state = "start"
    if menu_state == 'end':
        pygame.init()
        display_surface = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("End menu")
        font1 = pygame.font.Font("freesansbold.ttf", 48)
        font2 = pygame.font.Font("freesansbold.ttf", 32)
        endrun = True
        while endrun:
            display_surface.fill((255,255,255))
            render_text(display_surface,font1,"Game Over.",(0,0,0),(275,35))
            render_text(display_surface,font2," Score :  {0} word per minute".format(success_count),(0,0,0),(150,450))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()