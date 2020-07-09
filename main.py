import pygame
pygame.init()

# générer la fenêtre de notre jeu
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))

# Chargement du background du jeu
background = pygame.image.load('assets/bg.jpg')

running = True

# boucle tant que cette condition est vrai (tâche qui s'exécutera tant que le jeu sera actif)
while running:

    # Application de l'arrière-plan du jeu
    screen.blit(background, (0, -200))

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # pour vérifier que l'événement est : "fermeture de fenêtre"
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")