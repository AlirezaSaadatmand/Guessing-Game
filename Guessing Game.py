import pygame
from sys import exit
import string
import random

ISACTIVE = True

numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]
numbers_copy = numbers.copy()
c = random.randint(5 , 5)
s = ''
for i in range(c):
    choesen = random.choice(numbers)
    s += choesen
    numbers.remove(choesen)


words = ["apple" , "beach" ,"cat" , "dog" , "bread" , "brain" , "chair" , "chest" , "earth" , "music" , "money" ,
         "house" , "light" , "world" , "write" , "bank" , "card" , "case" , "back" , "fire" , "fish" , "form" ,
         "game" , "gold" , "home" , "idea" , "land" , "like" , "love" , "park" , "play" , "past" , "rise" , "type",
         "afraid" , "advise" , "amount" , "bright" , "breath" , "broken" , "change" , "danger" , "empire" , "family"] 

# counter of guess
counter = 1

# main Width and Height of the game
WIDTH = 1200
HEIGHT = 700

# Height from top
HEIGHT_FROM_TOP = 150


# The word we are looking for 
word = s
print(s)
correct_lst = list(word)
word_lst = []
word_lst.append([False for _ in range(len(word))])

# The width of each block
unit = int((WIDTH-100) / (len(word_lst[counter-1])+1))

# list of all blocks 
grid_lst = []

def create():
    lst = []
    for number in range(1 , len(word_lst[counter-1])+1):
        text_surface = pygame.Surface((100 , 100))
        text_rect = text_surface.get_rect(center = (number * unit + 100 , HEIGHT_FROM_TOP * counter-50))
        text_surface.fill("white")
        lst.append([text_rect , "black"])
    grid_lst.append(lst)
create() 

def makeList(character):
    if character == "backspace":
        if False in word_lst[counter-1]:
            x = word_lst[counter-1].index(False)
            word_lst[counter-1][(x-1)] = False
        else:
            word_lst[counter-1][-1] = False
    else:         
        if False in word_lst[counter-1]:
            for place , char in enumerate(word_lst[counter-1]):
                if char == False:
                    word_lst[counter-1][place] = character
                    break

def show():
    for block_lst in grid_lst:
        for block in block_lst:
            pygame.draw.rect(fake_screen, block[1], block[0],  3, 10)
    for j , i in enumerate(word_lst):
        for place , char in enumerate(i):
            counter_text = counter_serf.render(f"{(j+1)}-" , True , "white")
            fake_screen.blit(counter_text , (70 , (HEIGHT_FROM_TOP * (j+1)-50)-10))
            if char != False:
                text_serf = pygame.font.Font(None , 70)
                text_text = text_serf.render(char , True , "white")
                text_rect = text_text.get_rect(center = ((place + 1) * unit + 100 , HEIGHT_FROM_TOP * (j+1)-50))
                fake_screen.blit(text_text , text_rect)


def compare():
    for place , i in enumerate(word_lst[counter-2]):
        if i not in correct_lst:
            grid_lst[counter-2][place][1] = "red"
        else:
            place_correct = correct_lst.index(i)
            if place == place_correct:
                grid_lst[counter-2][place][1] = "green"
            else:
                grid_lst[counter-2][place][1] = "yellow"

pygame.init()
screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("game")
clock = pygame.time.Clock()
fake_screen = pygame.Surface( (WIDTH , 20000) )
fake_screen_rect = fake_screen.get_rect()

counter_serf = pygame.font.Font(None , 50)
game_over_serface = pygame.font.Font(None , 50)


while True:
    fake_screen.fill((70 , 70 , 70))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            # if event.unicode in numbers_copy: 
            if event.key == pygame.K_BACKSPACE:
                makeList("backspace")
            else:
                makeList(event.unicode)
                
            if event.key == pygame.K_SPACE:
                if False not in word_lst[counter-1]:
                    if correct_lst == word_lst[counter-1]:
                        ISACTIVE = False
                    counter += 1
                    word_lst.append([False for _ in range(len(word))])
                    compare()
                    create()
        if counter >= 4:
            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    fake_screen_rect.y += 40
                elif event.y == -1:
                    fake_screen_rect.y -= 40
    if ISACTIVE:
        show()
        screen.blit(fake_screen , fake_screen_rect)
    else:
        screen.fill((70 ,70 , 70))
        game_over_text = game_over_serface.render(f"You Win! {counter -1}" , True , "White")
        screen.blit(game_over_text , (575 , 275))
    pygame.display.update()
    clock.tick(60)