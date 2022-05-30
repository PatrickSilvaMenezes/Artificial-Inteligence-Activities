#parâmetro de desempenho: o quanto limpou com 10 pontos e o quanto andou com -1

sujeiraA = 0         #1 ou 0  
sujeiraB = 0         #1 ou 0    
pos = ''             #A ou B
cont = 0             #conta quanta sujeira limpou
cont2 = 0            #determina quantas voltas o aspirador dá


sujeiraA = int(input("Digite a sujeira na posição A "))
sujeiraB = int(input("Digite a sujeira na posição B "))
pos = str(input("Digite a posição inicial "))

if (sujeiraA != 1 and sujeiraA != 0) or (sujeiraB!= 1 and sujeiraB!=0) or (pos != "A" and pos != "B" and pos != "a" and pos != "b"):
    print("Dados inseridos inválidos, tente novamente")
    exit()

def aspira(pos, sujeiraA, sujeiraB, cont, cont2):
    log = ''  #guarda se estado anterior estava limpo para refletir na ação 
    andou = 0 #verifica se já passou por alguma posição na iteração
    while True:  
        andou = 0
        if (pos == 'A') or (pos == 'a'):
            if(sujeiraA == 1):
                print("Posição A está suja")
                sujeiraA = 0
                log = 'A'
                cont = cont+10              #cada limpo incrementa 10 na pontuação
            cont = cont-1              #cada vez que anda decrementa 1
            pos = 'B'
            andou = 1      
                             

        if ((pos == 'B') or (pos == 'b')) and andou == 0:                                                                
            if(sujeiraB == 1):
                print("Posição B está suja")
                sujeiraB = 0          
                log = 'B'     
                cont = cont+10           #cada limpo incrementa 10 na pontuação
            cont = cont-1           #cada vez que anda decrementa 1
            pos = 'A'
        
        cont2 = cont2 + 1

        if cont2 == 5 or (sujeiraA == 0 and log == 'B') or (sujeiraB == 0 and log == 'A'):              
            break
        
    print("Critério de desempenho: 10 pontos para limpeza e -1 para quando andar")
    cont = str(cont)
    print("Desempenho:"+   cont)

    
    

aspira(pos, sujeiraA, sujeiraB, cont, cont2)

