import pygame
pygame.init()
def menu_window():#function to create menu window

    screen=pygame.display.set_mode((800,500),pygame.RESIZABLE)
    pygame.display.set_caption('Score')
    clock=pygame.time.Clock()
    wordy_font=pygame.font.SysFont('Comic Sans MS',50,bold=True)
    button1_font=pygame.font.SysFont('Comic Sans MS',40,bold=True)
    one_star_img = pygame.image.load('1star.jpg')
    two_star_img = pygame.image.load('2star.jpg')
    three_star_img = pygame.image.load('3star.jpg')
    four_star_img = pygame.image.load('4star.jpg')
    five_star_img = pygame.image.load('5star.jpg')
    DEFAULT_IMAGE_SIZE = (125, 50)
    one_star_img = pygame.transform.scale(one_star_img, DEFAULT_IMAGE_SIZE)
    two_star_img = pygame.transform.scale(two_star_img, DEFAULT_IMAGE_SIZE)
    three_star_img = pygame.transform.scale(three_star_img, DEFAULT_IMAGE_SIZE)
    four_star_img = pygame.transform.scale(four_star_img, DEFAULT_IMAGE_SIZE)
    five_star_img = pygame.transform.scale(five_star_img, DEFAULT_IMAGE_SIZE)
   
    caption_surface=wordy_font.render("Score",False,"Red")
    caption_star1=button1_font.render("11111",False,"Blue")
    caption_star2=button1_font.render("1111",False,"Blue")
    caption_star3=button1_font.render("111",False,"Blue")
    caption_star4=button1_font.render("11",False,"Blue")
    caption_star5=button1_font.render("1",False,"Blue")
    caption_star6=button1_font.render("Try Again",False,"Blue")
    
    while True:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(caption_surface,(290,175))
        i=5
        if i==1:
            screen.blit(one_star_img,(300,255))
        elif i==2:
             screen.blit(two_star_img,(300,255))
        elif i==3:
            screen.blit(three_star_img,(300,255))
        elif i==4:
            screen.blit(four_star_img,(300,255))
        elif i==5:
            screen.blit(five_star_img,(300,255))
        else:
            screen.blit(caption_star6,(300,355))    
        pygame.display.update()
        clock.tick(60)
menu_window()