import pygame
from game import Game
pygame.init()

# Générer la fenêtre de notre jeu
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))

# Chargement du background du jeu
background = pygame.image.load('assets/bg.jpg')

# Chargement du jeu
game = Game()

running = True

# Boucle tant que cette condition est vrai (tâche qui s'exécutera tant que le jeu sera actif)
while running:

    # Application de l'arrière-plan du jeu
    screen.blit(background, (0, -200))

    # Application de l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Récupération des projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # Application de l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # Vérification si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # Vérification de l'événement : "fermeture de fenêtre"
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # Détection de la touche du clavier actionnée par le joueur
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Détection si la touche Space est enclenchée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False