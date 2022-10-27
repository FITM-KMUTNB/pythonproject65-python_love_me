import pygame
import random
import button
import pygame_gui
pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
MANAGER = pygame_gui.UIManager((SCREEN_WIDTH,SCREEN_HEIGHT))
menu_state = "start"
font1 = pygame.font.Font("freesansbold.ttf", 48)
font2 = pygame.font.Font("freesansbold.ttf", 32)
font3 = pygame.font.Font("freesansbold.ttf", 24)
font35 = font3 = pygame.font.Font("freesansbold.ttf", 22)
font4 = pygame.font.Font("freesansbold.ttf", 18)
TEXT_COL = (0, 0, 0)
userinput = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((500,50),(300,50)),manager = MANAGER,object_id ='#username')
start_img = pygame.image.load("images/start.png").convert_alpha()
tutorail_img = pygame.image.load("images/tutorial_1.png").convert_alpha()
scoreboard_img = pygame.image.load('images/scoreboard.png').convert_alpha()
restart_img = pygame.image.load('images/restart.png').convert_alpha()
home_img = pygame.image.load('images/home.png').convert_alpha()
bg_img = pygame.image.load('images/back_ground.png')
bg_img = pygame.transform.scale(bg_img,(SCREEN_WIDTH,SCREEN_HEIGHT))
bg1_img = pygame.image.load('images/bg_1.png')
bg1_img = pygame.transform.scale(bg1_img,(SCREEN_WIDTH,SCREEN_HEIGHT))
bg2_img = pygame.image.load('images/bg_2.png')
bg2_img = pygame.transform.scale(bg2_img,(SCREEN_WIDTH,SCREEN_HEIGHT))
bg3_img = pygame.image.load('images/bg_3.png')
bg3_img = pygame.transform.scale(bg3_img,(SCREEN_WIDTH,SCREEN_HEIGHT))

start_button = button.Button(75, 150, start_img, 0.3)
tutorail_button = button.Button(75, 250, tutorail_img, 0.3)
scoreboard_button = button.Button(75, 350, scoreboard_img, 0.3)
restart_button = button.Button(295, 250, restart_img, 0.33)
home_button = button.Button(295, 325, home_img, 0.33)
home2_button = button.Button(350,425, home_img, 0.33)

success_count = 0
wrong_count = 0
username = ''
score = 0

def get_user(userna):
    global username
    username = userna
def load_words_file(filename):
    word_file = open(filename, "r")
    lines_read = word_file.readlines()
    word_file.close()
    return lines_read
def render_text(display_surface, font, text_content, color, position):
    text = font.render(text_content, True, color)
    display_surface.blit(text, position)
def release_wave(count,lines_read,words_on_screen,random_y):#count : how many words will be spawned
    for i in range(count):
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
def fuc_start():
        global menu_state
        global run
        pygame.init()
        display_surface = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Start Menu")
        endrun = True
        display_surface.fill((255,255,255))
        while endrun:
            UI_REFRESH_RATE = clock.tick(60)/1000
            screen.blit(bg1_img,(0,0))
            render_text(display_surface,font1,"Typing Game",(0,0,0),(75,35))
            render_text(display_surface,font4,"Enter username and press Enter",(0,0,0),(505,30))
            if start_button.draw(screen):
                if username != '':
                    menu_state = 'game'
                    endrun = False
            if tutorail_button.draw(screen):
                menu_state = "tutorail"
                endrun = False
            if scoreboard_button.draw(screen):
                menu_state = "scoreboard"
                endrun = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    endrun = False
                if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#username':
                    get_user(event.text)
                MANAGER.process_events(event)
            MANAGER.update(UI_REFRESH_RATE)
            MANAGER.draw_ui(screen)
            pygame.display.update()
def fuc_game():
        global run
        global menu_state
        global success_count
        global wrong_count
        lines_read = load_words_file("english_words.txt")# load words from the file
        pygame.init()
        display_surface = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Typing Game")
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
        posi_y = 60
        while rungame:
            screen.blit(bg3_img,(0,0))
            countdown_timer = (60+pytime) - (pygame.time.get_ticks() / 1000)
            if float(countdown_timer) <= 0.00:#end game
                menu_state = 'end'
                ended = True
                rungame = False
            if not ended:
                if(pygame.time.get_ticks()-word_spawn_timer > 700):
                    word_spawn_timer = pygame.time.get_ticks()
                    release_wave(1,lines_read,words_on_screen,posi_y)
                    posi_y += 60
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
                                wrong_count += 1
                            typing_buffer = []
                        else:
                            if pygame.key.name(event.key) == "backspace": #if backspace then delete last element of typing buffer
                                if len(typing_buffer) != 0:
                                    typing_buffer.pop(len(typing_buffer)-1)
                            else:
                                typing_buffer.append(pygame.key.name(event.key))
                        current_text = "".join(typing_buffer)
                render_text(display_surface,font,current_text,(0,0,0),(20,450))
                render_text(display_surface,font,str('%.2f'%(countdown_timer)),(0,0,0),(700,460))
                render_text(display_surface,font,str('%d'%(success_count)),(0,0,0),(750,27))
                render_text(display_surface,font,username,(0,0,0),(230,25))
                render_text(display_surface,font,'Score:',(0,0,0),(640,25))
                render_text(display_surface,font,'Username:',(0,0,0),(40,25))
                render_text(display_surface,font,'Time:',(0,0,0),(600,460))
                if posi_y >= 450:
                    posi_y = 60
            pygame.display.update()
            clock.tick(60)
        save()
