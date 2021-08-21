import pygame
import random

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
score = 0
pygame.font.init()

background=pygame.image.load("background.png")
chicken=pygame.image.load("chicken.png")
user=pygame.image.load("user.png")
clock = pygame.time.Clock()

def display_score(score):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    score_text = 'Score: ' + str(score)
    text_img = font.render(score_text, True, (0,255,0))
    screen.blit(text_img, [150, 150])


def random_offset():
    return -1*random.randint(100, 2000)


def update_chicken_pos(idx):
   global score
   if(chicken_y[idx] > 600):
     chicken_y[idx] = random_offset()
     score = score+ 10
   else:
     chicken_y[idx] = chicken_y[idx] + 5

def crashed(idx):
  global score
  score = score - 5
  print("Crashed with **--", idx,"Score  =",score)
  chicken_y[idx] = random_offset()


chicken_y= [random_offset(),random_offset(),random_offset()]
user_x=150

keep_alive = True
while keep_alive:

   pygame.event.get()
   keys = pygame.key.get_pressed()
   if keys[pygame.K_RIGHT] and user_x <280:
            user_x = user_x + 10
   elif keys[pygame.K_LEFT] and user_x > 0:
            user_x = user_x - 10


   update_chicken_pos(0)
   update_chicken_pos(1)
   update_chicken_pos(2)
   screen.blit(background, [0, 0])
   screen.blit(chicken, [5, chicken_y[0]])
   screen.blit(chicken, [150, chicken_y[1]])
   screen.blit(chicken, [280, chicken_y[2]])
   screen.blit(user, [user_x, 520])

   if chicken_y[0] > 500 and user_x < 70:
       crashed(0)
   if chicken_y[1] > 500 and user_x > 100 and user_x < 200:
       crashed(1)

   if chicken_y[2] > 500 and user_x > 220:
       crashed(2)
   display_score(score)

   


   pygame.display.update()
   clock.tick(150)

