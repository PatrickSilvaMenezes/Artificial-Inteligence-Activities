def greedy_best_first_search(initial_node, frontiers, explored):
    print('331')    #primeiro nó percorrido
    goal = '000'    #objetivo
    h = [('331',11), ('130',10), ('230',12), ('220',12),('231',9),
         ('030',8), ('131',7), ('120',6), ('221',5), ('200',4), ('301',3),
         ('100',2),('201',1),('111',1),('000',0)]  #heuristica
    actual_node = initial_node  #atual valor de nó
    actual_h = 11               #atual valor de heurística
    lowest_value = ''           #menor valor da fronteira
    lowest_node = ''            #nó de menor valor da fronteira
 
    while(1):
        #define fronteira do nó atual
        if(actual_node == '331'):frontier = frontiers[0]
        elif(actual_node == '130'):frontier = frontiers[1]
        elif(actual_node == '230'):frontier = frontiers[2]
        elif(actual_node == '220'):frontier = frontiers[3]
        elif(actual_node == '231'):frontier = frontiers[4]
        elif(actual_node == '030'):frontier = frontiers[5]
        elif(actual_node == '131'):frontier = frontiers[6]
        elif(actual_node == '120'):frontier = frontiers[7]
        elif(actual_node == '221'):frontier = frontiers[8]
        elif(actual_node == '200'):frontier = frontiers[9]
        elif(actual_node == '301'):frontier = frontiers[10]
        elif(actual_node == '100'):frontier = frontiers[11]
        elif(actual_node == '201'):frontier = frontiers[12]
        elif(actual_node == '111'):frontier = frontiers[13]
        ##################################################

        #define o custo heurístico do nó atual
        cont = 0    #var auxiliar para percorrer for
        for y in h: #y retorna algo do tipo ('estado',valor)
            if(actual_node == h[cont][0]):
                actual_h=h[cont][1]
            cont = cont+1
        ##################################################  

        #se fronteira vazia, erro
        if(len(frontier) == 0):     
            return print("empty frontier")  
        ##################################################
        
        #verifica qual da fronteira tem menor custo em h(x)
        #transforma menor valor em nó atual
        lowest_value = actual_h
        lowest_node = actual_node
        for x in frontier: 
            cont = 0
            for y in h:
                if(x==h[cont][0]): 
                    if(h[cont][1]<lowest_value):
                        lowest_value = h[cont][1]
                        lowest_node = h[cont][0]
                cont = cont+1
        actual_node = lowest_node
        print(actual_node)  #mostra qual o nó atual
        ##################################################

        #verifica se terminamos
        if(actual_node == goal):
            return print("OK")
        ##################################################

        #adiciona nó atual aos explorados
        explored.append(actual_node)
        ##################################################

        #para todas ações possíveis daquele estado, faz trocas úteis
        for a in range(0,len(frontier)):
            if(frontier[a] not in explored or frontier[a] not in frontier):
                frontier.append(frontier[a])
            elif(frontier[a] in frontier):
                for j in range(0, len(frontier)):
                    if(frontier[a] > frontier[j]):
                        frontier[j] = frontier[a]

initial_node = '331'
explored = []

#tree
frontier331 = [('130'), ('230'), ('220')]
frontier130 = [('331'), ('231') ]
frontier230 = [('331')]
frontier220 = [('231'),('331')]
frontier231 = [('130'),('030'),('220')]
frontier030 = [('231'),('131')]
frontier131 = [('030'),('120')]
frontier120 = [('131'),('221'),('231')]
frontier221 = [('200')]
frontier200 = [('221'),('301')]
frontier301 = [('200'),('100')]
frontier100 = [('301'),('201'),('111')]
frontier201 = [('100'),('000')]
frontier111 = [('000'),('100')]
frontiers = [frontier331,frontier130,frontier230,frontier220,frontier231,
             frontier030,frontier131,frontier120,frontier221,frontier200,
             frontier301,frontier100,frontier201,frontier111] 

greedy_best_first_search(initial_node, frontiers, explored)     