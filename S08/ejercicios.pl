% Definición de arista en el grafo
aris(a, b).
aris(b, c).
aris(c, d).
aris(a, d).
aris(d, e).

camino(X, Y) :- aris(X, Y).
camino(X, Y) :- aris(X, Z), camino(Z, Y).

%?- camino(a, e).
