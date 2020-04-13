import pygame

pygame.init()


# ouvrire la fenetre
window = pygame.display.set_mode((400, 400))
fond = pygame.image.load("background.jpg")
window.blit(fond, (0,0))

pygame.display.flip()

#BOUCLE INFINIE
test = True

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
        