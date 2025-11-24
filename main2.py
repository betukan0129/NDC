# Créé par beytu, le 02/11/2024 en Python 3.7
# Créé par beytu, le 15/10/2024 en Python 3.7
import pygame

import time
pygame.display.set_icon(pygame.image.load('OIP.jpg'))
###################################################----------------------------> FONCTION <----------------------------------------#################################################################################################
def importf(fichier):
    try:
        return pygame.image.load(f'assets/{fichier}')
    except:
        return False
def deplcolli(x,y,d=0,vel=30): # definition du vérification de collision sur deplacments choisis (par l'utilisateur) de la cellule (en utilisation)
    if d == 1:
        x = x - vel
        y = y - vel
        return [x, y]
    elif d == 2:
        x = x + vel
        y = y - vel
        return [x, y]
    elif d == 3:
        x = x - vel
        y = y + vel
        return [x, y]
    elif d == 4:
        x = x + vel
        y = y + vel
        return [x, y]
    else:
        return [x, y]


def coordim(fc,img,x,y,w,h): # définition d'une image (dimension, coordonnées et chargement de l'image)
    return [x,y,w,h],pygame.transform.scale(fc(img), (w,h))

def coulirsouris(x,y,w,h,x2,y2):
    if x <= x2 <= x+w and  y <= y2<= y+h:
        return True
    else:
        return False

def collsioson(tab,h,img): # verification de collision possible sur deplacment choisis
    r=0
    for i in tab:
        if h.mask.overlap(img[r],i):
            return True
        r+=1
    return False
