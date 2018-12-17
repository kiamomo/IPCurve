import pygame

pygame.init()
keys = pygame.key.get_pressed()

run = True
while run:
    print("yay")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        run = False
        run1 = True

run1 = False
while run1:
    print("blab")

pygame.quit()