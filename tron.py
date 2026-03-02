import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Test")

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Simple fill to show window is working
        WIN.fill((255, 255, 255)) # Fill with white
        pygame.display.update() # Update the display

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
