#import all the needed modules
import pygame as game
from sys import exit
from random import randrange
import sys
#declaration of variables
highest_score = 0 # tracks the highest score
Screen_Height = 512
Screen_Width = 288
hours = 0   #Back_grounds[] -> indicator ( hours )
minutes = 0 #Back_grounds[] -> indicator ( hours -> indicator( minutes ) )
minutesPerSecond = 1 # indicator -> (min(acc))
base_X = 336#Bases[] -> indicator ( base_X )
bird_XPos = 100 #bird's X positioning
bird_YPos = 120 #bird's Y positioning
Game_Speed = 3  #Controlls speed of every motion
FPS = 60    #FPS locker
Bird_Indicator = 1 # indication for list which contains 3 types of bird
gravity = 0.2#applying gravity to bird
velocity = 0#velocity of bird
winging = 0#vecotr of bird's winging power
wing_T = False #state of bird's wing
count = 0
Pipe_X = 315
Pipe_Y = 400
Passed = False
Passed_Recorded = False
F = False
degree = 0 # bird posotion in terms of degree
Started = False
const_velocity = 1 #used for animation in the begining of program
count = 0 # track of previous animation
DownGrade = False # direction of bird's y-axis in the begining of program
Restart_Clicked = False
#definitions of several small functions
def Store_Score():
    global highest_score
    f = open("./highscore.txt", "r")
    highest_score = int(f.read())
    f.close()
    if highest_score < int(str_score):
        f = open("./highscore.txt", "w")
        f.write(str_score)
        f.close()
def Read_highScore():
    global highest_score
    f = open("./highscore.txt", "r")
    highest_score = int(f.read())
    f.close()
def hit_Music():
    game.mixer.Channel(1).play(game.mixer.Sound('./assets\\audio\\hit.wav'))
def die_Music():
    game.mixer.Channel(2).play(game.mixer.Sound('./assets\\audio\\die.wav'))
def Point_Music():
    game.mixer.Channel(3).play(game.mixer.Sound('./assets\\audio\\point.wav'))
def Wing_Music():
    game.mixer.Channel(3).play(game.mixer.Sound('./assets\\audio\\wing.wav'))
def Swoosh_Music():
    game.mixer.Channel(3).play(game.mixer.Sound('./assets\\audio\\swoosh.wav'))
def quit():
    game.quit()
    exit()
def game_exit():
    global wing_T
    global Bird_Indicator
    global count
    global F
    for i in game.event.get():
        if i.type == game.QUIT:
            quit()
        if i.type == game.KEYDOWN:
            if i.key == game.K_SPACE:
                wing_T = True
                F = True
                count = 7
                Wing_Music()
                Bird_Indicator = 0
def game_exit_End_Game():
    global wing_T
    global Bird_Indicator
    global count
    global F
    global mouse
    global Restart_Clicked
    mouse = game.mouse.get_pos()
    for i in game.event.get():
        if i.type == game.QUIT:
            quit()
        if i.type == game.MOUSEBUTTONDOWN:
            if mouse[0] >= 45 and mouse[0] <= 125 and mouse[1] >= 294 and mouse[1] <= 319:
                Store_Score()
                exec(open("./Flappy_Bird.py").read())
                quit()
            elif mouse[0] >= 165 and mouse[0] <= 245 and mouse[1] >= 294 and mouse[1] <= 319:
                Store_Score()
                quit()
def add_score():
    global str_score
    Point_Music()
    str_score = str(int(str_score) + 1)
def Draw_components():
    global Up_Pipe_Rect
    global Bt_Pipe_Rect
    global score
    global Birds
    Up_Pipe_Rect = Pipes_2.get_rect(midbottom = (Pipe_X,Pipe_Y-360))
    Bt_Pipe_Rect = Pipes.get_rect(midbottom = (Pipe_X,Pipe_Y+50))
    score = font.render(str_score,False,'White')
    Screen.blit(Back_grounds[int(hours / 12)],(0,0))
    Screen.blit(Pipes_2,Up_Pipe_Rect)
    Screen.blit(Pipes,Bt_Pipe_Rect)
    Screen.blit(Bases[0],(base_X,400))
    Screen.blit(Bases[1],(base_X-336,400))
    Screen.blit(score,(int((288-(len(str_score)*20))/2),50))
    Screen.blit(Birds[Bird_Indicator],Bird_Rect)
