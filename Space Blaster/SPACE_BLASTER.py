#SPACE BLASTER
import pygame
import os
import random
import time
import math
from pygame.constants import K_ESCAPE
from pygame.event import event_name
from pygame import mixer


pygame.init()
mixer.init()
pygame.font.init()
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

normal_end=(900,630)
resized_end=(1434,672)

width,height=0,0

FPS=10
intro_screen=pygame.image.load(os.path.join(r"Space Blaster\\Space Blaster\\intro_screen-01.jpg"))
background=pygame.image.load(os.path.join(r"Space Blaster\\Space Blaster\\game_screen-2.png"))
target=pygame.image.load(os.path.join(r"Space Blaster\\Space Blaster\\aestroid.png"))

window=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
transform_background=pygame.transform.scale(background,window.get_size())
transform_screen=pygame.transform.scale(intro_screen,window.get_size())

def tar():
    global tarwidth,tarheight
    tarwidth=random.randrange(85,100)
    tarheight=random.randrange(75,100)
    return tarwidth,tarheight

def draw(tar1):
    tar()
    a,b=window.get_size()
    transform_target=pygame.transform.scale(target,(tarwidth,tarheight))
    if tar1.x+tarwidth>a or tar1.y+tarheight>b:
        tar1.x=tar1.x-(tar1.x+tarwidth)
        tar1.y=tar1.y-(tar1.y+tarwidth)
    window.blit(transform_target,(tar1.x,tar1.y))
    pygame.display.update()

