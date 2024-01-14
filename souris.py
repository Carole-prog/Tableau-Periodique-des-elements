# MACKOWIAK Carole
# MARQUIS Zoé

import pygame
import carte

def pos(surface):
    ''' Retourne le nbre correspondant aux données de l'élément dans le tableau si la souris se trouve dessus
    sinon retourne -1
    '''
    x,y = pygame.mouse.get_pos()
    nbr = -1
    # colonne 1
    if 70<x<140:
        if 70<y<140:
            nbr =0
        elif 140<y<210:
            nbr =2
        elif 210<y<280:
            nbr =10
        elif 280<y<350:
            nbr =18
        elif 350<y<420:
            nbr =36
        elif 420<y<490:
            nbr =54
        elif 490<y<560:
            nbr = 86
    # colonne 18
    if 1260<x<1330:
        if 70<y<140:
            nbr =1
        elif 140<y<210:
            nbr =9
        elif 210<y<280:
            nbr =17
        elif 280<y<350:
            nbr =35
        elif 350<y<420:
            nbr =53
        elif 420<y<490:
            nbr =85
        elif 490<y<560:
            nbr = 117
    # colonne 2
    elif 140<x<210:
        if 140<y<210:
            nbr =3
        elif 210<y<280:
            nbr =11
        elif 280<y<350:
            nbr =19
        elif 350<y<420:
            nbr =37
        elif 420<y<490:
            nbr =55
        elif 490<y<560:
            nbr = 87            
    # colonne 13
    elif 910<x<980:
        if 140<y<210:
            nbr =4
        elif 210<y<280:
            nbr =12
        elif 280<y<350:
            nbr =30
        elif 350<y<420:
            nbr =48
        elif 420<y<490:
            nbr =80
        elif 490<y<560:
            nbr = 112
    # colonne 14
    elif 980<x<1050:
        if 140<y<210:
            nbr =5
        elif 210<y<280:
            nbr =13
        elif 280<y<350:
            nbr =31
        elif 350<y<420:
            nbr =49
        elif 420<y<490:
            nbr =81
        elif 490<y<560:
            nbr = 113
    # colonne 15
    elif 1050<x<1120:
        if 140<y<210:
            nbr =6
        elif 210<y<280:
            nbr =14
        elif 280<y<350:
            nbr =32
        elif 350<y<420:
            nbr =50
        elif 420<y<490:
            nbr =82
        elif 490<y<560:
            nbr = 114
    # colonne 16
    elif 1120<x<1190:
        if 140<y<210:
            nbr =7
        elif 210<y<280:
            nbr =15
        elif 280<y<350:
            nbr =33
        elif 350<y<420:
            nbr =51
        elif 420<y<490:
            nbr =83
        elif 490<y<560:
            nbr = 115
    # colonne 17
    elif 1190<x<1260:
        if 140<y<210:
            nbr =8
        elif 210<y<280:
            nbr =16
        elif 280<y<350:
            nbr =34
        elif 350<y<420:
            nbr =52
        elif 420<y<490:
            nbr =84
        elif 490<y<560:
            nbr = 116
    # colonne 3
    elif 210<x<280:
        if 280<y<350:
            nbr =20
        elif 350<y<420:
            nbr =38
    # colonne 4
    elif 280<x<350:
        if 280<y<350:
            nbr =21
        elif 350<y<420:
            nbr =39
        elif 420<y<490:
            nbr =71
        elif 490<y<560:
            nbr = 103
        # colonne 5
    elif 350<x<420:
        if 280<y<350:
            nbr =22
        elif 350<y<420:
            nbr =40
        elif 420<y<490:
            nbr =72
        elif 490<y<560:
            nbr = 104
        # colonne 6
    elif 420<x<490:
        if 280<y<350:
            nbr =23
        elif 350<y<420:
            nbr =41
        elif 420<y<490:
            nbr =73
        elif 490<y<560:
            nbr = 105
        # colonne 7
    elif 490<x<560:
        if 280<y<350:
            nbr =24
        elif 350<y<420:
            nbr =42
        elif 420<y<490:
            nbr =74
        elif 490<y<560:
            nbr = 106
        # colonne 8
    elif 560<x<630:
        if 280<y<350:
            nbr =25
        elif 350<y<420:
            nbr =43
        elif 420<y<490:
            nbr =75
        elif 490<y<560:
            nbr = 107
        # colonne 9
    elif 630<x<700:
        if 280<y<350:
            nbr =26
        elif 350<y<420:
            nbr =44
        elif 420<y<490:
            nbr =76
        elif 490<y<560:
            nbr = 108
        # colonne 10
    elif 700<x<770:
        if 280<y<350:
            nbr =27
        elif 350<y<420:
            nbr =45
        elif 420<y<490:
            nbr =77
        elif 490<y<560:
            nbr = 109
        # colonne 11
    elif 770<x<840:
        if 280<y<350:
            nbr =28
        elif 350<y<420:
            nbr =46
        elif 420<y<490:
            nbr =78
        elif 490<y<560:
            nbr = 110
        # colonne 12
    elif 840<x<910:
        if 280<y<350:
            nbr =29
        elif 350<y<420:
            nbr =47
        elif 420<y<490:
            nbr =79
        elif 490<y<560:
            nbr = 111
# bloc f
    # ligne 8
    if 630<y<700:
        if 280<x<350:
            nbr =56
        elif 350<x<420:
            nbr =57
        elif 420<x<490:
            nbr =58
        elif 490<x<560:
            nbr =59
        elif 560<x<630:
            nbr =60
        elif 630<x<700:
            nbr =61
        elif 700<x<770:
            nbr =62
        elif 770<x<840:
            nbr =63
        elif 840<x<910:
            nbr =64
        elif 910<x<980:
            nbr =65
        elif 980<x<1050:
            nbr =66
        elif 1050<x<1120:
            nbr =67
        elif 1120<x<1190:
            nbr =68
        elif 1190<x<1260:
            nbr =69
        elif 1260<x<1330:
            nbr =70
# ligne 9
    if 700<y<770:
        if 280<x<350:
            nbr =88
        elif 350<x<420:
            nbr =89
        elif 420<x<490:
            nbr =90
        elif 490<x<560:
            nbr =91
        elif 560<x<630:
            nbr =92
        elif 630<x<700:
            nbr =93
        elif 700<x<770:
            nbr =94
        elif 770<x<840:
            nbr =95
        elif 840<x<910:
            nbr =96
        elif 910<x<980:
            nbr =97
        elif 980<x<1050:
            nbr =98
        elif 1050<x<1120:
            nbr =99
        elif 1120<x<1190:
            nbr =100
        elif 1190<x<1260:
            nbr =101
        elif 1260<x<1330:
            nbr =102        
            
    return nbr