import sys

import pygame
def startScreen():
    global sesame_surface,sesame_index
    sesame_index+=0.1
    if sesame_index>=len(sesame_list):sesame_index=0
    sesame_surface=sesame_list[int(sesame_index)]
pygame.init()
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption('PlayWords')
clock=pygame.time.Clock()

name_font=pygame.font.Font('font/AlloyInk-nRLyO.ttf',40)
name_surface=name_font.render('Play Words',True,'Black')
name_rect=name_surface.get_rect(center=(400,100))

#play text
play_font=pygame.font.Font(None,40)
play_surface=play_font.render('Press Space To Start',True,'#00827f')
play_rect=play_surface.get_rect(center=(410,300))


#character
x=150
y=180
#frame 1
sesame_1=pygame.image.load('images/starting/1.png').convert_alpha()
sesame_1=pygame.transform.scale(sesame_1,(x,y))
# sesame_1_rect=sesame_1.get_rect(center=(400,150))
#frame 2
sesame_2=pygame.image.load('images/starting/2.png').convert_alpha()
sesame_2=pygame.transform.scale(sesame_2,(x,y))
# sesame_2_rect=sesame_2.get_rect(center=(400,150))
#frame 3
sesame_3=pygame.image.load('images/starting/3.png').convert_alpha()
sesame_3=pygame.transform.scale(sesame_3,(x,y))
# sesame_3_rect=sesame_3.get_rect(center=(400,150))
#frame 4
sesame_4=pygame.image.load('images/starting/4.png').convert_alpha()
sesame_4=pygame.transform.scale(sesame_4,(x,y))
# sesame_4_rect=sesame_4.get_rect(center=(400,150))
#frame 5
sesame_5=pygame.image.load('images/starting/5.png').convert_alpha()
sesame_5=pygame.transform.scale(sesame_5,(x,y))
#frame 6
sesame_6=pygame.image.load('images/starting/6.png').convert_alpha()
sesame_6=pygame.transform.scale(sesame_6,(x,y))
#frame 7
sesame_7=pygame.image.load('images/starting/7.png').convert_alpha()
sesame_7=pygame.transform.scale(sesame_7,(x,y))
#frame 8
sesame_8=pygame.image.load('images/starting/8.png').convert_alpha()
sesame_8=pygame.transform.scale(sesame_8,(x,y))
#frame 9
sesame_9=pygame.image.load('images/starting/9.png').convert_alpha()
sesame_9=pygame.transform.scale(sesame_9,(x,y))
#frame 10
sesame_10=pygame.image.load('images/starting/10.png').convert_alpha()
sesame_10=pygame.transform.scale(sesame_10,(x,y))
#frame 11
sesame_11=pygame.image.load('images/starting/11.png').convert_alpha()
sesame_11=pygame.transform.scale(sesame_11,(x,y))
#frame 12
sesame_12=pygame.image.load('images/starting/12.png').convert_alpha()
sesame_12=pygame.transform.scale(sesame_12,(x,y))
#frame 13
sesame_13=pygame.image.load('images/starting/13.png').convert_alpha()
sesame_13=pygame.transform.scale(sesame_13,(x,y))
#frame 14
sesame_14=pygame.image.load('images/starting/14.png').convert_alpha()
sesame_14=pygame.transform.scale(sesame_14,(x,y))
#frame 15
sesame_15=pygame.image.load('images/starting/15.png').convert_alpha()
sesame_15=pygame.transform.scale(sesame_15,(x,y))
#frame 18
sesame_18=pygame.image.load('images/starting/18.png').convert_alpha()
sesame_18=pygame.transform.scale(sesame_18,(x,y))
#frame 20
sesame_20=pygame.image.load('images/starting/20.png').convert_alpha()
sesame_20=pygame.transform.scale(sesame_20,(x,y))
#frame 21
sesame_21=pygame.image.load('images/starting/21.png').convert_alpha()
sesame_21=pygame.transform.scale(sesame_21,(x,y))
#frame 23
sesame_23=pygame.image.load('images/starting/23.png').convert_alpha()
sesame_23=pygame.transform.scale(sesame_23,(x,y))
#frame 24
sesame_24=pygame.image.load('images/starting/24.png').convert_alpha()
sesame_24=pygame.transform.scale(sesame_24,(x,y))
#sesame_list
sesame_list=[sesame_1,sesame_2,sesame_3,sesame_4,sesame_5,
             sesame_6,sesame_7,sesame_8,sesame_9,sesame_10,
             sesame_11,sesame_12,sesame_13,sesame_14,sesame_15,
             sesame_18,sesame_20,sesame_20,
             sesame_21,sesame_23,sesame_24]
sesame_index=0
sesame_surface=sesame_list[sesame_index]

sesame_rect=sesame_surface.get_rect(center=(400,230))

game_active=False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    if game_active:
        print("Space Pressed")
        screen.fill('White')
    else:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
        else:
            screen.fill('#FFF7B0')
            startScreen()
            screen.blit(sesame_surface, sesame_rect)
            screen.blit(name_surface,name_rect)
            screen.blit(play_surface,play_rect)
            # mouse button pressed
            # if event.type ==pygame.MOUSEBUTTONDOWN:
            #     print(event.pos)
            # key pressed
            # if event.type== pygame.KEYDOWN:
            #     print("key down pressed")
            # key release
            # if event.type==pygame.KEYUP:
            #     print("key up pressed")
            # get mouse position
            # mouse_pos=pygame.mouse.get_pos()
            # print(mouse_pos)
            # draw line wherever mouse pointer goes
            # pygame.draw.line(screen,'Red',(0,0),pygame.mouse.get_pos())
        pygame.display.update()
        clock.tick(80)