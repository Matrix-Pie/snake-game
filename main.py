import sys
import random
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = WINDOW_HEIGHT
BLOCKSIZE = int(WINDOW_HEIGHT/20)


foodx = round(random.randrange(0, WINDOW_WIDTH - BLOCKSIZE, BLOCKSIZE))
foody = round(random.randrange(0, WINDOW_WIDTH - BLOCKSIZE, BLOCKSIZE))

game_over = False

High_score = 0

FPS = 7
fpsClock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 50)
score_font = pygame.font.SysFont("comicsansms",35)
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('grid')

def drawSnake(snake_list):
    global x1,y1,x1_change,y1_change
    x1 += x1_change
    y1 += y1_change
    for x in snake_list:
        pygame.draw.rect(SCREEN, WHITE, [x[0], x[1], BLOCKSIZE, BLOCKSIZE])

def score(score):
    value = score_font.render("Your score: " + str(score), True, (0,100,0))
    SCREEN.blit(value, [0, 0])

def main():
    global SCREEN, CLOCK, x1, y1, x1_change, y1_change, game_over, foodx,foody, Length_of_snake, High_score
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    x1 = 0
    y1 = 0

    x1_change = 0
    y1_change = 0
    
    snake_List = []
    Length_of_snake = 1
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -BLOCKSIZE
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = BLOCKSIZE
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -BLOCKSIZE
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = BLOCKSIZE
                    x1_change = 0
                elif event.key == pygame.K_ESCAPE:
                    if Length_of_snake - 1 > High_score: 
                        High_score = Length_of_snake - 1
                    mainScreen()
        if x1 >= WINDOW_WIDTH or x1 < 0 or y1 >= WINDOW_HEIGHT or y1 < 0:
            if Length_of_snake - 1 > High_score: 
                    High_score = Length_of_snake - 1
            mainScreen()

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                if Length_of_snake - 1 > High_score: 
                    High_score = Length_of_snake - 1
                mainScreen()
 
        drawGrid()
        drawSnake(snake_List)
        score(Length_of_snake - 1)
        foodSpawn()
        pygame.display.update()
        fpsClock.tick(FPS)
    
def message(msg,color, x, y):
    mesg = font_style.render(msg, True, color)
    SCREEN.blit(mesg, [x, y])    

def foodSpawn():
    global foodx, foody,Length_of_snake
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, WINDOW_WIDTH - BLOCKSIZE, BLOCKSIZE))
        foody = round(random.randrange(0, WINDOW_WIDTH - BLOCKSIZE, BLOCKSIZE))
        Length_of_snake += 1
    pygame.draw.rect(SCREEN, (200,0,0), [foodx, foody, BLOCKSIZE, BLOCKSIZE])
      
def drawGrid():
    SCREEN.fill(BLACK)
    for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def mainScreen():
    global SCREEN, CLOCK, x1, y1, x1_change, y1_change, game_over
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                x1 = 0
                y1 = 0
                x1_change = 0
                y1_change = 0
                main()
                
            
        message("Game over", WHITE, 150, 200)   
        message("Your High score: " + str(High_score), WHITE, 150, 300 ) 
        pygame.display.update()
        fpsClock.tick(FPS)

# Main Loop
main()