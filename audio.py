import pygame
import random

pygame.mixer.init()
def chooseAudio():
    number = random.randint(0,7)
    soundFile = "" 
    if number == 0: 
        soundFile = "gameSounds/Track01.mp3"
    elif number == 1: 
        soundFile = "gameSounds/Track02.mp3"
    elif number == 2: 
        soundFile = "gameSounds/Track03.mp3"
    elif number == 3: 
        soundFile = "gameSounds/Track04.mp3"
    elif number == 4: 
        soundFile = "gameSounds/Track05.mp3"
    elif number == 5: 
        soundFile = "gameSounds/Track06.mp3"
    elif number == 6: 
        soundFile = "gameSounds/Track07.mp3"
    elif number == 7: 
        soundFile = "gameSounds/Track08.mp3"
    else: 
        print("Unknown command, please try again") 

    return soundFile

def playAudio():

    pygame.mixer.music.load(chooseAudio())
    pygame.mixer.music.play()

def stopAudio(): 
    pygame.mixer.music.stop()

