import pygame
from pygame.sprite import Group
from settings import settings
from game_starts import GameStats
from ship import Ship
from alien import Alien
import game_fuctions as gf
from scoreboard import scoreboard
from button import Button
pygame.init()
ai_settings=settings()
screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
pygame.display.set_caption("Alien Game")
play_button=Button(ai_settings,screen,"play")
stats=GameStats(ai_settings)
sb=scoreboard(ai_settings,screen,stats)
ship=Ship(ai_settings,screen)
bullets=Group()
aliens=Group()
gf.creat_fleet(ai_settings,screen,ship,aliens)
running=True
while running:
    gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
    if stats.game_active:
     ship.update()
     bullets.update()
     gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
     gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
    gf.update_screen(ai_settings,screen,stats,sb,ship,bullets,aliens,play_button)

             
