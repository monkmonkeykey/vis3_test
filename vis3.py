import pygame
import sys

def reproducir_video(pantalla, ruta_video):
    reproductor = pygame.movie.Movie(ruta_video)
    reproductor.set_display(pantalla, (0, 0, 1920, 1080))
    reproductor.play()

def main():
    pygame.init()
    pygame.display.set_caption("Reproducción de Video en Pantalla Extendida")
    pantalla1 = pygame.display.set_mode((1920, 1080))
    pantalla2 = pygame.display.set_mode((1920, 1080))
    reproductor1 = reproducir_video(pantalla1, "/home/frank/Desktop/vis3/vis_3--en.mov")
    reproductor2 = reproducir_video(pantalla2, "/home/frank/Desktop/vis3/vis_3--pl.mov")
    clock = pygame.time.Clock()
    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