def main():
    mixer.Channel(2).play(mixer.Sound((os.path.join(r"Space Blaster\\Space Blaster\\game_music.wav"))),100)
    window=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
    pygame.display.set_caption((os.path.join("Space Blaster","SPACE BLASTER")))
    pygame.display.set_icon(target)
    window.blit(transform_screen,(0,0))
    pygame.display.update()
    pygame.time.delay(3000)
    window.blit(transform_background,(0,0))
    a,b=window.get_size()
    font=pygame.font.SysFont("Anton-Regular",40)
    rules=font.render("RULES",True,(255,255,255))
    c,d=rules.get_size()
    center=((a//2)-(c//2),((b//2)-(d//2)-(2*d)))
    window.blit(rules,(center))
    font=pygame.font.SysFont("Anton-Regular",30)
    textsurface1=font.render("HIT THE ASTEROIDS TO SCORE POINTS AND TO FIND YOUR ACCURACY",True,(255,255,255))
    c,d=textsurface1.get_size()
    center=((a//2)-(c//2),((b//2)-(d//2)-(d)))
    window.blit(textsurface1,(center))
    textsurface2=font.render("CLICK ON THE ASTEROID TO START THE GAME",True,(255,255,255))
    c,d=textsurface2.get_size()
    center=((a//2)-(c//2),((b//2)-(d//2)))
    window.blit(textsurface2,(center))
    textsurface3=font.render("YOU HAVE 15 ASTEROIDS AND 5 LIVES",True,(255,255,255))
    c,d=textsurface3.get_size()
    center=((a//2)-(c//2),((b//2)-(d//2)+d))
    window.blit(textsurface3,(center))
    textsurface4=font.render("PRESS SPACE TO PAUSE THE GAME",True,(255,255,255))
    c,d=textsurface4.get_size()
    center=((a//2)-(c//2),((b//2)-(d//2)+(2*d)))
    window.blit(textsurface4,(center))
    textsurface5=font.render("PRESS ESCAPE AT ANY TIME TO CLOSE THE GAME",True,(255,255,255))
    c,d=textsurface5.get_size()
    center=((a//2)-(c//2),((b//2)-(d//2)+(3*d)))
    window.blit(textsurface5,(center))
    font=pygame.font.SysFont("Anton-Regular",20)
    textsurface6=font.render("Developed By :- Adarsh Sarathy",True,(255,255,255))
    c,d=textsurface6.get_size()
    bottomcenter=((a//2)-(c//2),(b//2)-(d//2)+(12*d))#ybyuk
    window.blit(textsurface6,(bottomcenter))
    font=pygame.font.SysFont("Anton-Regular",30)
    pygame.display.update()
    clock=pygame.time.Clock()
    c,d=textsurface5.get_size()
    tar1=pygame.Rect((a//2)-(tar()[0])//2,((b//2)-(d//2)+(4*d)),tar()[0],tar()[-1])
    hits=-1
    misses=0
    run=True
    x=0
    y=0.4
    t=True
    while run:
        a,b=window.get_size()
        clock.tick(FPS)
        for event in pygame.event.get():
            while x==0:
                draw(tar1)
                t=True
                x=1
            lives=font.render(f"LIVES LEFT : {(5-misses)}",True,(255,255,255))
            c,d=lives.get_size()
            topright=(a-c,0)
            window.blit(lives,topright)
            pygame.display.update()
            keypress=pygame.key.get_pressed()
            if keypress[pygame.K_SPACE]:
                font=pygame.font.SysFont("Anton-Regular",40)
                pause=font.render("PAUSED",True,(255,255,255))
                font=pygame.font.SysFont("Anton-Regular",30)
                resume=font.render("CLICK THE ASTEROID TO RESUME",True,(255,255,255))
                escape=font.render("PRESS ESCAPE TO EXIT THE GAME",True,(255,255,255))
                c,d=pause.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)-d))
                window.blit(pause,(center))
                c,d=resume.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)))
                window.blit(resume,(center))
                c,d=escape.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)+d))
                window.blit(escape,(center))
                pygame.display.update()
                pygame.event.wait()
                pygame.display.update()
                keypress=pygame.key.get_pressed()
                if keypress[pygame.K_ESCAPE]:
                    run=False
                else:
                    hits-=1
            keypress=pygame.key.get_pressed()
            if keypress[pygame.K_ESCAPE]:
                run=False
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if hits==-1:
                    begin=time.time()
                mixer.Channel(2).set_volume(0.2)
                pos=pygame.mouse.get_pos()
                if 15<=hits>0 or misses!=5:
                    mixer.Channel(0).play(mixer.Sound((os.path.join(r"Space Blaster\\Space Blaster\\laser_sound.mp3"))))
                if hits==15 or misses==5:
                    mixer.Channel(0).pause()
                    mixer.Channel(1).pause()
                    mixer.Channel(2).pause()
                    mixer.Channel(3).pause()
                    mixer.Channel(4).pause()
                    mixer.Channel(5).play(mixer.Sound((os.path.join(r"Space Blaster\\Space Blaster\\retry.wav"))))
                    hits=-1
                    misses=-1
                    x=1
                    window.blit(pygame.transform.scale(background,(a,b)),(0,0))
                    pygame.display.update()
                    mixer.Channel(2).play(mixer.Sound((os.path.join(r"Space Blaster\\Space Blaster\\game_music.wav"))))
                else:
                    pass
                if pos[0] in range(tar1.x,tar1.x+tar()[0]) and pos[-1] in range(tar1.y,tar1.y+tar()[-1]):
                    a,b=window.get_size()
                    pygame.draw.line(window,"YELLOW",(128, 733),(pos),3)
                    pygame.draw.line(window,"YELLOW",(1409, 734),(pos),3)
                    pygame.display.update()
                    pygame.time.delay(100)
                    hits+=1
                    window.blit(pygame.transform.scale(background,(a,b)),(0,0))
                    tar1.x=random.randrange(resized_end[0])
                    tar1.y=random.randrange(resized_end[-1])
                    draw(tar1)
                else:
                    mixer.Channel(3).play(mixer.Sound((os.path.join(r"Space Blaster\\Space Blaster\\miss.wav"))))
                    mixer.Channel(3).set_volume(0.7)
                    a,b=window.get_size()
                    pygame.draw.line(window,"YELLOW",(128, 733),(pos),3)
                    pygame.draw.line(window,"YELLOW",(1409, 734),(pos),3)
                    pygame.display.update()
                    pygame.time.delay(100)
                    misses+=1
                    window.blit(pygame.transform.scale(background,(a,b)),(0,0))
                    tar1.x=random.randrange(resized_end[0])
                    tar1.y=random.randrange(resized_end[-1])
                    draw(tar1)
            if misses==5:
                if t:
                    end=time.time()
                    t=False
                timetake=str(round((end-begin),2))
                if float(timetake)>60.00:
                    timetake=timetake.replace(".","min ")
                else:
                    timetake+="sec"
                while x==1:
                    mixer.Channel(2).set_volume(0.04)
                    mixer.Channel(4).play(mixer.Sound((os.path.join(r"Space Blaster\\Space Blaster\\lose.wav"))))
                    pygame.time.delay(1500)
                    x+=1
                mixer.Channel(2).set_volume(y)
                window.blit(pygame.transform.scale(background,(a,b)),(0,0))
                font=pygame.font.SysFont("Anton-Regular",40)
                textsurface=font.render("YOU LOSE!!!",True,(255,255,255))
                font=pygame.font.SysFont("Anton-Regular",30)
                if hits>0:
                    accuracy=font.render(f"YOUR ACCURACY : {round(((hits-misses)/15)*100,2)}%",True,(255,255,255))
                else:
                    accuracy=font.render(f"YOUR ACCURACY : {0}%",True,(255,255,255))
                timetaken=font.render(f"TIME TAKEN : {timetake}",True,(255,255,255))
                retry=font.render("CLICK HERE TO TRY AGAIN",True,(255,255,255))
                escape=font.render("PRESS ESCAPE TO EXIT THE GAME",True,(255,255,255))
                c,d=textsurface.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)-(2*d)))
                window.blit(textsurface,(center))
                c,d=accuracy.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)-(d)))
                window.blit(accuracy,(center))
                c,d=timetaken.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)))
                window.blit(timetaken,(center))
                c,d=retry.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)+(d)))
                window.blit(retry,(center))
                c,d=escape.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)+(2*d)))
                window.blit(escape,(center))
                if y!=1:
                    y+=0.001
                pygame.display.update()
                # pygame.event.wait()
                keypress=pygame.key.get_pressed()
                if keypress[pygame.K_ESCAPE]:
                    run=False
            elif hits==15:
                if t:
                    end=time.time()
                    t=False
                timetake=str(round((end-begin),2))
                if float(timetake)>60.00:
                    timetake=timetake.replace(".","min ")
                else:
                    timetake+="sec"
                while x==1:
                    mixer.Channel(2).set_volume(0.04)
                    mixer.Channel(1).play(mixer.Sound((os.path.join(r"Space Blaster\\Space Blaster\\You_Win.mp3"))))
                    x+=1
                mixer.Channel(2).set_volume(y)
                window.blit(pygame.transform.scale(background,(a,b)),(0,0))
                font=pygame.font.SysFont("Anton-Regular",40)
                textsurface=font.render("YOU WIN!!!",True,(255,255,255))
                font=pygame.font.SysFont("Anton-Regular",30)
                accuracy=font.render(f"YOUR ACCURACY : {round(((hits-misses)/15)*100,2)}%",True,(255,255,255))
                timetaken=font.render(f"TIME TAKEN : {timetake}",True,(255,255,255))
                retry=font.render("CLICK HERE TO TRY AGAIN",True,(255,255,255))
                escape=font.render("PRESS ESCAPE TO EXIT THE GAME",True,(255,255,255))
                c,d=textsurface.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)-(2*d)))
                window.blit(textsurface,(center))
                c,d=accuracy.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)-(d)))
                window.blit(accuracy,(center))
                c,d=timetaken.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)))
                window.blit(timetaken,(center))
                c,d=retry.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)+(d)))
                window.blit(retry,(center))
                c,d=escape.get_size()
                center=((a//2)-(c//2),((b//2)-(d//2)+(2*d)))
                window.blit(escape,(center))
                if y!=1:
                    y+=0.001
                pygame.display.update()
                # pygame.event.wait()
                keypress=pygame.key.get_pressed()
                if keypress[pygame.K_ESCAPE]:
                    run=False
    pygame.quit()
if __name__=="__main__":
    main()