def defcolli(tab,c,v): # définition de la vérification de collision possible sur deplacments pour chaque élément present entre les cellules, les murs,....
    t = []
    ind = 0
    for i in range(len(tab)//2):
        t.append((tab[ind]-c,tab[ind+1]-v))
        ind +=2
    return t

#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################

def accuil(img, c): #-------------------> ACCUEIL <----------------------------------#
    pygame.init()
    pygame.display.set_caption("Anti-virus")

    pygame.mixer.music.load("music/acc.mp3")

    pygame.mixer.music.play(-1)
    deci = 0
    screen = pygame.display.set_mode((960, 600))

    ic, acc = c(img, 'acc.jpg', 0, 0, 960, 600)
    fi, fleche = c(img, 'fleche.png', 430, 250, 72, 286)  # FLECHE
    im, master = c(img, 'master.png', 580, 250, 271, 61)  # MASTER
    ij, junior = c(img, 'junior.png', 100, 250, 269, 59)  # JUNIOR
    ie, expert = c(img, 'expert.png', 580, 335, 271, 61)  # EXPERT
    iss, starter = c(img, 'starter.png', 100, 335, 269, 61)  # STARTER
    ir, rond = c(img, 'rond.png', 270, 150, 381, 356)  # ROND
    ib, begin = c(img, 'begin.png', 0, 0, 45, 50)

    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        #AFFICHAGE DES IMAGES (FIXE pour l'accueil)
        screen.blit(acc, (ic[0], ic[1])) ; screen.blit(master, (im[0], im[1]));screen.blit(begin, (630, 255));screen.blit(expert, (ie[0], ie[1]))
        screen.blit(begin, (630, 340));screen.blit(junior, (ij[0], ij[1])),screen.blit(begin, (115, 255));screen.blit(starter, (iss[0], iss[1]))
        screen.blit(begin, (115, 340));screen.blit(rond, (ir[0], ir[1])) ; screen.blit(fleche, (fi[0],fi[1]))

        # DETECTION DU CLICK + OBTENTION DES COORDONNEES DU CLICK + RETOURNER LA VALEUR SELON LE NIIVEAU CHOISIS
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()

            if ie[0]+5<= pos_x <= ie[0]+ie[2] and  ie[1]+10 <= pos_y<= ie[1]+ie[3]:
                deci = 4
                running = False
            if iss[0]+5<= pos_x <= iss[0]+iss[2] and  iss[1]+10 <= pos_y<= iss[1]+iss[3]:
                deci = 1
                running = False
            if ij[0]+5<= pos_x <= ij[0]+ij[2] and  ij[1]-10 <= pos_y<= ij[1]+ij[3]:
                deci = 2
                running = False
            if im[0]+5<= pos_x <= im[0]+im[2] and  im[1]-10 <= pos_y<= im[1]+im[3]:
                deci = 3
                running = False

        pygame.display.flip()
    pygame.quit()
    return deci

#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################

def niv1(img,cordim,joueur,defcolli,collsioson): #-------------------> NIVEAU 1 <----------------------------------#
    pygame.init()
    pygame.display.set_caption("Anti-virus")
    pygame.mixer.music.load("music/niv1.mp3")
    pygame.mixer.music.play(-1)

    # JEU
    J1 = joueur() ; J1.img,J1.x,J1.y,J1.w,J1.h=img('Virus.png'),570,105,145,145 ; J1.img = pygame.transform.scale(J1.img, (J1.w,J1.h)) ;J1.mask =pygame.mask.from_surface(J1.img) ; j1 = [J1.x,J1.y]
    J2 = joueur() ; J2.img,J2.x,J2.y,J2.w,J2.h=img('Pink_2.png'),359,33,73,225  ; J2.img = pygame.transform.scale(J2.img, (J2.w,J2.h)) ;J2.mask=pygame.mask.from_surface(J2.img)  ; j2 = [J2.x,J2.y] ; g = [j1,j2];i = 0 ; h = J1 ; l = 1 ; d2 = 0 ; k,k2 = 0,0 ; h2 = J2

    #ELEMENT DE JEU
    ib, bakground = cordim(img,'back.png',0,0,960,600)  ; imt,maint = cordim(img,'download.jpg',0,0,960,600)    ;  irs,reset= cordim(img,'reset.png',60, 500,99,53)
    screen = pygame.display.set_mode((960, 600)) ; i2,img2 = cordim(img, '11.png',800,34,151,92)
    ip, imgp = cordim(img, 'pause.png', 790, 510,98,54) ; icc ,accc = cordim(img, 'loading.gif',0,0,960,600) ; xx1,xx2,xx3,xx4,yy1,yy2,yy3,yy4 = 110,210,750,290,100,560,100,-75
    ibg, begin = cordim(img,'begin.png',450,200,52,58) ; icr, accrond = coordim(img,'acce.png', 430,300,80,80) ; poss = 1000
    BLl =pygame.transform.scale(img("Blue_3.png"),(550,103))         # Chargement de l'image Blue_3
    BL = pygame.mask.from_surface(BLl)            # Création du masque pour Blue_3

    BL22 = pygame.transform.scale(img("Blue_13.png"), (103,450))       # Chargement de l'image Blue_13
    BL2 = pygame.mask.from_surface(BL22)
    key_states = {
        pygame.K_UP: False,
        pygame.K_DOWN: False,
        pygame.K_LEFT: False,
        pygame.K_RIGHT: False
    }
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        #AFFICHAGE
        screen.blit(BLl, (xx2,yy2));screen.blit(BL22, (xx3,yy3));screen.blit(BLl, (xx4,yy4)) ; screen.blit(BL22, (xx1,yy1))
        screen.blit(maint, (ib[0],ib[1])) ; screen.blit(bakground, (ib[0],ib[1])) ; screen.blit(reset,(irs[0],irs[1]))
        screen.blit(img2,(i2[0],i2[1])) ; screen.blit(J1.img,(g[0][0],g[0][1])) ; screen.blit(J2.img,(g[1][0],g[1][1]))
        screen.blit(imgp, (ip[0],ip[1])) ; screen.blit(accc, (icc[0]+poss,icc[1]+poss)) ; screen.blit(begin,(ibg[0]+poss,ibg[1]+poss)); screen.blit(accrond,(icr[0]+poss,icr[1]+poss))
        set_x = h2.x - h.x ; set_y = h2.y - h.y
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            print(pos_x,pos_y)
            if irs[0]<= pos_x <= irs[0]+irs[2] and  irs[1] <= pos_y<= irs[1]+irs[3]:
                rst = 'reset'
                running = False
        keys = pygame.key.get_pressed()
        set = (set_x,set_y)


        # DETECTION DU CLICK +
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            if ip[0] <= pos_x <= ip[0]+ip[1] and ip[1] <=pos_y<= ip[1]+ip[3]:
                poss = 0

            if ibg[0] <= pos_x <= ibg[0]+ibg[2] and ibg[1]<=pos_y <= ibg[1]+ibg[3]:

                poss=1000
            elif icr[0] <= pos_x <= icr[0]+icr[2] and icr[1] <= pos_y <= icr[1] + icr[3]:
                rst = 0
                running = False

                print(pos_x,pos_y)
        if keys[pygame.K_ESCAPE]:  #pour fermer le jeu
            running = False

        # SELECTION DE LA CELLULE
        if keys[pygame.K_0]:
                i =0 ; h = J1 ; l = 1 ; h2 = J2
        if keys[pygame.K_3]:
                i =1 ; h = J2 ; l = 0 ; h2 = J1
        if keys[pygame.K_UP] and not key_states[pygame.K_UP] and not key_states[pygame.K_LEFT]:
            c,v = deplcolli(k,k2,d=1,vel=71)
            s = defcolli([h2.x,h2.y,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4],c,v)

            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL]) == True:
                h.x,h.y = h.deplacer(vel=0,d=1) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:
                h.x,h.y = h.deplacer(vel=71,d=1) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            print(g[0][0],g[0][1],g[1][0],g[1][1])
            key_states[pygame.K_UP] = True
            key_states[pygame.K_LEFT] = True

        if keys[pygame.K_RIGHT] and not key_states[pygame.K_UP] and not key_states[pygame.K_RIGHT]:
            c,v = deplcolli(k,k2,d=2,vel=71)

            s = defcolli([h2.x,h2.y,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4],c,v)

            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL]) == True:
                h.x,h.y = h.deplacer(vel=0,d=2) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:

                h.x,h.y = h.deplacer(vel=71,d=2) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            key_states[pygame.K_UP] = True
            key_states[pygame.K_RIGHT] = True

        if keys[pygame.K_LEFT] and not key_states[pygame.K_DOWN] and not key_states[pygame.K_LEFT]:
            c,v = deplcolli(k,k2,d=3,vel=71)

            s = defcolli([h2.x,h2.y,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4],c,v)

            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL]) == True:
                h.x,h.y = h.deplacer(vel=0,d=3) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:
                h.x,h.y = h.deplacer(vel=71,d=3) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            key_states[pygame.K_DOWN] = True
            key_states[pygame.K_LEFT] = True

        if keys[pygame.K_DOWN]  and not key_states[pygame.K_DOWN] and not key_states[pygame.K_RIGHT]:
            c,v = deplcolli(k,k2,d=4,vel=71)

            s = defcolli([h2.x,h2.y,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4],c,v)

            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL]) == True:
                h.x,h.y = h.deplacer(vel=0,d=4) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:
                h.x,h.y = h.deplacer(vel=71,d=4) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            key_states[pygame.K_DOWN] = True
            key_states[pygame.K_RIGHT] = True
        image = img('R.png')
        if J1.x == 144 and J1.y == -37:
            rst = 0
            screen.blit(image, (240, 150))
            pygame.display.flip()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/win.mp3")
            pygame.mixer.music.play()

            start_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - start_time < 7000:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break

            pygame.display.flip()
            running = False
    # remettre en marche les touches (pour faire avancer qu'une fois)
        if not keys[pygame.K_UP]:
            key_states[pygame.K_UP] = False
        if not keys[pygame.K_DOWN]:
            key_states[pygame.K_DOWN] = False
        if not keys[pygame.K_LEFT]:
            key_states[pygame.K_LEFT] = False
        if not keys[pygame.K_RIGHT]:
            key_states[pygame.K_RIGHT] = False








        pygame.display.flip()
    pygame.quit()
    return rst

