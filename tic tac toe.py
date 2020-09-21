import pygame
import sys
import time
import random

#TO DO
#Fix ending easy
#fix easy double loop
#add Impossible buttons
#implement minimax


def drawGrid():
    blocksize = screen_width/3
    for y in range(0, int(screen_height)):
        for x in range(0, int(screen_width)):
            rect = pygame.Rect(x * (blocksize + 1), y * (blocksize + 1), blocksize, blocksize)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)
            squares.append(rect)
    print(squares[960].centerx, squares[960].centery)

def Cwin(text,location,color=(255,0,0)):
    while True:
        screen.fill((200,200,200))
        screen.blit(font.render(text,True,color),location)

        x,y = pygame.mouse.get_pos()
        eButton = pygame.Rect(120, 200, 250, 50)
        pygame.draw.rect(screen, (255,0,0), eButton)
        menuText("Back to menu", (160, 212), (0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if eButton.collidepoint((x,y)):
                    screen.fill((0,0,0))
                    menu()

        pygame.display.update()


def Swin(text,location,color=(0,0,255)):
    while True:
        screen.fill((200, 200, 200))
        screen.blit(font.render(text, True, color), location)

        x, y = pygame.mouse.get_pos()
        eButton = pygame.Rect(120, 200, 250, 50)
        pygame.draw.rect(screen, (0, 0, 255), eButton)
        menuText("Back to menu", (160, 212), (200,200,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if eButton.collidepoint((x, y)):
                    screen.fill((0, 0, 0))
                    menu()

        pygame.display.update()

def Tie(text,location,color=(0, 0, 0)):
    while True:
        screen.fill((200, 200, 200))
        screen.blit(font.render(text, True, color), location)

        x, y = pygame.mouse.get_pos()
        eButton = pygame.Rect(120, 200, 250, 50)
        pygame.draw.rect(screen, (0, 0, 255), eButton)
        menuText("Back to menu",  (160, 212), (0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if eButton.collidepoint((x, y)):
                    screen.fill((0, 0, 0))
                    menu()

        pygame.display.update()

def menuText(text,location,color=(0, 0, 0)):
    screen.blit(font2.render(text,True,color),location)

def easyMode():
    moves =  []
    for i in range(9):
        moves.append(0)
    drawGrid()
    clock.tick(10)
    while True:
        shapes = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                count = 0
                for i in squares:
                    count += 1
                    if i.collidepoint(pos):
                        if count == 1 and moves[0] == 0:
                            moves[0] = 1
                            pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                            shapes+=1

                        if count == 2 and moves[1] == 0:
                            moves[1] = 1
                            pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                            shapes+=1

                        if count == 3 and moves[2] == 0:
                            moves[2] = 1
                            pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                            shapes+=1

                        if count == 481 and moves[3] == 0:
                            moves[3] = 1
                            pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                            shapes+=1

                        if count == 482 and moves[4] == 0:
                            moves[4] = 1
                            pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                            shapes+=1

                        if count == 483 and moves[5] == 0:
                            moves[5] = 1
                            pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                            shapes+=1

                        if count == 961 and moves[6] == 0:
                            moves[6] = 1
                            pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                            shapes+=1

                        if count == 962 and moves[7] == 0:
                            moves[7] = 1
                            pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                            shapes+=1

                        if count == 963 and moves[8] == 0:
                            moves[8] = 1
                            pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                            shapes+=1

                        while True:
                            options = [0,1,2,480,481,482,960,961,962]
                            pick = int(random.choice(options))
                            print(pick)
                            if pick == 0:
                                pick2 = 0
                            elif pick == 1:
                                pick2 = 1
                            elif pick == 2:
                                pick2 = 2
                            elif pick == 480:
                                pick2 = 3
                            elif pick == 481:
                                pick2 = 4
                            elif pick == 482:
                                pick2 = 5
                            elif pick == 960:
                                pick2 = 6
                            elif pick == 961:
                                pick2 = 7
                            elif pick == 962:
                                pick2 = 8
                            if moves[pick2] == 0:
                                moves[pick2] = 2
                                r = pygame.Rect(squares[pick].centerx - 40, squares[pick].centery - 40, 80, 80)
                                pygame.draw.rect(screen, (0, 0, 255), r)
                                shapes += 1
                                break

                        if (moves[0] == 1 and moves[1] == 1 and moves[2] == 1) or (moves[3] == 1 and moves[4] == 1 and moves[5] == 1) or (moves[6] == 1 and moves[7] == 1 and moves[8] == 1):
                            screen.fill((200, 200, 200))
                            Cwin('Circle Wins!', (145, 220))
                            menu()


                        if (moves[0] == 2 and moves[1] == 2 and moves[2] == 2) or (moves[3] == 2 and moves[4] == 2 and moves[5] == 2) or (moves[6] == 2 and moves[7] == 2 and moves[8] == 2):
                            screen.fill((200, 200, 200))
                            Swin('Square Wins!', (130, 220))
                            menu()

                        if (moves[0] == 1 and moves[3] == 1 and moves[6] == 1) or (moves[1] == 1 and moves[4] == 1 and moves[7] == 1) or (moves[2] == 1 and moves[5] == 1 and moves[8] == 1):
                            screen.fill((200, 200, 200))
                            Cwin('Circle Wins!', (145, 220))
                            menu()


                        if (moves[0] == 2 and moves[3] == 2 and moves[6] == 2) or (moves[1] == 2 and moves[4] == 2 and moves[7] == 2) or (moves[2] == 2 and moves[5] == 2 and moves[8] == 2):
                            screen.fill((200, 200, 200))
                            Swin('Square Wins!', (130, 220))
                            menu()

                        if (moves[0] == 1 and moves[4] == 1 and moves[8] == 1) or (moves[2] == 1 and moves[4] == 1 and moves[6] == 1):
                            screen.fill((200, 200, 200))
                            Cwin('Circle Wins!', (145, 220))
                            menu()

                        if (moves[0] == 2 and moves[4] == 2 and moves[8] == 2) or (moves[2] == 2 and moves[4] == 2 and moves[6] == 2):
                            screen.fill((200, 200, 200))
                            Swin('Square Wins!', (130, 220))
                            menu()

                        elif (shapes >=8):
                            screen.fill((200, 200, 200))
                            Tie('Tie!', (200, 200))
        pygame.display.flip()

def Human():

    moves = []
    for i in range(9):
        moves.append(0)
    drawGrid()
    turn = 0
    clock.tick(10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                count = 0
                for i in squares:
                    count += 1
                    if i.collidepoint(pos):
                        if (turn % 2 == 0):
                            if count == 1 and moves[0] == 0:
                                moves[0] = 1
                                pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (0, 255, 0)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (255, 255, 255)), (380, 10))

                            if count == 2 and moves[1] == 0:
                                moves[1] = 1
                                pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (0, 255, 0)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (255, 255, 255)), (380, 10))



                            if count == 3 and moves[2] == 0:
                                moves[2] = 1
                                pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (0, 255, 0)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (255, 255, 255)), (380, 10))



                            if count == 481 and moves[3] == 0:
                                moves[3] = 1
                                pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (0, 255, 0)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (255, 255, 255)), (380, 10))


                            if count == 482 and moves[4] == 0:
                                moves[4] = 1
                                pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (0, 255, 0)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (255, 255, 255)), (380, 10))


                            if count == 483 and moves[5] == 0:
                                moves[5] = 1
                                pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (0, 255, 0)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (255, 255, 255)), (380, 10))


                            if count == 961 and moves[6] == 0:
                                moves[6] = 1
                                pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (0, 255, 0)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (255, 255, 255)), (380, 10))


                            if count == 962 and moves[7] == 0:
                                moves[7] = 1
                                pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (0, 255, 0)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (255, 255, 255)), (380, 10))


                            if count == 963 and moves[8] == 0:
                                moves[8] = 1
                                pygame.draw.circle(screen, (255, 0, 0), (i.centerx, i.centery), 50)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (0, 255, 0)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (255, 255, 255)), (380, 10))

                        else:
                            if count == 1 and moves[0] == 0:
                                moves[0] = 2
                                r = pygame.Rect(i.centerx - 40, i.centery - 40, 80, 80)
                                pygame.draw.rect(screen, (0, 0, 255), r)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (255, 255, 255)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (0, 255, 0)), (380, 10))


                            if count == 2 and moves[1] == 0:
                                moves[1] = 2
                                r = pygame.Rect(i.centerx - 40, i.centery - 40, 80, 80)
                                pygame.draw.rect(screen, (0, 0, 255), r)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (255, 255, 255)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (0, 255, 0)), (380, 10))



                            if count == 3 and moves[2] == 0:
                                moves[2] = 2
                                r = pygame.Rect(i.centerx - 40, i.centery - 40, 80, 80)
                                pygame.draw.rect(screen, (0, 0, 255), r)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (255, 255, 255)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (0, 255, 0)), (380, 10))


                            if count == 481 and moves[3] == 0:
                                moves[3] = 2
                                r = pygame.Rect(i.centerx - 40, i.centery - 40, 80, 80)
                                pygame.draw.rect(screen, (0, 0, 255), r)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (255, 255, 255)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (0, 255, 0)), (380, 10))


                            if count == 482 and moves[4] == 0:
                                moves[4] = 2
                                r = pygame.Rect(i.centerx - 40, i.centery - 40, 80, 80)
                                pygame.draw.rect(screen, (0, 0, 255), r)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (255, 255, 255)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (0, 255, 0)), (380, 10))


                            if count == 483 and moves[5] == 0:
                                moves[5] = 2
                                r = pygame.Rect(i.centerx - 40, i.centery - 40, 80, 80)
                                pygame.draw.rect(screen, (0, 0, 255), r)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (255, 255, 255)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (0, 255, 0)), (380, 10))


                            if count == 961 and moves[6] == 0:
                                moves[6] = 2
                                r = pygame.Rect(i.centerx - 40, i.centery - 40, 80, 80)
                                pygame.draw.rect(screen, (0, 0, 255), r)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (255, 255, 255)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (0, 255, 0)), (380, 10))


                            if count == 962 and moves[7] == 0:
                                moves[7] = 2
                                r = pygame.Rect(i.centerx - 40, i.centery - 40, 80, 80)
                                pygame.draw.rect(screen, (0, 0, 255), r)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (255, 255, 255)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (0, 255, 0)), (380, 10))


                            if count == 963 and moves[8] == 0:
                                moves[8] = 2
                                r = pygame.Rect(i.centerx - 40, i.centery - 40, 80, 80)
                                pygame.draw.rect(screen, (0, 0, 255), r)
                                turn += 1
                                screen.blit(font3.render("Player 1!", True, (255, 255, 255)), (10, 10))
                                screen.blit(font3.render("Player 2!", True, (0, 255, 0)), (380, 10))


                if (moves[0] == 1 and moves[1] == 1 and moves[2] == 1) or (moves[3] == 1 and moves[4] == 1 and moves[5] == 1) or (moves[6] == 1 and moves[7] == 1 and moves[8] == 1):
                    screen.fill((200, 200, 200))
                    Cwin("Circle Wins!", (145, 100))


                if (moves[0] == 2 and moves[1] == 2 and moves[2] == 2) or (
                    moves[3] == 2 and moves[4] == 2 and moves[5] == 2) or (
                    moves[6] == 2 and moves[7] == 2 and moves[8] == 2):
                    screen.fill((200, 200, 200))
                    Swin('Square Wins!', (130, 100))

                if (moves[0] == 1 and moves[3] == 1 and moves[6] == 1) or (
                    moves[1] == 1 and moves[4] == 1 and moves[7] == 1) or (
                    moves[2] == 1 and moves[5] == 1 and moves[8] == 1):
                    screen.fill((200, 200, 200))
                    Cwin('Circle Wins!', (145, 100))

                if (moves[0] == 2 and moves[3] == 2 and moves[6] == 2) or (
                    moves[1] == 2 and moves[4] == 2 and moves[7] == 2) or (
                    moves[2] == 2 and moves[5] == 2 and moves[8] == 2):
                    screen.fill((200, 200, 200))
                    Swin('Square Wins!', (130, 100))

                if (moves[0] == 1 and moves[4] == 1 and moves[8] == 1) or (
                    moves[2] == 1 and moves[4] == 1 and moves[6] == 1):
                    screen.fill((200, 200, 200))
                    Cwin('Circle Wins!', (145, 100))

                if (moves[0] == 2 and moves[4] == 2 and moves[8] == 2) or (
                    moves[2] == 2 and moves[4] == 2 and moves[6] == 2):
                    screen.fill((200, 200, 200))
                    Swin('Square Wins!', (130, 100))

                if (turn == 9):
                    screen.fill((200, 200, 200))
                    Tie('Tie!', (200, 100))

        pygame.display.flip()


