import pygame
pygame.init()
#iniciando o pygame;
pygame.mixer.music.load('ex021.mp3')
#carregando arquivo;
pygame.mixer.music.play()
#dando play;
input()
pygame.event.wait()
#comando para pausar assim que arquivo terminar;