def Draw_components_num2():
    global Up_Pipe_Rect
    global Bt_Pipe_Rect
    global score
    global font
    global highest_score
    Up_Pipe_Rect = Pipes_2.get_rect(midbottom = (Pipe_X,Pipe_Y-360))
    Bt_Pipe_Rect = Pipes.get_rect(midbottom = (Pipe_X,Pipe_Y+50))
    score = font.render(str_score,False,'White')
    Screen.blit(Back_grounds[int(hours / 12)],(0,0))
    Screen.blit(Pipes_2,Up_Pipe_Rect)
    Screen.blit(Pipes,Bt_Pipe_Rect)
    Screen.blit(Bases[0],(base_X,400))
    Screen.blit(Bases[1],(base_X-336,400))
    Screen.blit(Birds[Bird_Indicator],Bird_Rect)
    Screen.blit(Score_Board,(19,150))
    font = game.font.Font('./assets\\font\\Flappy_bird_score_font.TTF',30)
    score = font.render(str_score,False,'White')
    Screen.blit(score,(int(148+(144-(len(str_score)*15))/2),193))
    if int(str_score) > highest_score:
        highest_score = int(str_score)
    high_score = font.render(str(highest_score),False,'White')
    Screen.blit(high_score,(int((144-(len(str_score)*15))/2)+5,193))
    Screen.blit(End_Game_Message,(47,70))
    Screen.blit(Container, (45,294))
    Screen.blit(Container, (165,294))
    Screen.blit(Restart, (55,300))
    Screen.blit(OK, (195,300))
# calucaltion section of bird's Y position and Y-axis velocity
def Draw_components_Begining():
    global Up_Pipe_Rect
    global Bt_Pipe_Rect
    global score
    Up_Pipe_Rect = Pipes_2.get_rect(midbottom = (Pipe_X,Pipe_Y-360))
    Bt_Pipe_Rect = Pipes.get_rect(midbottom = (Pipe_X,Pipe_Y+50))
    score = font.render(str_score,False,'White')
    Screen.blit(Back_grounds[int(hours / 12)],(0,0))
    Screen.blit(Pipes_2,Up_Pipe_Rect)
    Screen.blit(Pipes,Bt_Pipe_Rect)
    Screen.blit(Bases[0],(base_X,400))
    Screen.blit(Bases[1],(base_X-336,400))
    Screen.blit(score,(int((288-(len(str_score)*20))/2),50))
    Screen.blit(Birds[Bird_Indicator],Bird_Rect)
    Screen.blit(Start_Menu,(19,350-(bird_YPos + 50)))
    Screen.blit(Message,(19,350-int(bird_YPos / 2)))
def Bird_Pos():
    global bird_XPos
    global bird_YPos
    global velocity
    global winging
    global F
    global count
    global Bird_Indicator
    global Birds
    global degree
    velocity += gravity
    if F:
        F = False
        velocity = 0
    if wing_T and count > 0:
        winging += 0.3
        count -= 1
    else:
        winging = 0
    if winging == 0 and velocity > 0:
        Bird_Indicator = 2 
    velocity -= winging
    if velocity >= 5:
        velocity = 5
    elif velocity <= -5:
        velocity = -5
    bird_YPos += int(velocity)
def Bird_Pos_Begining():
    global bird_XPos
    global bird_YPos
    global count
    global DownGrade
    if count > 10:
        DownGrade = True
    elif count < -10:
        DownGrade = False
    if DownGrade:
        bird_YPos += const_velocity
        count -= 1
    else:
        bird_YPos -= const_velocity
        count += 1
#definitions of several major functions
#Start Programm
def Launch_Game():
    global minutes
    global hours
    global base_X
    global Bird_Rect
    global Pipe_X
    global Pipe_Y
    global velocity
    while True:
        game_exit()
        #day or night 
        minutes += minutesPerSecond
        if minutes >= 60:
            minutes = 0
            hours += 1
        if hours == 24:
            hours = 0
        #speed
        base_X -= Game_Speed
        Pipe_X -= Game_Speed
        #base_repositioning
        if Pipe_X <= -5:
            Pipe_X = 312
            random_int = randrange(400,600)
            Pipe_Y = random_int
        if base_X <= 0:
            base_X = 336
        Bird_Pos()
        Bird_Rect = Birds[Bird_Indicator].get_rect( topleft = (bird_XPos,bird_YPos))
        if Base_Rect.colliderect(Bird_Rect):
            hit_Music()
            End_Game()
            break
        if bird_YPos + 264 >= Pipe_Y and (bird_XPos + 60 >= Pipe_X and bird_XPos <= Pipe_X + 26) :
            hit_Music()
            End_Game()
            break
        if bird_YPos < Pipe_Y - 410 and (bird_XPos + 60 >= Pipe_X and bird_XPos <= Pipe_X + 26) :
            hit_Music()
            End_Game()
            break
        elif bird_XPos >= Pipe_X - 26 and bird_XPos <= Pipe_X + 26 and (bird_YPos <= Pipe_Y - 360 or bird_YPos >= Pipe_Y - 294):
            hit_Music()
            End_Game()
            break
        elif bird_XPos >= Pipe_X - 26 and bird_XPos <= Pipe_X + 26:
            Passed = True
        else:
            Passed = False
            Passed_Recorded = False
        if Passed and not Passed_Recorded:
            add_score()
            Passed_Recorded = True
        Draw_components()
        game.display.update()
        clock.tick(FPS)
