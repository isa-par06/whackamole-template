import pygame
import random


def draw_grid(screen):
    #horizontal lines
    for i in range(1,21):
        pygame.draw.line(screen, "black", (0, 32*i), (640, 32*i))
    #vertical lines
    for i in range(1, 21):
        pygame.draw.line(screen, "black", (32*i, 0), (32*i, 512))




def main():
    try:
        pygame.init()
        mole_image = pygame.image.load(
            "../../../OneDrive/Documents/COP3502C Labs & Projects/Mole/whackamole-template/mole.png")
        # You can draw the mole with this snippet:
        screen = pygame.display.set_mode((640, 512))
        #screen.blit(mole_image, mole_image.get_rect(topleft=(0,0)))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    user_x, user_y = event.pos
                    if (user_x >= mole_x and user_x <= (mole_x + 32)) and (user_y >= mole_y and user_y <= (mole_y + 32)):
                        mole_x = random.randrange(0, 640//32) * 32
                        mole_y = random.randrange(0, 512//32) * 32
            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
            pygame.display.update()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
