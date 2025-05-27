%Control de ejecucion


%%%MAYUSCULAS """X"""


%Regla orden de aparicion
hora(8).
hora(15).

saludo(buenos_dias) :- hora(8).
saludo(buenas_tarde) :- hora(15).
%? saludo(x).

%Backtraking
color('rojo').
color('azul').
%?- color(x). %Respuesta x = rojo


%operador
mensaje(positivo) :- !, write('todo esta bien').
mensaje(negativo) :- write('algo salio mal').
%?- mensaje(positivo). %respuesta: 'todo esta bien'

%ejercicio propuesto 02

%control de ejecucion de lista
longitud([],0).
longitud([_|resto],N) :- longitud(resto, M), N is M + 1.

%uso de corte para evitar multiples soluciones
es_mayor(x, y) :- x > y , !.
es_mayor(_,_) :- write('no es mayor').
 
%control de ejecucion
buscar(x,[x|_]).
buscar(x,[x|_]resto) :- buscar(x,resto).