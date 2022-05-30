from random import randint      #biblioteca para gerar números aleatórios
import math

def reflex_vacuum_agent(pos):
    location = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0]]
    pontuation = 0
    #INICIALMENTE TEMOS:
    #0|0|0
    #0|0|0
    #0|0|0
    #1 PARA SUJO 0 PARA LIMPO
    
    #DEFINIMOS STATUS DO AMBIENTE (20% DE CHANCE DE ESTAR SUJO)
    random = 0
    for i in range(0,9):
        random = randint(0,9)
        if(random == 1 or random == 0):
            location[i][1] = 1
        else:
            location[i][1] = 0
        print(location[i][1])
    print("--------------------------")
    #gerar caminhos aleatórios
    pos_atual = 0
    for i in range(0,100):                       #vezes
        #print("Onde: "+ str(location[pos][0]))
        #print("Status"+str(location[pos][1]))
        pos_atual = pos
        if(location[pos][1] == 1):  #se posição estiver suja
            location[pos][1] = 0
            pontuation = pontuation + 1
        else:                       #pega posição próxima
            if(location[pos][0] == 0):
                pos = randint(0,8)
                if(pos == pos_atual or (pos != 1 and pos != 3)):
                    while(pos == pos_atual or (pos != 1 and pos != 3)):
                        pos = randint(0,8)
            elif(location[pos][0] == 1):
                pos = randint(0,8)
                if(pos == pos_atual or (pos != 0 and pos != 2 and pos != 4)):
                    while(pos == pos_atual or (pos != 1 and pos != 2 and pos != 4)):
                        pos = randint(0,8)
            elif(location[pos][0] == 2):
                pos = randint(0,8)
                if(pos == pos_atual or (pos != 1 and pos != 5)):
                    while(pos == pos_atual or (pos != 1 and pos != 5)):
                        pos = randint(0,8)
            elif(location[pos][0] == 3):
                pos = randint(0,8)
                if(pos == pos_atual or (pos != 0 and pos != 4 and pos != 6)):
                    while(pos == pos_atual or (pos != 0 and pos != 4 and pos != 6)):
                        pos = randint(0,8)
            elif(location[pos][0] == 4):
                pos = randint(0,8)
                if(pos == pos_atual or (pos != 1 and pos != 3 and pos != 7 and pos != 5)):
                    while(pos == pos_atual or (pos != 1 and pos != 3 and pos != 7 and pos != 5)):
                        pos = randint(0,8)
            elif(location[pos][0] == 5):
                pos = randint(0,8)
                if(pos == pos_atual or (pos != 2 and pos != 4 and pos != 8)):
                    while(pos == pos_atual or (pos != 2 and pos != 4 and pos != 8)):
                        pos = randint(0,8)
            elif(location[pos][0] == 6):
                pos = randint(0,8)
                if(pos == pos_atual or (pos != 3 and pos != 7)):
                    while(pos == pos_atual or (pos != 3 and pos != 7)):
                        pos = randint(0,8)
            elif(location[pos][0] == 7):
                pos = randint(0,8)
                if(pos == pos_atual or (pos != 4 and pos != 6 and pos != 8)):
                    while(pos == pos_atual or (pos != 4 and pos != 6 and pos != 8)):
                        pos = randint(0,8)
            elif(location[pos][0] == 8):
                pos = randint(0,8)
                if(pos == pos_atual or (pos != 7 and pos != 5)):
                    while(pos == pos_atual or (pos != 7 and pos != 7)):
                        pos = randint(0,8)    
        
        
    print("--------------------------")

    for i in range(0,9):
        print(location[i][1])
    print("Desempenho: " + str(pontuation))        
    
pos = int(input("Digite a posição inicial [0 a 8] "))
if(pos < 0 or pos > 8):
    print("Valor inválido")
else:
    reflex_vacuum_agent(pos)

##verificar parte do maior que 1 a distancia


