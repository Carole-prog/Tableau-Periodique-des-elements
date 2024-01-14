# MACKOWIAK Carole
# MARQUIS Zoé

import pygame
from couleur import *
from donnees import *

def lettre(surface):
    ''' TSurface -> None
    dessine les lettres/symboles représentant chaque élément
    '''
    police = pygame.font.Font(None, 30)
    for i in data1:
        lettre = data1[i][0]
        positionx = data1[i][3]*70+35
        positiony = data1[i][4]*70+35
        texte = police.render(lettre, True, NOIR)
        text_rect_obj = texte.get_rect()
        text_rect_obj.center = (positionx, positiony)
        surface.blit(texte, text_rect_obj)
        
def nom(surface):
    ''' TSurface -> None
    dessine les noms complets de chaque élément
    '''
    police = pygame.font.Font(None, 15)
    for i in data1:
        nom = data1[i][1]
        positionx = data1[i][3]*70+35
        positiony = data1[i][4]*70+60
        texte = police.render(nom, True, NOIR)
        text_rect_obj = texte.get_rect()
        text_rect_obj.center = (positionx, positiony)
        surface.blit(texte, text_rect_obj)

def numato(surface):
    ''' TSurface -> None
    dessine le Z
    '''
    police = pygame.font.Font(None, 20)
    for i in data1.keys():
        num = str(i+1)
        positionx = data1[i][3]*70+55
        positiony = data1[i][4]*70+10
        texte = police.render(num, True, NOIR)
        text_rect_obj = texte.get_rect()
        text_rect_obj.center = (positionx, positiony)
        surface.blit(texte, text_rect_obj)
        
def masato(surface):
    ''' TSurface -> None
    dessine le Z
    '''
    police = pygame.font.Font(None, 12)
    for i in data1.keys():
        mas = data1[i][2]
        positionx = data1[i][3]*70+20
        positiony = data1[i][4]*70+10
        texte = police.render(mas, True, NOIR)
        text_rect_obj = texte.get_rect()
        text_rect_obj.center = (positionx, positiony)
        surface.blit(texte, text_rect_obj)              