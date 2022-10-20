from cgitb import text
from tkinter.tix import IMAGE, Tree
from numpy import true_divide
import pygame
import random
pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TYPING GAME')
icon = pygame.image.load('icon.png') #import icon 
pygame.display.set_icon(icon)

font = pygame.font.Font(None,32)
#coordinates
textX = 170
Texty = 450

currentWord = ''
OGword = " "
indexedWord = list(currentWord)
currentLenght = len(indexedWord)
lenghtTracker = 0
starttracker = 0 #used to have the intro screen only appear 

#Random words
words = ["The environment refers to the surroundings in which life exists on earth. Components like animals, humans, sunlight, water, trees, and air make up the environment. They are the earth/'s living and nonliving components. Living organisms include trees, humans, and animals. Non-living components such as the sun, water and air are essential for man/'s life.","Our environment is nature/'s most precious and vital gift, which needs to be handled with utmost care. It is the natural ecological system where we live, depending on each other for survival. The environment is divided into physical and biological components. The atmosphere, lithosphere and hydrosphere constitute the physical category, and the biological category comprises human beings and other living beings. In simple terms, the environment is defined as the combination and interrelation between all biotic and abiotic components. The ecosystem of our environment needs to be maintained in a proper balance, and if any part of it is disturbed, the whole ecosystem gets affected."]

score = 0 
scorebord = "Score"+ str(score)

def printer(x,y):
    """ Present  the text onto the screen """
    show = font.render(currentWord, True,(255,0,100))
    screen.blit(show,(x,y))

def updatescore():
    """ Updates the  score"""
    show = font.render((scorebord),True,(0,0,0)) #surface string
    screen.blit(show,(525,10))

def intro():
    """ Lays out everything for  the starting screen"""
    CX = 350
    show1 = font.render("Press SPACEBAR"), True,(0,0,0)
    show2 = font.render("To start typing "),True,(0,0,0)
    screen.blit(show1,(75,90))
    screen.blit(show2,(70,125))

def randomString():
    """Generate a random string of fixed length"""
    num =  random.randrange(2)
    return words[num]

def randomCoordinates():
    """Generates  a random  coordinates to use when spawing  a new  word in"""
    textX = random.randrange(550)
    Texty = random.randrange(125,350)
    return textX,Texty

def correctLetter():
    """Eliminates the first letter of  the word when the user is correct"""
    global textX
    global lenghtTracker
    global indexedWord
    global currentWord
    del indexedWord[0]
    temp = ""  #stores the joined string
    currentWord = temp.join(indexedWord)
    lenghtTracker += 1 # used to keep track of which  letter the user is on

def wrongLetter():
    """when  a letter is wrong, we want to restart and print  out the original words."""
    global OGword
    global currentWord
    global OGindex
    global indexedWord
    global lenghtTracker
    #reseting the word length
    currentWord = OGword
    indexedWord = OGindex.copy()
    lenghtTracker = 0 #resets the letter tracker

tracker = True
while tracker :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tracker=(
                False
            )
            if event.key == pygame.K_a:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "a":
                    correctLetter()
                else:
                    wrongLetter()

            # Each elif statement is for a certain letter on the keyboard
            elif event.key == pygame.K_b:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "b":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_c:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "c":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_d:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "d":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_e:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "e":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_f:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "f":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_g:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "g":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_h:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "h":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_i:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "i":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_j:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "j":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_k:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "k":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_l:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "l":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_m:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "m":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_n:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "n":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_o:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "o":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_p:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "p":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_q:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "q":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_r:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "r":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_s:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "s":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_t:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "t":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_u:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "u":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_v:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "v":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_w:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "w":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_x:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "x":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_y:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "y":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_z:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "z":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_SPACE:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == " ":
                    correctLetter()
screen.fill((65,105,225))
screen.blit(0,0)
printer(textX,Texty)
updatescore(scorebord)
if starttracker == 0:
    intro()
if lenghtTracker== currentLenght:
    IMAGE_TIME = 30
    if IMAGE_TIME > 0 and(starttracker != 0):
        #fire the bullet
        IMAGE_TIME-=1
        score +=1
    starttracker += 1 #used to exits loading screen in the begining
    scorebord = "Words Types: "+str(score)
    currentWord = randomString()
    OGword = currentWord
    OGindex = indexedWord.copy()
    currentLenght = len(indexedWord)
    lenghtTracker = 0
    textX, Texty = randomCoordinates() 

    #this spawn image
pygame.display.update()


playing = True # run program
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit game while push bottom [X]
            playing = False

