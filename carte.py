# MACKOWIAK Carole
# MARQUIS Zoé

import pygame
from couleur import *
from donnees import *

def carte(nb,surface):
    '''int,TSurface -> None
    dessine la carte correspondant à un élément en position nb
    '''
    if data1[nb][5] == 'Indéfinie':
            coul = GRIS
    elif data1[nb][5] == 'Halogène':
            coul = ROSE
    elif data1[nb][5] == 'Actinide':
            coul = VERTF
    elif data1[nb][5] == 'Métal alcalino-terreux':
            coul = BLEU
    elif data1[nb][5] == 'Métal alcalin':
            coul = MARINE
    elif data1[nb][5] == 'Gaz noble':
            coul = VIOLET
    elif data1[nb][5] == 'Métalloïde':
            coul = SANG
    elif data1[nb][5] == 'Métal pauvre':
            coul = ORANGE
    elif data1[nb][5] == 'Lanthanide':
            coul = VERT
    elif data1[nb][5] == 'Métal de transition':
            coul = JAUNE
    elif data1[nb][5] == 'Non-métal':
            coul = ROUGE
    
    pygame.draw.rect(surface,coul,[1500,450,250,340])
    pygame.draw.rect(surface,NOIR,[1500,450,250,340],3)
    
    # symbole chimique
    police = pygame.font.Font(None, 100)
    lettre = data1[nb][0]
    positionx = 1625
    positiony = 525
    texte = police.render(lettre, True, NOIR)
    text_rect_obj = texte.get_rect()
    text_rect_obj.center = (positionx, positiony)
    surface.blit(texte, text_rect_obj)
    
    police = pygame.font.Font(None, 20)
    
    # nom
    lettre = 'Nom : '
    positionx = 1590
    positiony = 600
    texte = police.render(lettre, True, NOIR)
    text_rect_obj = texte.get_rect()
    text_rect_obj.center = (positionx, positiony)
    surface.blit(texte, text_rect_obj)
    
    lettre = data1[nb][1]
    positionx = 1650
    positiony = 600
    texte = police.render(lettre, True, NOIR)
    text_rect_obj = texte.get_rect()
    text_rect_obj.center = (positionx, positiony)
    surface.blit(texte, text_rect_obj)
    
    # famille
    lettre = 'Groupe : '
    positionx = 1570
    positiony = 630
    texte = police.render(lettre, True, NOIR)
    text_rect_obj = texte.get_rect()
    text_rect_obj.center = (positionx, positiony)
    surface.blit(texte, text_rect_obj)
    
    lettre = data1[nb][5]
    positionx = 1670
    positiony = 630
    texte = police.render(lettre, True, NOIR)
    text_rect_obj = texte.get_rect()
    text_rect_obj.center = (positionx, positiony)
    surface.blit(texte, text_rect_obj)
    
    # num ato
    lettre = 'Numéro atomique : '
    positionx = 1600
    positiony = 660
    texte = police.render(lettre, True, NOIR)
    text_rect_obj = texte.get_rect()
    text_rect_obj.center = (positionx, positiony)
    surface.blit(texte, text_rect_obj)
    
    lettre = str(nb+1)
    positionx = 1680
    positiony = 660
    texte = police.render(lettre, True, NOIR)
    text_rect_obj = texte.get_rect()
    text_rect_obj.center = (positionx, positiony)
    surface.blit(texte, text_rect_obj)
    
    # masse ato
    lettre = 'Masse atomique : '
    positionx = 1600
    positiony = 690
    texte = police.render(lettre, True, NOIR)
    text_rect_obj = texte.get_rect()
    text_rect_obj.center = (positionx, positiony)
    surface.blit(texte, text_rect_obj)
    
    lettre = data1[nb][2]
    positionx = 1690
    positiony = 690
    texte = police.render(lettre, True, NOIR)
    text_rect_obj = texte.get_rect()
    text_rect_obj.center = (positionx, positiony)
    surface.blit(texte, text_rect_obj)
    
    # config electronique
    lettre = 'Configuration électronique :'
    positionx = 1625
    positiony = 720
    texte = police.render(lettre, True, NOIR)
    text_rect_obj = texte.get_rect()
    text_rect_obj.center = (positionx, positiony)
    surface.blit(texte, text_rect_obj)
    
    lettre = data2[nb][0]
    positionx = 1625
    positiony = 750
    texte = police.render(lettre, True, NOIR)
    text_rect_obj = texte.get_rect()
    text_rect_obj.center = (positionx, positiony)
    surface.blit(texte, text_rect_obj)    
    
    
    
    
    
    
    
    
    
    