import pygame_textinput
import pygame
import os

pygame.init()
def name():
    try:
        textinput = pygame_textinput.TextInput()

        icon=pygame.image.load(os.path.join("name_icon.png"))
        background=pygame.image.load(os.path.join("Background.jfif"))
        screen = pygame.display.set_mode((1536,800),pygame.FULLSCREEN)
        transform_background=pygame.transform.scale(background,screen.get_size())
        screen.blit(transform_background,(0,0))
        pygame.display.set_caption("ENTER YOUR NAME")
        pygame.display.set_icon(icon)
        clock = pygame.time.Clock()

        while True:
            screen.fill((225, 225, 225))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    file=open("NAMES.txt","r")
                    data=file.read()
                    if word not in data:
                        file=open("NAMES.txt","a")
                        file.write(word+"\n")
                        file.close()
                        print(word)
                        exit()
                    else:
                        exit()
            word=textinput.update(events)
            word=(word[-1]).replace("Enter Your Name:","")
            screen.blit(textinput.get_surface(), (10,10))
            pygame.display.update()
            clock.tick(30)
    except:
        pass
# name()