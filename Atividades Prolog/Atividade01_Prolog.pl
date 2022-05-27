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
irmao(X,Y):- progenitor(Z,X), progenitor(Z,Y), masculino(Y), X\==Y. % X é irmao de Y comparação de diferente é em vez de !=, \==
irma(X,Y) :- progenitor(Z,X), progenitor(Z,Y), feminino(Y), X\==Y.% X é irma de Y
avo(X,Y) :- progenitor(X,Z), progenitor(Z, Y), masculino(X) . % X é avo de Y
tio(X,Y)  :- mae(S, Y), irmao(S, X); pai(S, Y), irmao(S, X), !.

