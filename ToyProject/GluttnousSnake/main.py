import pygame
import sys
import random

SCREEN_X = 600
SCREEN_Y = 600

class Snake(object):
    def __init__(self):
        self.direction = pygame.K_RIGHT
        self.body = []
        for x in range(5):
            self.add_node()

    def add_node(self):
        #Must use curly brackets?
        left,top = (0,0)
        if self.body:
            left,top = (self.body[0].left,self.body[0].top)
        node = pygame.Rect(left,top,25,25)
        if self.direction == pygame.K_LEFT:
            node.left-=25
        elif self.direction == pygame.K_RIGHT:
            node.left+=25
        elif self.direction == pygame.K_UP:
            node.top-=25
        elif self.direction == pygame.K_DOWN:
            node.top+=25
        self.body.insert(0,node)

    def del_node(self):
        self.body.pop()

    def is_dead(self):
        if self.body[0].x not in range(SCREEN_X):
            return True
        if self.body[0].y not in range(SCREEN_Y):
            return True
        if self.body[0] in self.body[1:]:
            return True

    def move(self):
        self.add_node()
        self.del_node()

    def change_direction(self,curKey):
        LR = [pygame.K_LEFT,pygame.K_RIGHT]
        UD = [pygame.K_UP,pygame.K_DOWN]
        if curKey in LR+UD:
            if (curKey in LR) and (self.direction in LR):
                return
            if (curKey in UD) and (self.direction in UD):
                return
            self.direction = curKey


class Food:
    def __init__(self):
        self.rect = pygame.Rect(-25,0,25,25)

    def remove(self):
        self.rect.x-=25

    def set(self):
        if self.rect.x == -25:
            allpos=[]
            for pos in range(25,SCREEN_X-25,25):
                allpos.append(pos)
            
            self.rect.left = random.choice(allpos)
            self.rect.top = random.choice(allpos)
            print(self.rect)


def show_text(screen,pos,text,color,font_bold=False,font_size=60,font_italic=False):
    cur_font = pygame.font.SysFont('宋体',font_size)
    cur_font.set_bold(font_bold)
    cur_font.set_italic(font_italic)
    text_fmt = cur_font.render(text,1,color)
    screen.blit(text_fmt,pos)

def main():
    pygame.init()
    screen_size =(SCREEN_X,SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    scores = 0
    isdead=False

    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                snake.change_direction(event.key)
                if event.key == pygame.K_SPACE and isdead:
                    return main()
        
        screen.fill((255,255,255))

        if not isdead:
            scores+=1
            snake.move()
        for rect in snake.body:
            pygame.draw.rect(screen,(20,220,39),rect,0)

        isdead = snake.is_dead()
        if isdead:
            show_text(screen,(100,200),'YOU DEAD!',(227,29,18),False,100)
            show_text(screen,(150,260),'press space to try again...',(0,0,22),False,30)
        if food.rect == snake.body[0]:
            scores+=50
            food.remove()
            snake.add_node()

        food.set()
        pygame.draw.rect(screen,(136,0,21),food.rect,0)

        show_text(screen,(50,500),'Scores: '+str(scores),(223,223,223))

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()