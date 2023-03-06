import pygame
import sys

import asset
import var
import const

import sceneplay
import sceneedit
import scenetitle

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.screen_size)
    pygame.display.set_caption('2D Platformer Editor')
    var.clock = pygame.time.Clock()

    load_font()
    load_image()

def load_font():
    pygame.font.init()
    const.Font.title = pygame.font.Font('Font/neodgm.ttf', 32)
    const.Font.main_1 = pygame.font.Font('Font/neodgm.ttf', 24)
    const.Font.main_2 = pygame.font.Font('Font/neodgm.ttf', 16)

def load_image():
    asset.Img.Icon.new = pygame.image.load('Image/Icon/New.png')
    asset.Img.Icon.load = pygame.image.load('Image/Icon/Load.png')
    asset.Img.Icon.save = pygame.image.load('Image/Icon/Save.png')
    asset.Img.Icon.pointer = pygame.image.load('Image/Icon/Pointer.png')
    asset.Img.Icon.brush = pygame.image.load('Image/Icon/Brush.png')
    asset.Img.Icon.erase = pygame.image.load('Image/Icon/Erase.png')
    asset.Img.Icon.close = pygame.image.load('Image/Icon/Close.png')
    asset.Img.Icon.move = pygame.image.load('Image/Icon/Move.png')

    asset.Img.Icon.block = pygame.image.load('Image/Icon/Block.png')
    asset.Img.Icon.coin = pygame.image.load('Image/Icon/Coin.png')
    asset.Img.Icon.flag = pygame.image.load('Image/Icon/Flag.png')
    asset.Img.Icon.background = pygame.image.load('Image/Icon/Background.png')

    asset.Img.Icon.play = pygame.image.load('Image/Icon/Play.png')
    asset.Img.Icon.pause = pygame.image.load('Image/Icon/Pause.png')
    asset.Img.Icon.stop = pygame.image.load('Image/Icon/Stop.png')

    asset.Img.player = pygame.image.load('Image/Player.png')

    asset.Img.block[1] = pygame.image.load('Image/Block/Dirt.png')
    asset.Img.block[2] = pygame.image.load('Image/Block/Grass.png')

def main():
    while True:
        var.clock.tick(60)
        input_handle()
        loop_scene()

def loop_scene():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'edit':
        sceneedit.loop()

    elif var.scene == 'play':
        sceneplay.loop()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            button = event.button

            if var.scene == 'title':
                scenetitle.mouse_up(x, y, button)

            elif var.scene == 'edit':
                sceneedit.mouse_up(x, y, button)

            elif var.scene == 'play':
                sceneplay.mouse_up(x, y, button)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            button = event.button

            if var.scene == 'edit':
                sceneedit.mouse_down(x, y, button)

        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()

            if var.scene == 'edit':
                sceneedit.mouse_motion(x, y)

        if event.type == pygame.KEYDOWN:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_down(key)
            
            elif var.scene == 'edit':
                sceneedit.key_down(key)

            elif var.scene == 'play':
                sceneplay.key_down(key)

init()
main()