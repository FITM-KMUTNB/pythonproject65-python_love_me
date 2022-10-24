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
font1 = pygame.font.Font("freesansbold.ttf", 48)
font2 = pygame.font.Font("freesansbold.ttf", 32)
TEXT_COL = (0, 0, 0)
success_count = 0

start_img = pygame.image.load("images/start.png").convert_alpha()
tutorail_img = pygame.image.load("images/tutorail.png").convert_alpha()
scoreboard_img = pygame.image.load('images/scoreboard.png').convert_alpha()
quit_img = pygame.image.load("images/quit.png").convert_alpha()
restart_img = pygame.image.load('images/restart.png').convert_alpha()
home_img = pygame.image.load('images/home.png').convert_alpha()

start_button = button.Button(295, 175, start_img, 0.33)
tutorail_button = button.Button(295, 250, tutorail_img, 0.33)
scoreboard_button = button.Button(295, 325, scoreboard_img, 0.33)
quit_button = button.Button(295, 400, quit_img, 0.33)
restart_button = button.Button(295, 250, restart_img, 0.33)
home_button = button.Button(295, 325, home_img, 0.33)

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
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
run = True
while run:
    if menu_state == "start":
        pygame.init()
        display_surface = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Start menu")
        startrun = True
        display_surface.fill((255,255,255))
        while startrun:
            if start_button.draw(screen):
                menu_state = 'game'
                startrun = False
            if tutorail_button.draw(screen):
                menu_state = "tutorail"
                startrun = False
            if scoreboard_button.draw(screen):
                menu_state = 'scoreboard'
                startrun = False
            if quit_button.draw(screen):
                run = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    startrun = False
            pygame.display.update()
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
            countdown_timer = (5+pytime) - (pygame.time.get_ticks() / 1000)
            if float(countdown_timer) <= 0.00:#end game
                display_surface.fill((255,255,255))
                menu_state = 'end'
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
                        rungame = False
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
            pygame.display.update()
            clock.tick(60)
    if menu_state == "tutorail":
        pass
    if menu_state == 'scoreboard':
        pass
    if menu_state == 'end':
        pygame.init()
        display_surface = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("End menu")
        endrun = True
        display_surface.fill((255,255,255))
        while endrun:
            render_text(display_surface,font1,"Game Over.",(0,0,0),(275,35))
            render_text(display_surface,font2," Score :  {0} word per minute".format(success_count),(0,0,0),(175,125))
            if restart_button.draw(screen):
                menu_state = 'game'
                endrun = False
            if home_button.draw(screen):
                menu_state = "start"
                endrun = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    endrun = False
            pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()