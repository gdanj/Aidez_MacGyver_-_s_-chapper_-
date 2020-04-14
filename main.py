import pygame
from constantes import *
pygame.init()


# ouvrire la fenetre
window = pygame.display.set_mode((cote_fenetre, cote_fenetre))
fond = pygame.image.load("pictures/background.png").convert()

pygame.display.flip()

#BOUCLE INFINIE
test = True



icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

#On parcourt la liste du niveau

			

#Boucle infinie
while test:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            test = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                print("Espace")
            if event.key == pygame.K_UP :
                print("Espace")
            if event.key == pygame.K_RIGHT :
                print("Espace")
            if event.key == pygame.K_DOWN :
                print("Espace")


    with open("map.txt", "r") as fichier:
	    structure_niveau = []
	    #On parcourt les lignes du fichier
	    for ligne in fichier:
	    	ligne_niveau = []
	    	#On parcourt les sprites (lettres) contenus dans le fichier
	    	for sprite in ligne:
	    		#On ignore les "\n" de fin de ligne
	    		if sprite != '\n':
	    			#On ajoute le sprite à la liste de la ligne
	    			ligne_niveau.append(sprite)
	    	#On ajoute la ligne à la liste du niveau
	    	structure_niveau.append(ligne_niveau)

    window.blit(fond, (0,0))
    mur = pygame.image.load(image_mur).convert()
    depart = pygame.image.load(image_depart).convert()
    arrivee = pygame.image.load(image_arrivee).convert_alpha()
    num_ligne = 0
    for ligne in structure_niveau:
        #On parcourt les listes de lignes
        num_case = 0
        for sprite in ligne:
            #On calcule la position réelle en pixels
            x = num_case * taille_sprite
            y = num_ligne * taille_sprite
            if sprite == 'm':		   #m = Mur
                window.blit(mur, (x,y))
            elif sprite == 'd':		   #d = Départ
                window.blit(depart, (x,y))
            elif sprite == 'a':		   #a = Arrivée
                window.blit(arrivee, (x,y))
            num_case += 1
        num_ligne += 1  
    
    pygame.display.flip()