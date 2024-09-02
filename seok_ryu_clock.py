# -*- coding: utf-8 -*-

import pygame
from math import pi, cos, sin, radians
import datetime
from pygame import gfxdraw

WIDTH, HEIGHT = 1920, 1080
center = (WIDTH / 2, HEIGHT / 2)
clock_radius = 400

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SEOK RYU Clock")
clock = pygame.time.Clock()
FPS = 60

CLOCK = (33,35,57)
BACKGROUND = (217,215,211)
RED = (255, 0, 0)
YELLOW = (196,166,0)

fonts = pygame.font.get_fonts()
print(fonts)


def numbers(number, size, position):
    font = pygame.font.Font("Dubai-Regular.ttf", size)
    text = font.render(number, True, CLOCK)
    text_rect = text.get_rect(center=(position))
    screen.blit(text, text_rect)

def write_text(text, size, position, font_file, text_rotate_degrees=0, align="center"):
    font = pygame.font.Font(font_file, size)
    text_surface = font.render(text, True, CLOCK)

    if text_rotate_degrees != 0:
        text_surface = pygame.transform.rotate(text_surface, text_rotate_degrees)

    text_rect = text_surface.get_rect()

    if align == "right":
        text_rect.topright = position
    elif align == 'left':
        text_rect.topleft = position
    else:
        text_rect.center = position
    screen.blit(text_surface, text_rect)


def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + WIDTH / 2, -(y - HEIGHT / 2)


def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(BACKGROUND)

        # draw circles
        pygame.draw.circle(screen, CLOCK, center, clock_radius - 10, 5)

        outer_radius = clock_radius - 2
        pygame.draw.circle(screen, CLOCK, center, outer_radius, 2)
        gfxdraw.aacircle(screen, int(center[0]), int(center[1]), outer_radius + 1, CLOCK)
        gfxdraw.aacircle(screen, int(center[0]), int(center[1]), outer_radius, CLOCK)
        gfxdraw.aacircle(screen, int(center[0]), int(center[1]), outer_radius - 1, CLOCK)

        # 24h
        for number in range(1, 25):
            numbers(str(number), 40, polar_to_cartesian(clock_radius + 30, number * 15))

    
        # hour hooks
        for number in range(0, 360, 15):
            width = 3
            if (number % 90) == 0:
                width = 6
            pygame.draw.line(screen, CLOCK, polar_to_cartesian(clock_radius + 8, number), polar_to_cartesian(clock_radius - 22, number), width)


        # draw dividing lines
        rb = 15
        thetas = [5*rb, 6*rb, 9*rb, 12*rb-6, 12*rb+6, 15*rb, 18*rb, 20*rb, 21*rb, 22*rb]
        for theta in thetas:
            pygame.draw.line(screen, CLOCK, polar_to_cartesian(clock_radius - 30, theta), polar_to_cartesian(clock_radius - 335, theta), 2)

        write_text(u"꿈나라", 56, (WIDTH / 2 + 100, HEIGHT / 2 - 150), "1HoonSaemaulundong\HoonSaemaulundong Regular.ttf")
        write_text(u"아침", 40, (WIDTH / 2 + 350, HEIGHT / 2 - 60), "1HoonSaemaulundong\HoonSaemaulundong Regular.ttf", 8, 'right')
        write_text(u"게임하기", 40, (WIDTH / 2 + 330, HEIGHT / 2 + 60), "1HoonSaemaulundong\HoonSaemaulundong Regular.ttf", 360-23, 'right')
        write_text(u"멍때리기", 40, (WIDTH / 2 + 160, HEIGHT / 2 + 195), "1HoonSaemaulundong\HoonSaemaulundong Regular.ttf", 360-65, 'right')
        write_text(u"점심", 40, (WIDTH / 2 + 22, HEIGHT / 2 + 285), "1HoonSaemaulundong\HoonSaemaulundong Regular.ttf", 360-90, 'right')
        write_text(u"TV보기", 40, (WIDTH / 2 - 80, HEIGHT / 2 + 215), "1HoonSaemaulundong\HoonSaemaulundong Regular.ttf", 65, 'right')
        write_text(u"낮잠자기", 40, (WIDTH / 2 - 200, HEIGHT / 2 + 60), "1HoonSaemaulundong\HoonSaemaulundong Regular.ttf", 20, 'right')
        write_text(u"만화방 가기", 40, (WIDTH / 2 - 170, HEIGHT / 2 - 105), "1HoonSaemaulundong\HoonSaemaulundong Regular.ttf", 360-15, 'right')
        write_text(u"자유시간", 40, (WIDTH / 2 - 165, HEIGHT / 2 - 225), "1HoonSaemaulundong\HoonSaemaulundong Regular.ttf", 360-37, 'right')
        write_text(u"고려", 40, (WIDTH / 2 - 163, HEIGHT / 2 - 290), "1HoonSaemaulundong\HoonSaemaulundong Regular.ttf", 360-53, 'right')

        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour

        r = 130
        theta = (hour + minute / 60 + second / 3600) * (360 / 24)
        pygame.draw.line(screen, CLOCK, center, polar_to_cartesian(r, theta), 14)

        
        r = 280
        theta = (minute + second / 60) * (360 / 60)
        pygame.draw.line(screen, CLOCK, center, polar_to_cartesian(r, theta), 10)

        r = 340
        theta = second * (360 / 60)
        pygame.draw.line(screen, YELLOW, center, polar_to_cartesian(r, theta), 4)
        pygame.draw.line(screen, YELLOW, center, polar_to_cartesian(80, (theta + 180) % 360), 4)



        # play button
        gfxdraw.filled_circle(screen, int(center[0]), int(center[1]), clock_radius - 350, YELLOW)
        pygame.draw.circle(screen, CLOCK, center, clock_radius - 350 - 1, 2)
        write_text("PLAY", 46, (WIDTH/2, HEIGHT/2 + 3), "calibri-font-family\calibri-bold.ttf")

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()

main()
