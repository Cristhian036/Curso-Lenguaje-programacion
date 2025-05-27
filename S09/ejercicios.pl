%Programacion logica - listas

lista([1,2,3,4]).

%?- lista(L), L= [X | Y].

%Programacion logica
%listas - Tamaño de lista

longitud([],0).
longitud([_ | Resto], N) :- longitud(Resto, M), N is M + 1.

%?- longitud([a,b,c,d], L).

%Programacion logica - Backtracking

conectado(a,b).
conectado(b,c).
conectado(c,d).
conectado(d,salida).

camino(X,Y)	:- conectado(X, Y).
camino(X,Y)	:- conectado(X, Z), camino(Z,Y).

%?- camino(a, salida).

%Programacion logica - indeterminismo
%Generacion numero

num(1).
num(2).
num(3).

%?- num(X).

%Concatenación en listas

concat([], L,L).
concat([X | L1], L2 , [X| L3]) :- concat(L1,L2,L3).

%?- concat([1,2,3],[2,3,4],R).

%Eliminar elemento de lista

del(X,[X | Resto], Resto).
del(X,[Y | Resto], [Y | R]) :- del(X, Resto, R).

%?- del(1, [1,2,3,4], R).

%Busqueda de elementos

search(X,[X|_]).
search(X,[_|Resto]) :- search(X, Resto).

%?- search(2,[1,3,4]).

% Disponibilidad de colores
color(rojo).
color(azul).
color(verde).

%?- color(X). Respuesta 1er elemento 
%?- color(azul) Respuesta true

% Disponibilidad de comida
comida(pizza).
comida(hamburguesa).
comida(ensalada).

%?- comida(Y) Respuesta 1er elemento
%?- comida(ensalada) Respues true

% Asignación de roles

rol(ana, ingeniera).
rol(juan, doctor).
rol(maria, profesora).

%?-rol(Persona, Rol).

/* 
Realizar un ejemplo de listas con recursividad,
indique el enunciado, la solución y resultados obtenidos.
*/

adicion([], 0).
adicion([X | Y], S) :- adicion(Y, Z),S is X + Z.

%?- sumar([10, 3], S).

/*
Realizar un ejemplo de indeterminismo utilizando listas, 
indique el enunciado, la solución y resultados obtenidos.
*/
reemplazar(_, _, [], []).
reemplazar(A, N, [A | Y], [N | R]) :- reemplazar(A, N, Y, R).
reemplazar(A, N, [X | Y], [X | R]) :- X \= A, reemplazar(A, N, Y, R).

%?- reemplazar(1, 9, [1, 2, 3, 1], R).

/*
Realizar un ejemplo de indeterminismo utilizando caminos con recursividad, 
indique el enunciado, la solución y resultados obtenidos.
*/

conectado(a, b).
conectado(b, c).
conectado(c, d).
conectado(d, e).
conectado(e, f).
conectado(f, g).
conectado(g, h).


arista(X, Y) :- conectado(X, Y).
arista(X, Y) :- conectado(Y, X).

camino(I, F, C) :-
    camino_aux(I, F, [I], CR),
    reverse(CR, C).

camino_aux(F, F, C, C).
camino_aux(I, F, V, C) :-arista(I, N),\+ member(N, V),camino_aux(N, F, [N|V], C).


%?- camino(a, h, Camino).

