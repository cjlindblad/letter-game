import glob
import os
import pygame

def main():

    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("minimal program")

    # create a surface on screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

    font = pygame.font.SysFont(None, SCREEN_HEIGHT)
    
    # read image files
    image_data = list(map(lambda f: (os.path.basename(f)[0].lower(), f), glob.glob(os.path.join("images", "*.jpg"))))

    # game state
    running = True
    letters = [name for (name, _) in image_data]
    images = [pygame.transform.scale(pygame.image.load(image_path), (SCREEN_WIDTH, SCREEN_HEIGHT)) for (_, image_path) in image_data]
    current_letter_index = 0

    # main loop
    while running:
        current_letter = letters[current_letter_index % len(letters)]
        current_image = images[current_letter_index % len(letters)]

        screen.fill((255, 255, 255))
        screen.blit(current_image, (0, 0))

        # event handling, gets all events from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.KEYDOWN:
                # change the value to False, to exit the main loop
                if event.key == ord(current_letter):
                    current_letter_index += 1
                if event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    running = False

        text = font.render(current_letter.upper(), True, (127, 222, 234))
        text.set_alpha(235)
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(text, text_rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()