#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################

def niv2(img,cordim,jeu): #-------------------> NIVEAU 2 <----------------------------------#
    pygame.init()
    pygame.display.set_caption("Anti-virus")

    pygame.mixer.music.load("music/niv2.mp3")
    pygame.mixer.music.play(-1)

    # JEU
    J1 = jeu() ; J1.img,J1.x,J1.y,J1.w,J1.h=img('Virus.png'),300,405,125,125    ; J1.img = pygame.transform.scale(J1.img, (J1.w,J1.h))  ;J1.mask =pygame.mask.from_surface(J1.img)    ; j1 = [J1.x,J1.y]  ; h = J1
    J2 = jeu() ; J2.img,J2.x,J2.y,J2.w,J2.h=img('Pink_2.png'),359,33,63,215     ; J2.img = pygame.transform.scale(J2.img, (J2.w,J2.h)) ;J2.mask=pygame.mask.from_surface(J2.img)      ; j2 =[J2.x,J2.y]   ; i = 0    ; l = 1 ; d2 = 0 ; k,k2 = 0,0 ; h2 = J2
    J3 = jeu() ; J3.img,J3.x,J3.y,J3.w,J3.h=img('Orange_3.png'),389,297,182,108 ; J3.img = pygame.transform.scale(J3.img, (J3.w,J3.h)) ;J3.mask=pygame.mask.from_surface(J3.img)      ; j3 =[J3.x,J3.y]   ; g = [j1,j2,j3] ; h3 = J3

    # ELEMENT DE JEU
    ib, bakground = cordim(img,'back.png',0,0,960,600)  ; imt,maint = cordim(img,'download.jpg',0,0,960,600)    ;  irs,reset= cordim(img,'reset.png',60, 500,99,53)
    screen = pygame.display.set_mode((960, 600)) ; i2,img2 = cordim(img, '2.png',800,34,151,92) ; h3 = J3
    ip, imgp = cordim(img, 'pause.png', 790, 510,98,54) ; icc ,accc = cordim(img, 'loading.gif',0,0,960,600) ; xx1,xx2,xx3,xx4,yy1,yy2,yy3,yy4 = 110,210,750,290,100,560,100,-75
    ibg, begin = cordim(img,'begin.png',450,200,52,58) ; icr, accrond = coordim(img,'acce.png', 430,300,80,80) ; ico,coli= coordim(img,'obstacle.png',310,354,49,29) ; ico2,coli2 = coordim(img,'obstacle.png',604,354,49,29)
    ico3,coli3 = coordim(img,'obstacle.png',250,280,49,29)
    ico4,coli4 = coordim(img,'obstacle.png',225,145,49,29)
    BLl =pygame.transform.scale(img("Blue_3.png"),(550,103))        ; cm =pygame.mask.from_surface(coli)    ; cm2 =pygame.mask.from_surface(coli2) ;
    BL = pygame.mask.from_surface(BLl)                              ; cm3 =pygame.mask.from_surface(coli3) ; cm4 = pygame.mask.from_surface(coli4) ;

    BL22 = pygame.transform.scale(img("Blue_13.png"), (103,450))       # Chargement de l'image Blue_13
    BL2 = pygame.mask.from_surface(BL22)

    poss = 1000 # Elle permet de positionner le bouton 'reprendre' et le bouton 'accueil' (et en arrière plan, l'image de la pause du niveau)
    key_states = {
        pygame.K_UP: False,
        pygame.K_DOWN: False,
        pygame.K_LEFT: False,
        pygame.K_RIGHT: False
    }
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # AFFICHAGE
        screen.blit(BLl, (xx2,yy2));screen.blit(BL22, (xx3,yy3));screen.blit(BLl, (xx4,yy4)) ; screen.blit(BL22, (xx1,yy1))
        screen.blit(maint, (ib[0],ib[1])) ; screen.blit(bakground, (ib[0],ib[1])) ; screen.blit(reset,(irs[0],irs[1]))
        screen.blit(img2,(i2[0],i2[1])) ; screen.blit(J1.img,(g[0][0],g[0][1])) ; screen.blit(J2.img,(g[1][0],g[1][1])) ; screen.blit(J3.img,(J3.x,J3.y))
        screen.blit(imgp, (ip[0],ip[1]))
        screen.blit(coli,(ico[0],ico[1])) ; screen.blit(coli2, (ico2[0],ico2[1])) , screen.blit(coli3, (ico3[0],ico3[1])) ; screen.blit(coli4, (ico4[0],ico4[1]))
        screen.blit(accc, (icc[0]+poss,icc[1]+poss)) ; screen.blit(begin,(ibg[0]+poss,ibg[1]+poss)); screen.blit(accrond,(icr[0]+poss,icr[1]+poss))
        set_x = h2.x - h.x ; set_y = h2.y - h.y

        # LE RECOMMENCEMENT DU NIVEAU
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            print(pos_x,pos_y)
            if irs[0]<= pos_x <= irs[0]+irs[2] and  irs[1] <= pos_y<= irs[1]+irs[3]:
                rst = 'reset'
                running = False
        keys = pygame.key.get_pressed()
        set = (set_x,set_y)

        # CONDITION DE L'UTILISATEUR SUR LE NIVEAU
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            # PAUSE
            if ip[0] <= pos_x <= ip[0]+ip[1] and ip[1] <=pos_y<= ip[1]+ip[3]:
                poss = 0
            # CONTINUER
            if ibg[0] <= pos_x <= ibg[0]+ibg[2] and ibg[1]<=pos_y <= ibg[1]+ibg[3]:

                poss=1000
            # RETOUR à L'ACCUEIL
            elif icr[0] <= pos_x <= icr[0]+icr[2] and icr[1] <= pos_y <= icr[1] + icr[3]:
                rst = 0
                running = False

            print(pos_x,pos_y)
        if keys[pygame.K_ESCAPE]:  #pour fermer le jeu
            running = False

        # SELECTIONNEMENT D'UNE CELLULE
        if keys[pygame.K_0]:
                i =0 ; h = J1 ; l = 1 ; h2 = J2 ; h3 = J3 ; k = h.x ; k2 = h.y
        if keys[pygame.K_2]:
            i = 2 ; h = J3 ; h2 = J1 ; h3 = J2 ; k = h.x ; k2 = h.y
        if keys[pygame.K_3]:
                i =1 ; h = J2 ; l = 0 ; h2 = J1; h3 = J3 ; k = h.x ; k2 = h.y

        # CONDITION DE COLLISION ET DEPLACEMENTS
        if keys[pygame.K_UP] and not key_states[pygame.K_UP] and not key_states[pygame.K_LEFT]:
            c,v = deplcolli(k,k2,d=1,vel=71)
            s = defcolli([h2.x,h2.y,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4,h3.x,h3.y,ico[0],ico[1],ico2[0],ico2[1],ico3[0],ico3[1],ico4[0],ico4[1]],c,v)
            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL,h3.mask,cm,cm2,cm3,cm4]) == True:
                h.x,h.y = h.deplacer(vel=0,d=1) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:
                h.x,h.y = h.deplacer(vel=71,d=1) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            print(g[i][0],g[i][1])
            key_states[pygame.K_UP] = True
            key_states[pygame.K_LEFT] = True

        if keys[pygame.K_RIGHT] and not key_states[pygame.K_UP] and not key_states[pygame.K_RIGHT]:
            c,v = deplcolli(k,k2,d=2,vel=71)
            s = defcolli([h2.x,h2.y,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4,h3.x,h3.y,ico[0],ico[1],ico2[0],ico2[1],ico3[0],ico3[1],ico4[0],ico4[1]],c,v)
            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL,h3.mask,cm,cm2,cm3,cm4]) == True:
                h.x,h.y = h.deplacer(vel=0,d=2) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:

                h.x,h.y = h.deplacer(vel=71,d=2) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            key_states[pygame.K_UP] = True
            key_states[pygame.K_RIGHT] = True
            print(g[i][0],g[i][1])

        if keys[pygame.K_LEFT] and not key_states[pygame.K_DOWN] and not key_states[pygame.K_LEFT]:
            c,v = deplcolli(k,k2,d=3,vel=71)
            s = defcolli([h2.x,h2.y,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4,h3.x,h3.y,ico[0],ico[1],ico2[0],ico2[1],ico3[0],ico3[1],ico4[0],ico4[1]],c,v)
            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL,h3.mask,cm,cm2,cm3,cm4]) == True:
                h.x,h.y = h.deplacer(vel=0,d=3) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:
                h.x,h.y = h.deplacer(vel=71,d=3) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            key_states[pygame.K_DOWN] = True
            key_states[pygame.K_LEFT] = True
            print(g[i][0],g[i][1])

        if keys[pygame.K_DOWN]  and not key_states[pygame.K_DOWN] and not key_states[pygame.K_RIGHT]:
            c,v = deplcolli(k,k2,d=4,vel=71)
            s = defcolli([h2.x,h2.y,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4,h3.x,h3.y,ico[0],ico[1],ico2[0],ico2[1],ico3[0],ico3[1],ico4[0],ico4[1]],c,v)
            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL,h3.mask,cm,cm2,cm3,cm4]) == True:
                h.x,h.y = h.deplacer(vel=0,d=4) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:
                h.x,h.y = h.deplacer(vel=71,d=4) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y

            key_states[pygame.K_DOWN] = True
            key_states[pygame.K_RIGHT] = True
            print(g[i][0],g[i][1])
        image = img('R.png')
        # CONDITION DE VICTOIRE
        if J1.x == 158 and J1.y == -21:
            rst = 0
            screen.blit(image, (240, 150))
            pygame.display.flip()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/win.mp3")
            pygame.mixer.music.play()

            start_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - start_time < 7000:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break

            pygame.display.flip()
            running = False
    # remettre en marche les touches (pour faire avancer qu'une fois)
        if not keys[pygame.K_UP]:
            key_states[pygame.K_UP] = False
        if not keys[pygame.K_DOWN]:
            key_states[pygame.K_DOWN] = False
        if not keys[pygame.K_LEFT]:
            key_states[pygame.K_LEFT] = False
        if not keys[pygame.K_RIGHT]:
            key_states[pygame.K_RIGHT] = False








        pygame.display.flip()
    pygame.quit()
    return rst

