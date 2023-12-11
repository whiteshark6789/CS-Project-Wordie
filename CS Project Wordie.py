import tkinter
import customtkinter
import pygame

customtkinter.set_appearance_mode('red')
from sys import exit

def create_window():#creates window
    global mw
    mw=customtkinter.CTk()#mw=main window
    mw.geometry('2000x2000')#sets the size of the window
    mw.title('wordy')
    welcome=customtkinter.CTkLabel(mw,text='WELCOME TO WORDY',fg_color='black',width=100,height=100,text_color='green',corner_radius=50,font=('Arial Black',38))
    welcome.place(x=340,y=175)
    click=customtkinter.CTkLabel(mw,text='''click 'PLAY' to start''',fg_color='black',text_color='white').place(x=510,y=370)
    play_button()
    mw.mainloop()

def play_button():#button to enter into the game
    enter=customtkinter.CTkButton(mw,text='PLAY',fg_color='black',text_color='red',font=('Arial Black',30),corner_radius=30,command=play_command).place(x=500,y=400)

def play_command():#function which creates new windnow after clicking play
    mw.destroy()#closes the main window
    actual_game()#opens the menu window


pygame.init()
def score(i):#function to display final score
    screen1=pygame.display.set_mode((800,500),pygame.RESIZABLE)
    pygame.display.set_caption('Final Score')
    clock=pygame.time.Clock()
    wordy_font=pygame.font.SysFont('Comic Sans MS',50,bold=True)
    button1_font=pygame.font.SysFont('Comic Sans MS',40,bold=True)
    caption_surface=wordy_font.render("Score",False,"GREEN")
    
        
    one_star_img = pygame.image.load('1star.jpg')# 5 attempts
    two_star_img = pygame.image.load('2star.jpg')# 4 attempts
    three_star_img = pygame.image.load('3star.jpg')#3 attempts
    four_star_img = pygame.image.load('4star.jpg')#2 attempts
    five_star_img = pygame.image.load('5star.jpg')# first attempt
    DEFAULT_IMAGE_SIZE = (125, 50)
    one_star_img = pygame.transform.scale(one_star_img, DEFAULT_IMAGE_SIZE)
    two_star_img = pygame.transform.scale(two_star_img, DEFAULT_IMAGE_SIZE)
    three_star_img = pygame.transform.scale(three_star_img, DEFAULT_IMAGE_SIZE)
    four_star_img = pygame.transform.scale(four_star_img, DEFAULT_IMAGE_SIZE)
    five_star_img = pygame.transform.scale(five_star_img, DEFAULT_IMAGE_SIZE)
    caption_star6=button1_font.render("Invalid Score" ,False,"Blue")
    
    while True:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                pygame.quit()
                exit()
        screen1.blit(caption_surface,(290,175))
        if i==1:
            screen1.blit(five_star_img,(300,255))
        elif i==2:
             screen1.blit(four_star_img,(300,255))
        elif i==3:
            screen1.blit(three_star_img,(300,255))
        elif i==4:
            screen1.blit(two_star_img,(300,255))
        elif i==5:
            screen1.blit(one_star_img,(300,255))
        else:
            screen1.blit(caption_star6,(300,355))    
        pygame.display.update()
        clock.tick(60)

def actual_game():#game window
    global loop#loop is the number of times you can guess
    loop=0
    l=customtkinter.CTk()
    l.geometry('1000x500')
    l.configure(bg='black')
    global b#b is used to alter y axis position of each guess
    b=0
    def enter_bar():#fcuntion  of the enter button
        global b
        global loop
        enter=customtkinter.CTkEntry(l)#creates entry bar to enter guess
        enter.pack(side='left')
        def op():#working/logic of the game
            word='hello'
            m=[]
            for i in range(5):
                m.append(word[i])
                i=0
            while i<5:
                p=enter.get()
                if p[i]==word[i]:
                    green=customtkinter.CTkLabel(l,text=p[i],fg_color='green',text_color='black',width=50).place(x=500+i*70,y=100+b*70)
                    m.remove(p[i])
                elif p[i] in m:
                    yellow=customtkinter.CTkLabel(l,text=p[i],fg_color='yellow',text_color='black',width=50).place(x=500+i*70,y=100+b*70)
                    m.remove(p[i])
                else:
                    white=customtkinter.CTkLabel(l,text=p[i],fg_color='gray',text_color='black',width=50).place(x=500+i*70,y=100+b*70)
                if loop==5:
                    st.destroy()
                    if p==word:
                        y=customtkinter.CTkLabel(l,text='Congrats you got it',fg_color='blue',text_color='red').place(x=900,y=300)
                        score(loop)
                    else:
                        z=customtkinter.CTkLabel(l,text='sorry you didnt get it',fg_color='blue',text_color='red').place(x=900,y=300)
                elif p==word:
                    st.destroy()
                    y=customtkinter.CTkLabel(l,text='Congrats you got it',fg_color='blue',text_color='red').place(x=900,y=300)
                    score(loop)
                else:pass
                i+=1
            enter.destroy()#destroys entry bar after guessing
            cl.destroy()
        cl=customtkinter.CTkButton(l,text='check',fg_color='white',text_color='black',command=op)
        cl.pack()
        b+=1
        loop+=1
        
    st=customtkinter.CTkButton(l,text='start',fg_color='white',text_color='black',command=enter_bar)
    st.pack(side='bottom')
    l.mainloop()
  

def menu_window():#function to create menu window
    screen=pygame.display.set_mode((800,500),pygame.RESIZABLE)
    pygame.display.set_caption('Menu')
    clock=pygame.time.Clock()
    wordy_font=pygame.font.SysFont('Comic Sans MS',50,bold=True)
    button1_font=pygame.font.SysFont('Comic Sans MS',40,bold=True)
    caption_surface=wordy_font.render("WORDY",False,"Red")
    button1_surface=button1_font.render('play', True, 'Blue')
    button1_rectangle = pygame.Rect(225,255,150,50)
    button2_surface=button1_font.render('quit', True, 'Blue')
    button2_rectangle = pygame.Rect(400,255,150,50)

    while True:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                pygame.quit()
                exit()
            if events.type==pygame.MOUSEBUTTONDOWN:
                if button1_rectangle.collidepoint(events.pos):
                    pygame.quit()
                    pygame.init()
                    actual_game()

                    
                    
                if button2_rectangle.collidepoint(events.pos):
                    pygame.quit()
                    exit()
    
        
        screen.blit(caption_surface,(290,175))
        pygame.draw.rect(screen,'Yellow',button1_rectangle)
        screen.blit(button1_surface,(230,250))
        pygame.draw.rect(screen,'Yellow',button2_rectangle)
        screen.blit(button2_surface,(405,250))
        pygame.display.update()
        clock.tick(60)

create_window()
