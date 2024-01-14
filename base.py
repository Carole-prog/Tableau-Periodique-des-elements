# MACKOWIAK Carole
# MARQUIS Zoé

import pygame
from couleur import *
from donnees import *

def cases(surface):
    ''' TSurface -> None
    dessine les cases sans texte '''
    for element in data1.keys():
        if data1[element][5] == 'Indéfinie':
            coul = GRIS
        elif data1[element][5] == 'Halogène':
            coul = ROSE
        elif data1[element][5] == 'Actinide':
            coul = VERTF
        elif data1[element][5] == 'Métal alcalino-terreux':
            coul = BLEU
        elif data1[element][5] == 'Métal alcalin':
            coul = MARINE
        elif data1[element][5] == 'Gaz noble':
            coul = VIOLET
        elif data1[element][5] == 'Métalloïde':
            coul = SANG
        elif data1[element][5] == 'Métal pauvre':
            coul = ORANGE
        elif data1[element][5] == 'Lanthanide':
            coul = VERT
        elif data1[element][5] == 'Métal de transition':
            coul = JAUNE
        elif data1[element][5] == 'Non-métal':
            coul = ROUGE
            
        pygame.draw.rect(surface,coul,[data1[element][3]*70, data1[element][4]*70, 70,70])
        
def legende(surface):
    ''' TSurface -> None
    dessine la légende : couleur-famille
    '''
    famille = ['Métal alcalin','Métal alcalino-terreux','Métal de transition',
               'Métal pauvre','Non-métal','Métalloïde','Halogène','Gaz noble',
               'Lanthanide','Actinide','Indéfinie']
    colors = [MARINE,BLEU,JAUNE,ORANGE,ROUGE,SANG,ROSE,VIOLET,VERT,VERTF,GRIS]
    police = pygame.font.Font(None, 30)
    interligne = 0           
    for i in range(len(famille)):
        col = colors[i]
        pygame.draw.rect(surface,col,[1475,85+interligne,300,30])
        positionx = 1625
        positiony = 100+interligne
        texte = police.render(famille[i], False, NOIR)
        text_rect_obj = texte.get_rect()
        text_rect_obj.center = (positionx, positiony)
        surface.blit(texte, text_rect_obj)
        interligne += 30