def menu():
    while True:
        screen.fill((0,0,0))
        menuText('Welcome to Tic Tac Toe!', (100, 75), (255,255,255))

        x,y = pygame.mouse.get_pos()
        humanButton = pygame.Rect(120, 150, 250, 50)
        pygame.draw.rect(screen, (0,0,255), humanButton)
        menuText("Human v Human", (145, 162))

        easyButton = pygame.Rect(120, 250, 250, 50)
        pygame.draw.rect(screen, (0, 0, 255), easyButton)
        menuText("Easy Mode", (180, 265))

        #x, y = pygame.mouse.get_pos()
        #humanButton = pygame.Rect(120, 200, 250, 50)
        #pygame.draw.rect(screen, (0, 0, 255), humanButton)
        #menuText("Human v Human", (145, 212))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.K_SPACE:
                menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if humanButton.collidepoint((x,y)):
                    screen.fill((0,0,0))
                    Human()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easyButton.collidepoint((x,y)):
                    screen.fill((0,0,0))
                    easyMode()

        pygame.display.update()



pygame.init()
pygame.font.init()
global font
font=pygame.font.SysFont("Helvetica", 50)
font2=pygame.font.SysFont("Helvetica", 35)
font3= pygame.font.SysFont("Helvetica", 28)

screen_width = 480
screen_height = 480
squares = []


pygame.init()
title = pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_height, screen_width))


def main():
    menu()


main()