def check_For_Event():
    global Started
    for i in game.event.get():
        if i.type == game.QUIT:
            quit()
        if i.type == game.KEYDOWN:           
            Started = True
            Swoosh_Music()
            break
#End Programm
def End_Game():
    global White_Surface
    global k
    while True:
        Screen.blit(White_Surface,(0,0))
        White_Surface.set_alpha(0)
        k += 1
        if k==5:
            die_Music()
        if(k==10):
            break
        game.display.flip()
        clock.tick(FPS)
    game.mixer.Channel(0).stop()
    while True:
        game_exit_End_Game()
        Draw_components_num2()
        game.display.update()
        clock.tick(FPS)
def Begining():
    global Started
    global Bird_Rect
    while True:
        Bird_Pos_Begining()
        Bird_Rect = Birds[Bird_Indicator].get_rect( topleft = (bird_XPos,bird_YPos))
        Draw_components_Begining()
        check_For_Event()
        game.display.update()
        if Started==True:
            Launch_Game()
            break
        clock.tick(FPS)
#initialazing pygame components
game.init()
#declaration of Screen
Screen = game.display.set_mode((Screen_Width,Screen_Height))
Back_grounds = list([game.image.load('./assets\\sprites\\background-day.png').convert(),game.image.load('./assets\\sprites\\background-night.png').convert()])
Birds = list([game.image.load('./assets\\sprites\\yellowbird-downflap.png').convert_alpha(),game.image.load('./assets\\sprites\\yellowbird-midflap.png').convert_alpha(),game.image.load('./assets\\sprites\\yellowbird-upflap.png').convert_alpha()])
Bases = list([game.image.load('./assets\\sprites\\base.png').convert_alpha(),game.image.load('./assets\\sprites\\base.png').convert_alpha()])
clock = game.time.Clock()
Pipes = game.image.load('./assets\\sprites\\pipe-green.png').convert_alpha()
Pipes_2 = game.transform.rotate(Pipes, 180)
Up_Pipe_Rect = Pipes_2.get_rect(midbottom = (Pipe_X,Pipe_Y-410))
Bt_Pipe_Rect = Pipes.get_rect(midbottom = (Pipe_X,Pipe_Y))
Score_Range = game.Rect(52,70,Pipe_X,Pipe_Y-290)
#declaration of Score font
str_score = '0'
font = game.font.Font('./assets\\font\\Flappy_bird_score_font.TTF',40)
score = font.render(str_score,False,'White')
#declaration of Songs/Musics
game.mixer.Channel(0).play(game.mixer.Sound('./assets\\audio\\theme.wav'))
Base_Rect = Bases[0].get_rect(topleft = (0,400))
#declaration of Rectangle for bird
Bird_Rect = Birds[Bird_Indicator].get_rect( topleft = (bird_XPos,bird_YPos))
White_Surface = game.Surface((288,512))
White_Surface.fill('White')
k = 0
End_Game_Message = game.image.load('./assets\\sprites\\gameover.png').convert_alpha()
Score_Board = game.image.load('./assets\\sprites\\Score_Board( End_Game).png').convert_alpha()
Start_Menu = game.image.load('./assets\\sprites\\start_Menu_text.png').convert_alpha()
font_2 = game.font.Font('./assets\\font\\Flappy_bird_score_font.TTF',15)
Message = font_2.render("Press space bar to start the game",False,'Black')
Restart = font_2.render("Restart",False,'Black')
random_int = randrange(400)
mouse = game.mouse.get_pos()
Container = game.image.load('./assets\\sprites\\Container.png').convert()
OK = font_2.render("OK",False,'Black')
Read_highScore()
Begining()
