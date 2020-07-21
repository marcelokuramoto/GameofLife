#author: Marcelo Kuramoto
#date: 21/07/2020

#Based on https://humberto.io/pt-br/blog/desbravando-o-pygame-4-game-of-life/
-----------------------------
import pygame
import random
import time

#declarando cores
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

#Classe Célula
class Celula():
    def __init__(self):
        self.status = random.randint(0,1)
        self.x = 0
        self.y = 0
    

#Inicialização
Seed = []
pygame.init()
screen = pygame.display.set_mode([640,640])
pygame.display.set_caption('Game of Life')

#Deslocamento x e y
x_desl = 10
y_desl = 10
iteracoes = 5 #input('Digite a quantidade de iterações:  ')


Seed = [[Celula() for x in range(50)] for y in range(50)]
#Analise das vizinhança
for itt in range(iteracoes):
    screen.fill(BLUE)
    for i in range (1,49):
        for j in range (1,49):
            SurroundingSum = 0
            for k in range(-1,2):
                for a in range(-1,2):
                    SurroundingSum = SurroundingSum + Seed[i+k][j+a].status
            
            SurroundingSum = SurroundingSum - Seed[i][j].status
            
            #Verificando se a celula está viva
            if Seed[i][j].status == 1:
                if SurroundingSum == 1 or SurroundingSum >3: #Apenas uma celula viva na vizinhança ou Mais de 3 celulas vivas na vizinhaca
                    Seed[i][j].status = 0
            else:
                if SurroundingSum == 3:
                    Seed[i][j].status = 1
            

            
            Seed[i][j].x =x_desl * i 
            Seed[i][j].y =y_desl * j 

            #escrevendo a celula
            
            if Seed[i][j].status == 1:
                pygame.draw.rect(screen,BLACK,[Seed[i][j].x,Seed[i][j].y,10,10])
            elif Seed[i][j].status == 0:
                pygame.draw.rect(screen,WHITE,[Seed[i][j].x,Seed[i][j].y,10,10])
            else:
                print('Erro - Status.seed diferente de 1 ou 0')

    pygame.display.flip()
    time.sleep(3)



               

        


