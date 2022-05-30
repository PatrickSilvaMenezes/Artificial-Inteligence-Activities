#parâmetro de desempenho: o quanto limpou

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

    while True:  

        if (pos == 'A') or (pos == 'a'):
            if(sujeiraA == 1):
                print("Posição A está suja")
                sujeiraA = 0
                cont = cont+1
            pos = 'B'
  
        if (pos == 'B') or (pos == 'b'):                                                                
            if(sujeiraB == 1):
                print("Posição B está suja")
                sujeiraB = 0
                cont = cont+1
            pos = 'A'
        
        cont2 = cont2 + 1

        if cont2 == 1000:
            break
        

    if(cont == 2):
        print("Desempenho: limpou 2")
    elif(cont == 1):
        print("Desempenho: limpou 1")
    elif(cont == 0):
        print("Desempenho: limpou 0")
    

aspira(pos, sujeiraA, sujeiraB, cont, cont2)

