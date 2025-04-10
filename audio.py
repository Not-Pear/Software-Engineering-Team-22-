import pygame
import random

pygame.mixer.init()
def chooseAudio():
    number = random.randint(0,7)
    soundFile = "" 
    if number == 0: 
        soundFile = "Track01.mp3"
    elif number == 1: 
        soundFile = "Track02.mp3"
    elif number == 2: 
        soundFile = "Track03.mp3"
    elif number == 3: 
        soundFile = "Track04.mp3"
    elif number == 4: 
        soundFile = "Track05.mp3"
    elif number == 5: 
        soundFile = "Track06.mp3"
    elif number == 6: 
        soundFile = "Track07.mp3"
    elif number == 7: 
        soundFile = "Track08.mp3"
    else: 
        print("Unknown command, please try again") 

    return soundFile

def playAudio():

    pygame.mixer.music.load(chooseAudio())
    pygame.mixer.music.play()

def stopAudio(): 
    pygame.mixer.music.stop()