#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################

def niv3(img,cordim,jeu,defcolli,collsioson):  #-------------------> NIVEAU 3 <----------------------------------#
    pygame.init()
    pygame.display.set_caption("Anti-virus")

    pygame.mixer.music.load("music/niv3.mp3")
    pygame.mixer.music.play(-1)

    # JEU
    J1 = jeu() ; J1.img,J1.x,J1.y,J1.w,J1.h=img('Virus.png'),300,405,125,125 ;   J1.img = pygame.transform.scale(J1.img, (J1.w,J1.h)) ; j1 = [J1.x,J1.y] ;J1.mask =pygame.mask.from_surface(J1.img)
    J2 = jeu() ; J2.img,J2.x,J2.y,J2.w,J2.h=img('Pink_2.png'),359,33,63,215;     J2.img = pygame.transform.scale(J2.img, (J2.w,J2.h)) ;J2.mask=pygame.mask.from_surface(J2.img)  ; j2 =[J2.x,J2.y]   ;i = 0 ; h = J1    ; l = 1 ; d2 = 0 ; k,k2 = 0,0 ; h2 = J2
    J3 = jeu() ; J3.img,J3.x,J3.y,J3.w,J3.h=img('Orange_3.png'),389,297,182,108; J3.img = pygame.transform.scale(J3.img, (J3.w,J3.h)) ;J3.mask=pygame.mask.from_surface(J3.img)  ; j3 =[J3.x,J3.y]
    J4 = jeu() ; J4.img,J4.x,J4.y,J4.w,J4.h=img('Blue_i2.png'),597,200,125,125; J4.img = pygame.transform.scale(J4.img, (J4.w,J4.h)) ;J4.mask=pygame.mask.from_surface(J4.img)   ; j4 =[J4.x,J4.y] ; g = [j1,j2,j3,j4] ; h4 = J4

    # ELEMENT DE JEU
    ib, bakground = cordim(img,'back.png',0,0,960,600)  ; imt,maint = cordim(img,'download.jpg',0,0,960,600)    ;  irs,reset= cordim(img,'reset.png',60, 500,99,53)
    screen = pygame.display.set_mode((960, 600)) ; i2,img2 = cordim(img, '2.png',800,34,151,92) ; h3 = J3
    ip, imgp = cordim(img, 'pause.png', 790, 510,98,54) ; icc ,accc = cordim(img, 'loading.gif',0,0,960,600) ; xx1,xx2,xx3,xx4,yy1,yy2,yy3,yy4 = 110,210,750,290,100,560,100,-75
    ibg, begin = cordim(img,'begin.png',450,200,52,58) ; icr, accrond = coordim(img,'acce.png', 430,300,80,80) ; poss = 1000 ; ico,coli= coordim(img,'obstacle2.png',310,354,49,29) ; ico2,coli2 = coordim(img,'obstacle.png',609,354,49,29) ; ico3,coli3 = coordim(img,'obstacle.png',299,215,49,29)
    BLl =pygame.transform.scale(img("Blue_3.png"),(550,103))        ; cm =pygame.mask.from_surface(coli) ; cm2 =pygame.mask.from_surface(coli2) ; cm3 = pygame.mask.from_surface(coli3)
    BL = pygame.mask.from_surface(BLl)                              ;ico4,coli4 = coordim(img,'obstacle.png',610,72,49,29);ico5,coli5 = coordim(img,'obstacle2.png',670,140,49,29);cm5 =pygame.mask.from_surface(coli5);cm4 =pygame.mask.from_surface(coli4)

    BL22 = pygame.transform.scale(img("Blue_13.png"), (103,450))       # Chargement de l'image Blue_13
    BL2 = pygame.mask.from_surface(BL22)
    pos_x,pos_y = 0,0
    key_states = {
        pygame.K_UP: False,
        pygame.K_DOWN: False,
        pygame.K_LEFT: False,
        pygame.K_RIGHT: False
    }
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # AFFICHAGE
        screen.blit(BLl, (xx2,yy2));screen.blit(BL22, (xx3,yy3));screen.blit(BLl, (xx4,yy4)) ; screen.blit(BL22, (xx1,yy1))
        screen.blit(maint, (ib[0],ib[1])) ; screen.blit(bakground, (ib[0],ib[1])) ; screen.blit(reset,(irs[0],irs[1]))
        screen.blit(img2,(i2[0],i2[1])) ; screen.blit(J1.img,(g[0][0],g[0][1])) ; screen.blit(J2.img,(g[1][0],g[1][1])) ; screen.blit(J3.img,(J3.x,J3.y)),screen.blit(J4.img,(J4.x,J4.y))
        screen.blit(imgp, (ip[0],ip[1]))
        screen.blit(coli,(ico[0],ico[1])) ; screen.blit(coli2, (ico2[0],ico2[1])); screen.blit(coli3, (ico3[0],ico3[1])); screen.blit(coli4, (ico4[0],ico4[1])); screen.blit(coli5, (ico5[0],ico5[1]))
        screen.blit(accc, (icc[0]+poss,icc[1]+poss)) ; screen.blit(begin,(ibg[0]+poss,ibg[1]+poss)); screen.blit(accrond,(icr[0]+poss,icr[1]+poss))
        set_x = h2.x - h.x ; set_y = h2.y - h.y
        pos_x,pos_y=0,0

        # DETECTION DU CLICK + OBTENTION DE SA POSITION (pos_x et pos_y)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            print(pos_x,pos_y)

            # RECOMMENCEMENT DU NIVEAU
            if irs[0]<= pos_x <= irs[0]+irs[2] and  irs[1] <= pos_y<= irs[1]+irs[3]:
                rst = 'reset'
                running = False

        keys = pygame.key.get_pressed()
        set = (set_x,set_y)

        # DETECTION DU CLICK + OBTENTION DE SA POSITION (pos_x et pos_y)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()

        # CONDITION DE L'UTILISATEUR SUR LE NIVEAU
        #PAUSE
        if ip[0] <= pos_x <= ip[0]+ip[1] and ip[1] <=pos_y<= ip[1]+ip[3]:
            poss = 0
        # CONTINUER
        if ibg[0] <= pos_x <= ibg[0]+ibg[2] and ibg[1]<=pos_y <= ibg[1]+ibg[3]:

            poss=1000
        # RETOUR A L ACCUEIL
        elif icr[0] <= pos_x <= icr[0]+icr[2] and icr[1] <= pos_y <= icr[1] + icr[3]:
            rst = 0
            running = False

            print(pos_x,pos_y)
        if keys[pygame.K_ESCAPE]:  #pour fermer le jeu
            running = False

        # SELECTION DE LA CELLULE
        if keys[pygame.K_0]:
                i =0 ; h = J1  ; h2 = J2 ; h3 = J3 ; h4 = J4 ; k = h.x ; k2 = h.y
        if keys[pygame.K_1]:
                i =3 ; h = J4  ; h2 = J2 ; h3 = J3 ; h4 = J1 ; k = h.x ; k2 = h.y
        if keys[pygame.K_2]:
                i = 2 ; h = J3 ; h2 = J1 ; h3 = J2 ; h4 = J4 ;  k = h.x ; k2 = h.y
        if keys[pygame.K_3]:
                i =1 ; h = J2 ;  h2 = J1; h3 = J3 ; h4 = J4 ; k = h.x ; k2 = h.y

        # CONDITION DE COLLISION ET DEPLACEMENENTS
        if keys[pygame.K_UP] and not key_states[pygame.K_UP] and not key_states[pygame.K_LEFT]:
            c,v = deplcolli(k,k2,d=1,vel=71)
            s = defcolli([h2.x+10,h2.y+10,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4,h3.x,h3.y,ico[0],ico[1],ico2[0],ico2[1],h4.x,h4.y,ico3[0],ico3[1],ico4[0],ico4[1],ico5[0],ico5[1]],c,v) # PREVENTION D UNE COLLISION SUR DEPLACEMENTS
            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL,h3.mask,cm,cm2,h4.mask, cm3,cm4,cm5]) == True: # DETECTION D UNE COLLISION DE LA PREVENTION
                h.x,h.y = h.deplacer(vel=0,d=1) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:
                h.x,h.y = h.deplacer(vel=71,d=1) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            print(g[i][0],g[i][1])
            key_states[pygame.K_UP] = True
            key_states[pygame.K_LEFT] = True

        if keys[pygame.K_RIGHT] and not key_states[pygame.K_UP] and not key_states[pygame.K_RIGHT]:
            c,v = deplcolli(k,k2,d=2,vel=71)

            s = defcolli([h2.x+10,h2.y+10,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4,h3.x,h3.y,ico[0],ico[1],ico2[0],ico2[1],h4.x,h4.y,ico3[0],ico3[1],ico4[0],ico4[1],ico5[0],ico5[1]],c,v) # PREVENTION D UNE COLLISION SUR DEPLACEMENTS

            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL,h3.mask,cm,cm2,h4.mask, cm3,cm4,cm5]) == True: # DETECTION D UNE COLLISION DE LA PREVENTION
                h.x,h.y = h.deplacer(vel=0,d=2) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:

                h.x,h.y = h.deplacer(vel=71,d=2) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            key_states[pygame.K_UP] = True
            key_states[pygame.K_RIGHT] = True
            print(g[i][0],g[i][1])

        if keys[pygame.K_LEFT] and not key_states[pygame.K_DOWN] and not key_states[pygame.K_LEFT]:
            c,v = deplcolli(k,k2,d=3,vel=71)


            s = defcolli([h2.x+10,h2.y+10,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4,h3.x,h3.y,ico[0],ico[1],ico2[0],ico2[1],h4.x,h4.y,ico3[0],ico3[1],ico4[0],ico4[1],ico5[0],ico5[1]],c,v) # PREVENTION D UNE COLLISION SUR DEPLACEMENTS
            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL,h3.mask,cm,cm2,h4.mask, cm3,cm4,cm5]) == True: # DETECTION D UNE COLLISION DE LA PREVENTION

                h.x,h.y = h.deplacer(vel=0,d=3) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:
                h.x,h.y = h.deplacer(vel=71,d=3) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            key_states[pygame.K_DOWN] = True
            key_states[pygame.K_LEFT] = True
            print(g[i][0],g[i][1])
        if keys[pygame.K_DOWN]  and not key_states[pygame.K_DOWN] and not key_states[pygame.K_RIGHT]:
            c,v = deplcolli(k,k2,d=4,vel=71)
            s = defcolli([h2.x+10,h2.y+10,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4,h3.x,h3.y,ico[0],ico[1],ico2[0],ico2[1],h4.x,h4.y,ico3[0],ico3[1],ico4[0],ico4[1],ico5[0],ico5[1]],c,v) # PREVENTION D UNE COLLISION SUR DEPLACEMENTS
            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL,h3.mask,cm,cm2,h4.mask, cm3,cm4,cm5]) == True: # DETECTION D UNE COLLISION DE LA  PREVENTION
                h.x,h.y = h.deplacer(vel=0,d=4) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:
                h.x,h.y = h.deplacer(vel=71,d=4) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y

            key_states[pygame.K_DOWN] = True
            key_states[pygame.K_RIGHT] = True
            print(g[i][0],g[i][1])

        image = img('R.png')
        # CONDITION DE VICTOIRE
        if J1.x == 158 and J1.y == -21:
            rst = 0
            screen.blit(image, (240, 150))
            pygame.display.flip()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/win.mp3")
            pygame.mixer.music.play()

            start_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - start_time < 7000:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break

            pygame.display.flip()
            running = False
    # remettre en marche les touches (pour faire avancer qu'une fois)
        if not keys[pygame.K_UP]:
            key_states[pygame.K_UP] = False
        if not keys[pygame.K_DOWN]:
            key_states[pygame.K_DOWN] = False
        if not keys[pygame.K_LEFT]:
            key_states[pygame.K_LEFT] = False
        if not keys[pygame.K_RIGHT]:
            key_states[pygame.K_RIGHT] = False








        pygame.display.flip()
    pygame.quit()
    return rst

