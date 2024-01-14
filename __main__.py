# MACKOWIAK Carole
# MARQUIS Zoé

import pygame
import math

from couleur import * 
from donnees import * # données à mettre dans le tableau
import base # dessin des cases et de la légende
import ecriture # remplissage de toutes les cases
import carte # dessin de la carte correspondant à l'element sur lequel est la souris
import souris # position de la souris faisant apparaitre la bonne carte
 
def main():
    ''' Fonction principale
    None -> None
    '''
    
    pygame.init()
     
    horloge = pygame.time.Clock()
    
    # titre
    pygame.display.set_caption('Tableau périodique des éléments chimiques.')
    
    # icone
    image_icon = pygame.image.load('periodic.png')
    pygame.display.set_icon(image_icon)
    #Fenêtre
    largeur = 1900
    hauteur = 1000
    surface = pygame.display.set_mode((largeur, hauteur))
    
    #Bannière du Menu
    image_menu = pygame.image.load('Menu.png')
    image_menu = pygame.transform.scale(image_menu,(1000,1000))
    image_menu_rect = image_menu.get_rect()
    
    #Repositionnement du Menu
    image_menu_rect.x = math.ceil(surface.get_width()/5)    
    
    def button_1(msg,x,y,w,h,inactivecolor,activecolor,action=None):
        ''' Gérer le bouton LANCER du menu '''
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Bouton Lancer    
        if x + w > mouse[0] > x and y + h > mouse[1] >y:
            pygame.draw.rect(surface, activecolor , (x,y,w,h))
            if click[0]==1 and action !=None:
                action()
        else :
            pygame.draw.rect(surface, inactivecolor , (x,y,w,h))
            
        TextMenu = pygame.font.Font(None,100)
        textSurf, textRect = text_objects(msg,TextMenu)
        textRect.center =((x+(w/2)),(y+(h/2)))
        surface.blit(textSurf,textRect)
        
    def button_2(msg,x,y,w,h,inactivecolor,activecolor,action=None):
        ''' Gérer le bouton CREDITS du menu '''
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Bouton Credits    
        if x + w > mouse[0] > x and y + h > mouse[1] >y:
            pygame.draw.rect(surface, activecolor , (x,y,w,h))
            if click[0]==1 and action !=None:
                action()
        else :
            pygame.draw.rect(surface, inactivecolor , (x,y,w,h))
            
        TextMenu = pygame.font.Font(None,100)
        textSurf, textRect = text_objects(msg,TextMenu)
        textRect.center =((x+(w/2)),(y+(h/2)))
        surface.blit(textSurf,textRect)
        
    def button_3(msg,x,y,w,h,inactivecolor,activecolor,action=None):
        ''' Gérer le bouton QUITTER du menu '''
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Bouton Quitter
        if x + w > mouse[0] > x and y + h > mouse[1] >y:
            pygame.draw.rect(surface, activecolor , (x,y,w,h))
            if click[0]==1 and action !=None:
                action()
        else :
            pygame.draw.rect(surface, inactivecolor , (x,y,w,h))
            
        TextMenu = pygame.font.Font(None,100)
        textSurf, textRect = text_objects(msg,TextMenu)
        textRect.center =((x+(w/2)),(y+(h/2)))
        surface.blit(textSurf,textRect)
        
    def quitTab():
        ''' Fonction qui quitte proprement '''
        pygame.quit()
        quit()
     
    def text_objects(text,font):
        ''' Initialisation du texte '''
        textSurface = font.render(text,True,NOIR)
        return textSurface , textSurface.get_rect()
    
    def Tab_intro():
        ''' Affichage du menu '''
        intro = True
        while intro :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            surface.fill(BLANC)
            
            surface.blit(image_menu,image_menu_rect)
            
            button_1("Lancer",1200,450,500,100,ROSE,SANG,Tab_loop)
            button_2("Credits",1200,600,500,100,ROSE,SANG,Tab_credits)
            button_3("Quitter",1200,750,500,100,ROSE,SANG,quitTab)
            
            
            pygame.display.update()
            horloge.tick(15)
            
    def Tab_credits():
        ''' Affichage des crédits '''
        credit = True
        while credit :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            surface.fill(BLANC)
            
            Titre =pygame.font.Font(None,115)
            TextSurf, TextRect = text_objects("CREDITS",Titre)
            TextRect.center =((largeur/2),(hauteur/4))
            surface.blit(TextSurf, TextRect)
            
            Nom =pygame.font.Font(None,50)
            Suf,rec = text_objects("MACKOWIAK Carole",Nom)
            rec.center=((largeur/2),(hauteur/3))
            surface.blit(Suf,rec)
            
            Nom =pygame.font.Font(None,50)
            Suf,rec = text_objects("MARQUIS Zoé",Nom)
            rec.center=((largeur/2),(hauteur/2.65))
            surface.blit(Suf,rec)
            
            button_1("Retour",50,850,500,100,ROSE,SANG,Tab_intro)
            pygame.display.update()
            horloge.tick(25)
            
            
    def Tab_loop():
        ''' Boucle principale du programme '''
        terminer = False
        while not terminer :
 
            for event in pygame.event.get() :
             
                if event.type == pygame.QUIT :
                    terminer = True
         
            surface.fill(BLANC)
        
            base.cases(surface)
            base.legende(surface)
            ecriture.lettre(surface)
            ecriture.nom(surface)
            ecriture.numato(surface)
            ecriture.masato(surface)
            res = souris.pos(surface)
            if res != -1:
                carte.carte(res,surface)
            
            button_1("Retour",600,850,250,100,ROSE,SANG,Tab_intro)
            pygame.display.update()
            horloge.tick(25)
            pygame.display.flip()
            
    Tab_intro()
    Tab_loop()
    pygame.quit()
 
 
if __name__ == '__main__':
    main()