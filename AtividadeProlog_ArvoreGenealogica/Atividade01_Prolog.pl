masculino(joao).
masculino(joaquim).
masculino(marcelino).
masculino(aristides).
feminino(joana).
feminino(serafina).
feminino(maria).
feminino(ana).
progenitor(joao, joaquim).
progenitor(joao, serafina).
progenitor(joana, joaquim).
progenitor(joana, serafina).
progenitor(joaquim, marcelino).
progenitor(serafina, maria).
progenitor(serafina, ana).
progenitor(marcelino, aristides).
progenitor(maria, aristides).

mae(X, Y) :- progenitor(X, Y), feminino(X). % X é projenitor de Y
pai(X,Y)  :- progenitor(X,Y), masculino(X).% X é progenitor de Y

irmao(X,Y):- progenitor(Z,X), progenitor(Z,Y), masculino(X), X\==Y, !. % X é irmao de Y comparação de diferente é em vez de !=, \==
irma(X,Y) :- progenitor(Z,X), progenitor(Z,Y), feminino(X), X\==Y, !.% X é irma de Y

avo(X,Y) :- progenitor(X,Z), progenitor(Z, Y), masculino(X) . % X é avo de Y

tio(X,Y)  :- mae(S, Y), irmao(X, S); pai(S, Y), irmao(X, S), !. % funciona para achar tio(X), 
tia(X,Y)  :- mae(S, Y), irma(X, S); pai(S, Y), irma(X, S), !. % funciona para achar tia(X),
tios(X,Y) :- tio(X,Y); tia(X,Y). % funciona para achar tio ou tia(X) de alguem (Y)

primos(X,Y) :- tios(S,Y), progenitor(S,X). % funciona para achar os primos ou primas(X) de alguem(Y)

descendentes(X,Y) :- progenitor(Y,X).% tal que X é descendente de Y
descendentes(X,Y) :- progenitor(Y,W), descendentes(X,W).


