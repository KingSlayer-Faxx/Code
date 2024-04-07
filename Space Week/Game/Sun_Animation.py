import pygame
import os

window=pygame.display.set_mode((0,0),pygame.FULLSCREEN)


def draw_sun(x):
    sun=[pygame.transform.scale(pygame.image.load(os.path.join(r"Space Week\Assets\Sun_1.jpeg")),(window.get_size())),pygame.transform.scale(pygame.image.load(os.path.join(r"Space Week\Assets\Sun_2.jpeg")),(window.get_size())),pygame.transform.scale(pygame.image.load(os.path.join(r"Space Week\Assets\Sun_3.jpeg")),(window.get_size()))]
    for image in sun:
        window.blit(image,(0,0))
        pygame.display.update()
        pygame.time.delay(1000)
        x+=1
        if x==len(sun):
            break

def main():
    x=0
    clock=pygame.time.Clock()
    FPS=1
    while True:
        clock.tick(FPS)
        draw_sun(x)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key--pygame.K_ESCAPE:
                    quit()


if __name__=="__main__":
    main()