#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################

def niv4(img,cordim,colli,defcolli,jeu):  #-------------------> NIVEAU 4 <----------------------------------#
    pygame.init()
    pygame.display.set_caption("Anti-virus")
    pygame.mixer.music.load("music/niv4.mp3")

    pygame.mixer.music.play(-1)

    # JEU
    J1 = jeu();J1.img,J1.x,J1.y,J1.w,J1.h=img('Virus.png'),300,405,125,125 ; J1.img = pygame.transform.scale(J1.img, (J1.w,J1.h))                                               ; j1 = [J1.x,J1.y] ;J1.mask =pygame.mask.from_surface(J1.img)
    J2 = jeu() ; J2.img,J2.x,J2.y,J2.w,J2.h=img('Pink_2.png'),380,33,61,212; J2.img = pygame.transform.scale(J2.img, (J2.w,J2.h)) ;J2.mask=pygame.mask.from_surface(J2.img)     ; j2 =[J2.x,J2.y]   ;i = 0 ;  d2 = 0 ; k,k2 = 0,0
    J3 = jeu() ; J3.img,J3.x,J3.y,J3.w,J3.h=img('Orange_3.png'),389,297,182,108; J3.img = pygame.transform.scale(J3.img, (J3.w,J3.h)) ;J3.mask=pygame.mask.from_surface(J3.img) ; j3 =[J3.x,J3.y]
    J4 = jeu() ; J4.img,J4.x,J4.y,J4.w,J4.h=img('Blue_i2.png'),597,200,125,125; J4.img = pygame.transform.scale(J4.img, (J4.w,J4.h)) ;J4.mask=pygame.mask.from_surface(J4.img)  ; j4 =[J4.x,J4.y] ; g = [j1,j2,j3,j4]
    h = J1 ; h2 = J2 ; h3 = J3 ; h4 = J4

    # ELEMENT DE JEU
    ib, bakground = cordim(img,'back.png',0,0,960,600)  ; imt,maint = cordim(img,'download.jpg',0,0,960,600)    ;  irs,reset= cordim(img,'reset.png',60, 500,99,53)
    screen = pygame.display.set_mode((960, 600)) ; i2,img2 = cordim(img, '2.png',800,34,151,92) ; h3 = J3
    ip, imgp = cordim(img, 'pause.png', 790, 510,98,54) ; icc ,accc = cordim(img, 'loading.gif',0,0,960,600)    ; xx1,xx2,xx3,xx4,yy1,yy2,yy3,yy4 = 110,210,750,290,100,560,100,-75
    ibg, begin = cordim(img,'begin.png',450,200,52,58)  ; icr, accrond = coordim(img,'acce.png', 430,300,80,80) ; poss = 1000 ;
    ico,coli= coordim(img,'obstacle2.png',310,354,49,29)
    ico2,coli2 = coordim(img,'obstacle.png',609,354,49,29)
    ico3,coli3 = coordim(img,'obstacle.png',299,215,49,29)
    ico4,coli4 = coordim(img,'obstacle.png',610,72,49,29)
    ico5,coli5 = coordim(img,'obstacle.png',670,140,49,29)
    BLl =pygame.transform.scale(img("Blue_3.png"),(550,103))        ; cm =pygame.mask.from_surface(coli) ; cm2 =pygame.mask.from_surface(coli2) ; cm3 = pygame.mask.from_surface(coli3)
    BL = pygame.mask.from_surface(BLl)                              ;cm5 =pygame.mask.from_surface(coli5);cm4 =pygame.mask.from_surface(coli4)
    ico6,coli6 = coordim(img,'obstacle2.png',615,505,49,29);cm6 =pygame.mask.from_surface(coli6)
    BL22 = pygame.transform.scale(img("Blue_13.png"), (103,450))       # Chargement de l'image Blue_13
    BL2 = pygame.mask.from_surface(BL22)
    pos_x,pos_y = 0,0
    key_states = {
        pygame.K_UP: False,
        pygame.K_DOWN: False,
        pygame.K_LEFT: False,
        pygame.K_RIGHT: False
    }
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # AFFICHAGE
        screen.blit(BLl, (xx2,yy2));screen.blit(BL22, (xx3,yy3));screen.blit(BLl, (xx4,yy4)) ; screen.blit(BL22, (xx1,yy1)) # Collision extérieur
        screen.blit(maint, (ib[0],ib[1])) ; screen.blit(bakground, (ib[0],ib[1])) ; screen.blit(reset,(irs[0],irs[1]))
        screen.blit(img2,(i2[0],i2[1])) ; screen.blit(J1.img,(g[0][0],g[0][1])) ; screen.blit(J2.img,(g[1][0],g[1][1])) ; screen.blit(J3.img,(J3.x,J3.y)),screen.blit(J4.img,(J4.x,J4.y))
        screen.blit(imgp, (ip[0],ip[1]))
        screen.blit(coli,(ico[0],ico[1])) ; screen.blit(coli2, (ico2[0],ico2[1])); screen.blit(coli3, (ico3[0],ico3[1])); screen.blit(coli4, (ico4[0],ico4[1])); screen.blit(coli5, (ico5[0],ico5[1]))
        screen.blit(coli6, (ico6[0],ico6[1]))
        screen.blit(accc, (icc[0]+poss,icc[1]+poss)) ; screen.blit(begin,(ibg[0]+poss,ibg[1]+poss)); screen.blit(accrond,(icr[0]+poss,icr[1]+poss))
        set_x = h2.x - h.x ; set_y = h2.y - h.y
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            print(pos_x,pos_y)
            if irs[0]<= pos_x <= irs[0]+irs[2] and  irs[1] <= pos_y<= irs[1]+irs[3]:
                rst = 'reset'
                running = False

        keys = pygame.key.get_pressed()
        set = (set_x,set_y)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
        # PAUSE
        if ip[0] <= pos_x <= ip[0]+ip[1] and ip[1] <=pos_y<= ip[1]+ip[3]:
            poss = 0
        # CONTINUER
        if ibg[0] <= pos_x <= ibg[0]+ibg[2] and ibg[1]<=pos_y <= ibg[1]+ibg[3]:

            poss=1000
        # RETOUR A L ACCUEIL
        elif icr[0] <= pos_x <= icr[0]+icr[2] and icr[1] <= pos_y <= icr[1] + icr[3]:
            rst = 0
            running = False

            print(pos_x,pos_y)
        if keys[pygame.K_ESCAPE]:  #pour fermer le jeu
            running = False

        # SELECCTION DE LA CELLULE
        if keys[pygame.K_0]:
                i =0 ; h = J1  ; h2 = J2 ; h3 = J3 ; h4 = J4 ; k = h.x ; k2 = h.y
        if keys[pygame.K_1]:
                i =3 ; h = J4  ; h2 = J2 ; h3 = J3 ; h4 = J1 ; k = h.x ; k2 = h.y
        if keys[pygame.K_2]:
                i = 2 ; h = J3 ; h2 = J1 ; h3 = J2 ; h4 = J4 ;  k = h.x ; k2 = h.y
        if keys[pygame.K_3]:
                i =1 ; h = J2 ;  h2 = J1; h3 = J3 ; h4 = J4 ; k = h.x ; k2 = h.y

        #Condition de déplacements et déplacements
        if keys[pygame.K_UP] and not key_states[pygame.K_UP] and not key_states[pygame.K_LEFT]:
            c,v = deplcolli(k,k2,d=1,vel=71) # PREVENTION DE DEPLACMENT

            s = defcolli([h2.x+10,h2.y+10,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4,h3.x,h3.y,ico[0],ico[1],ico2[0],ico2[1],h4.x,h4.y,ico3[0],ico3[1],ico4[0],ico4[1],ico5[0],ico5[1],ico6[0],ico6[1]],c,v) # PREVENTION D UNE COLLISION SUR DEPLACEMENTS

            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL,h3.mask,cm,cm2,h4.mask,cm3,cm4,cm5,cm6]) == True: # DETECTION D UNE COLLISION DE LA PREVENTION
                h.x,h.y = h.deplacer(vel=0,d=1) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y # PAS DE DEPLACEMENT
            else:
                h.x,h.y = h.deplacer(vel=71,d=1) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y # DEPLACEMENT POSSIBLE
            print(g[i][0],g[i][1])
            key_states[pygame.K_UP] = True
            key_states[pygame.K_LEFT] = True

        if keys[pygame.K_RIGHT] and not key_states[pygame.K_UP] and not key_states[pygame.K_RIGHT]:
            c,v = deplcolli(k,k2,d=2,vel=71)

            s = defcolli([h2.x+10,h2.y+10,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4,h3.x,h3.y,ico[0],ico[1],ico2[0],ico2[1],h4.x,h4.y,ico3[0],ico3[1],ico4[0],ico4[1],ico5[0],ico5[1],ico6[0],ico6[1]],c,v) # PREVENTION D UNE COLLISION SUR DEPLACEMENTS

            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL,h3.mask,cm,cm2,h4.mask,cm3,cm4,cm5,cm6]) == True: # DETECTION D UNE COLLISION DE LA PREVENTION
                h.x,h.y = h.deplacer(vel=0,d=2) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:

                h.x,h.y = h.deplacer(vel=71,d=2) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            key_states[pygame.K_UP] = True
            key_states[pygame.K_RIGHT] = True
            print(g[i][0],g[i][1])

        if keys[pygame.K_LEFT] and not key_states[pygame.K_DOWN] and not key_states[pygame.K_LEFT]:
            c,v = deplcolli(k,k2,d=3,vel=71)

            s = defcolli([h2.x+10,h2.y+10,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4,h3.x,h3.y,ico[0],ico[1],ico2[0],ico2[1],h4.x,h4.y,ico3[0],ico3[1],ico4[0],ico4[1],ico5[0],ico5[1],ico6[0],ico6[1]],c,v) # PREVENTION D UNE COLLISION SUR DEPLACEMENTS

            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL,h3.mask,cm,cm2,h4.mask,cm3,cm4,cm5,cm6]) == True: # DETECTION D UNE COLLISION DE LA PREVENTION
                h.x,h.y = h.deplacer(vel=0,d=3) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:
                h.x,h.y = h.deplacer(vel=71,d=3) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            key_states[pygame.K_DOWN] = True
            key_states[pygame.K_LEFT] = True
            print(g[i][0],g[i][1])

        if keys[pygame.K_DOWN]  and not key_states[pygame.K_DOWN] and not key_states[pygame.K_RIGHT]:
            c,v = deplcolli(k,k2,d=4,vel=71)

            s = defcolli([h2.x+10,h2.y+10,xx1,yy1,xx2,yy2,xx3,yy3,xx4,yy4,h3.x,h3.y,ico[0],ico[1],ico2[0],ico2[1],h4.x,h4.y,ico3[0],ico3[1],ico4[0],ico4[1],ico5[0],ico5[1],ico6[0],ico6[1]],c,v) # PREVENTION D UNE COLLISION SUR DEPLACEMENTS

            if collsioson(s,h,[h2.mask,BL2,BL,BL2,BL,h3.mask,cm,cm2,h4.mask,cm3,cm4,cm5,cm6]) == True: # DETECTION D UNE COLLISION DE LA PREVENTION
                h.x,h.y = h.deplacer(vel=0,d=4) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y
            else:
                h.x,h.y = h.deplacer(vel=71,d=4) ; g[i][0],g[i][1] = h.x,h.y ; k,k2 = h.x, h.y

            key_states[pygame.K_DOWN] = True
            key_states[pygame.K_RIGHT] = True
            print(g[i][0],g[i][1])

        image = img('R.png')
        # CONDITION DE VICTOIRE
        if J1.x == 158 and J1.y == -21:
            rst = 0
            screen.blit(image, (240, 150))
            pygame.display.flip()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/win.mp3")
            pygame.mixer.music.play()

            start_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - start_time < 7000:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break

            pygame.display.flip()
            running = False
    # remettre en marche les touches (pour faire avancer qu'une fois)
        if not keys[pygame.K_UP]:
            key_states[pygame.K_UP] = False
        if not keys[pygame.K_DOWN]:
            key_states[pygame.K_DOWN] = False
        if not keys[pygame.K_LEFT]:
            key_states[pygame.K_LEFT] = False
        if not keys[pygame.K_RIGHT]:
            key_states[pygame.K_RIGHT] = False








        pygame.display.flip()
    pygame.quit()
    return rst



