import pygame

pygame.init()


# ouvrire la fenetre
window = pygame.display.set_mode((400, 400))
fond = pygame.image.load("background.jpg")
window.blit(fond, (0,0))

pygame.display.flip()

#BOUCLE INFINIE
test = True


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
        