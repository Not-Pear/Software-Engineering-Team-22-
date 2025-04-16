import pygame
import random

pygame.mixer.init()
def chooseAudio():
    number = random.randint(0,7)
    soundFile = "" 
    if number == 0: 
        soundFile = "gamesounds1/Track01.mp3"
    elif number == 1: 
        soundFile = "gamesounds1/Track02.mp3"
    elif number == 2: 
        soundFile = "gamesounds1/Track03.mp3"
    elif number == 3: 
        soundFile = "gamesounds1/Track04.mp3"
    elif number == 4: 
        soundFile = "gamesounds1/Track05.mp3"
    elif number == 5: 
        soundFile = "gamesounds1/Track06.mp3"
    elif number == 6: 
        soundFile = "gamesounds1/Track07.mp3"
    elif number == 7: 
        soundFile = "gamesounds1/Track08.mp3"
    else: 
        print("Unknown command, please try again") 

    return soundFile

def playAudio():

    pygame.mixer.music.load(chooseAudio())
    pygame.mixer.music.play()

def stopAudio(): 
    pygame.mixer.music.stop()