def fuc_end():
        global menu_state
        global run
        pygame.init()
        display_surface = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("End Menu")
        endrun = True
        display_surface.fill((255,255,255))
        while endrun:
            screen.blit(bg_img,(0,0))
            render_text(display_surface,font1,"Game Over!!",(0,0,0),(275,35))
            render_text(display_surface,font2," Score :  {0} word per minute".format(success_count),(0,0,0),(175,125))
            render_text(display_surface,font2," Wrong :  {0} word".format(wrong_count),(0,0,0),(175,170))
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
dic = {}
dicbod = {}
hilow = [0,1,2,3,4,5,6,7,8,9,10,
        11,12,13,14,15,16,17,18,
        19,20,21,22,23,24,25,26,
        27,28,29,30,31,32,33,34,
        35,36,37,38,39,40,41,42,
        43,44,45,46,47,48,49,50,
        51,52,53,54,55,56,57,58,
        59,60,61,62,63,64,65,66,
        67,68,69,70,71,72,73,74,
        75,76,77,78,79,80,81,82,
        83,84,85,86,87,88,89,90,
        91,92,93,94,95,96,97,98,
        99,100,101,102,103,104,105,
        106]
def write():
    filew = open('diction.txt','w')
    for name,score in dic.items():
        score = str(score)
        filew.write(name)
        filew.write(' ')
        filew.write(score)
        filew.write('\n')
    filew.close()
def read():
    filer = open('diction.txt','r')
    line = filer.readline().rstrip('\n')
    while line != '':
        name,score = line.split()
        dic[name] = score
        line = filer.readline().rstrip('\n')
    filer.close()
def updic():
    if username in dic.keys():
        if success_count >= int(dic[username]):
            dic[username] = success_count
    if username not in dic.keys():
        dic[username] = success_count
    else:
        pass

def save():
    read()
    updic()
    write()
def scoreboard():
    read()
    nhilow = len(hilow)
    nhilow = nhilow - 1
    count = 0
    while nhilow >= 0: 
        for name, score in dic.items():
            score = int(score)
            if score == hilow[nhilow]:
                dicbod[name] = score
                count += 1
        if count == 10:
            break
        nhilow -= 1
def fuc_scoreboard():
        scoreboard()
        global menu_state
        global run
        pygame.init()
        display_surface = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("End Menu")
        endrun = True
        display_surface.fill((255,255,255))
        while endrun:
            screen.blit(bg2_img,(0,0))
            render_text(display_surface,font1,"Scoreboard",(0,0,0),(290,15))
            render_text(display_surface,font2,"Ranking",(0,0,0),(50, 75))
            render_text(display_surface,font2,"Username",(0,0,0),(325, 75))
            render_text(display_surface,font2,"Score",(0,0,0),(650, 75))
            for rank in range(10):
                rank = str(rank + 1)
                render_text(display_surface,font3,rank,(0,0,0),(115, 75+int(rank)*32))
            j = 1
            for name,score in dicbod.items():
                score = str(score)
                render_text(display_surface,font3,name,(0,0,0),(350, 75+int(j)*32))
                render_text(display_surface,font3,score,(0,0,0),(675, 75+int(j)*32))
                if j == 10:
                    break
                j += 1
            if home2_button.draw(screen):
                menu_state = "start"
                endrun = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    endrun = False
            pygame.display.update()
def fuc_tutorial():
        scoreboard()
        global menu_state
        global run
        pygame.init()
        display_surface = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("End Menu")
        endrun = True
        display_surface.fill((255,255,255))
        while endrun:
            screen.blit(bg_img,(0,0))
            render_text(display_surface,font1,"Tutorial",(0,0,0),(300,35))
            render_text(display_surface,font35,"1.Enter your username, then press enter",(0,0,0),(50,135))
            render_text(display_surface,font35,"2.Click start button",(0,0,0),(50,185))
            render_text(display_surface,font35,"3.Type each word, then press Enter (the words are on screen)",(0,0,0),(50,235))
            render_text(display_surface,font35,"4.You have only 60 seconds (1 word: 1 score point)",(0,0,0),(50,285))
            render_text(display_surface,font35,"5.Type as much as you can",(0,0,0),(50,335))

            if home2_button.draw(screen):
                menu_state = "start"
                endrun = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    endrun = False
            pygame.display.update()
run = True
while run:
    if menu_state == "start":
        fuc_start()
    if menu_state == "game":
        fuc_game()
    if menu_state == "tutorail":
        fuc_tutorial()
    if menu_state == 'scoreboard':
        fuc_scoreboard()
    if menu_state == 'end':
        fuc_end()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()