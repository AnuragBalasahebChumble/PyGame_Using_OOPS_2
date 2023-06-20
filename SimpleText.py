# SimpleText class

import pygame
from pygame.locals import *

class SimpleText():
    def __init__(self, window, loc, value, textColor):
        pygame.font.init()   #  It will start Pygame font system.
        self.window = window
        self.loc = loc
        self.font = pygame.font.SysFont("Arial", 30)  # None indicates standard system font.
        self.textColor = textColor
        self.text = None  # So the call to setText below will
                          # force the creation of the text image
        self.setValue(value)  # set the initial text for drawing

    def setValue(self, newText):
        if self.text == newText:
            return  # Nothing to change
        self.text = newText
        self.textSurface = self.font.render(self.text, True, self.textColor)

    def draw(self):
        self.window.blit(self.textSurface, self.loc)
