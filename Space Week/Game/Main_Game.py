import pygame
import os


pygame.init()


window=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
width,height=window.get_size()
# print(width,height)
def draw_welcome_screen():
    width,height=window.get_size()
    welcome_screen=pygame.transform.scale(pygame.image.load(os.path.join(r"Space Week\Assets\Welcome_Screen.jpg")),(width,height))
    window.blit(welcome_screen,(0,0))
    pygame.display.update()
def draw_background():
    width,height=window.get_size()
    background=pygame.transform.scale(pygame.image.load(os.path.join(r"Space Week\Assets\Background.jpg")),(width,height))
    window.blit(background,(0,0))
    pygame.display.update()
def draw_rocket(x=150,y=150,width=window.get_size()[0],height=window.get_size()[-1],centre=True):
    rocket=pygame.transform.scale(pygame.image.load(os.path.join(r"Space Week\\Assets\\Rocket.png")),(x,y))
    if centre==True:
        window.blit(rocket,((width//2)-(x//2),height))
        # window.blit(rocket((width//2)-(x//2),(height//2)-(y//2)))
    else:
        window.blit(rocket,((width//2)-(x//2),height))
    pygame.display.update()
def write():
    font=pygame.font.SysFont("Anton-Regular",40)
    
clock=pygame.time.Clock()
FPS=15
def main():
    ws=0
    while True:
        clock.tick(FPS)
        while ws==0:
            draw_welcome_screen()
            ws+=1
        for event in pygame.event.get():
            pygame.event.wait()
            if event.type==pygame.QUIT:
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    quit()
                if event.key==pygame.K_w:
                    speed=5
            if event.type==pygame.MOUSEBUTTONDOWN:
                draw_background()
                draw_rocket(height=900-150,centre=False)


if __name__=="__main__":
    main()