#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))

    def run(self):
        pygame.display.set_caption("It works!")
        running = True
        while running:
            menu = Menu(self.window)
            menu.run()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()