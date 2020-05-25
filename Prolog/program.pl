win(Board, Player) :- rowwin(Board, Player).
win(Board, Player) :- colwin(Board, Player).
win(Board, Player) :- diagwin(Board, Player).

rowwin(Board, Player) :- Board = [Player,Player,Player,_,_,_,_,_,_].
rowwin(Board, Player) :- Board = [_,_,_,Player,Player,Player,_,_,_].
rowwin(Board, Player) :- Board = [_,_,_,_,_,_,Player,Player,Player].

colwin(Board, Player) :- Board = [Player,_,_,Player,_,_,Player,_,_].
colwin(Board, Player) :- Board = [_,Player,_,_,Player,_,_,Player,_].
colwin(Board, Player) :- Board = [_,_,Player,_,_,Player,_,_,Player].

diagwin(Board, Player) :- Board = [Player,_,_,_,Player,_,_,_,Player].
diagwin(Board, Player) :- Board = [_,_,Player,_,Player,_,Player,_,_].

move([b,B,C,D,E,F,G,H,I], Player, [Player,B,C,D,E,F,G,H,I]).
move([A,b,C,D,E,F,G,H,I], Player, [A,Player,C,D,E,F,G,H,I]).
move([A,B,b,D,E,F,G,H,I], Player, [A,B,Player,D,E,F,G,H,I]).
move([A,B,C,b,E,F,G,H,I], Player, [A,B,C,Player,E,F,G,H,I]).
move([A,B,C,D,b,F,G,H,I], Player, [A,B,C,D,Player,F,G,H,I]).
move([A,B,C,D,E,b,G,H,I], Player, [A,B,C,D,E,Player,G,H,I]).
move([A,B,C,D,E,F,b,H,I], Player, [A,B,C,D,E,F,Player,H,I]).
move([A,B,C,D,E,F,G,b,I], Player, [A,B,C,D,E,F,G,Player,I]).
move([A,B,C,D,E,F,G,H,b], Player, [A,B,C,D,E,F,G,H,Player]).

x_can_win_in_one(Board) :- move(Board, x, Newboard), win(Newboard, x).
o_can_win_in_one(Board) :- move(Board, '0', Newboard), win(Newboard, '0').

xrespond(Board,Newboard) :-
  move(Board, x, Newboard),
  win(Newboard, x),
  !.
xrespond(Board,Newboard) :-
  move(Board, x, Newboard),
  not(o_can_win_in_one(Newboard)).
xrespond(Board,Newboard) :-
  move(Board, x, Newboard).
xrespond(Board,Newboard) :-
  not(member(b,Board)),
  !,
  open('output.txt',append,OS),
  write(OS,'Cats game!'),
  close(OS),
  Newboard = Board.

orespond(Board,Newboard) :-
  move(Board, '0', Newboard),
  win(Newboard, '0'),
  !.
orespond(Board,Newboard) :-
  move(Board, '0', Newboard),
  not(x_can_win_in_one(Newboard)).
orespond(Board,Newboard) :-
  move(Board, '0', Newboard).
orespond(Board,Newboard) :-
  not(member(b,Board)),
  !,
  open('output.txt',append,OS),
  write(OS,'Cats Game!'),
  close(OS),
  Newboard = Board.

respond('0', Board, Newboard) :-
  orespond(Board, Newboard).
respond(x, Board, Newboard) :-
  xrespond(Board, Newboard).

read_from_file(File) :-
    open('output.txt',write,OS),
    write(OS,''),
    close(OS),

    open(File, read, Stream),
    nb_setval(mylist, [a,b,c,d,e,f,g,h,i]),
    nb_getval(mylist, Board),
    get_char(Stream, Char1),
    process_the_stream(Char1, Stream, Board),
    close(Stream).

process_the_stream(end_of_file, _, Board) :-
    replace(a,b, Board, R),
    replace(c,b, R, R1),
    replace(d,b, R1, R2),
    replace(e,b, R2, R3),
    replace(f,b, R3, R4),
    replace(g,b, R4, R5),
    replace(h,b, R5, R6),
    replace(i,b, R6, R7),

   %write(R7),

    nb_getval(last,Last),
    other(Last,Next),
    respond(Next, R7, Newboard),

   %write(Newboard),

    open('output.txt',write,OS),
    write(OS,Next),
    close(OS),
    get_first(R7, Newboard, [1,2,3,4,5,6,7,8,9]),
    !.

process_the_stream(Char, Stream, Board) :-
    get_char(Stream, Char1),
    nb_setval(last, Char1),
    get_char(Stream, _),
    get_char(Stream, Char3),
    replace(Char, Char1, Board, Rez),
    process_the_stream(Char3, Stream, Rez).

replace(_, _, [], []).
replace(O, R, [O|T], [R|T2]) :- replace(O, R, T, T2).
replace(O, R, [H|T], [H|T2]) :- H \= O, replace(O, R, T, T2).

other(x,'0').
other('0',x).

get_first([],[],[]) :- nb_setval(first,false), nb_getval(first,R),
                       open('output.txt',append,OS),
                       write(OS,R),
                       close(OS).
get_first([H|T],[H|T1],[_|It]) :- get_first(T,T1,It).
get_first([_|_],[_|_],[Ih|_]) :- nb_setval(first,Ih), nb_getval(first,R),
                       open('output.txt',append,OS),
                       write(OS,R),
                       close(OS).







iterate_list([]).

iterate_list([Head|Tail]):-
	write(Head),
	write(' '),
	iterate_list(Tail).

list_append(A,Tail,[A|Tail]).

myfunc() :-    list_append(a,[b,c,d,e,f,g,h,i],L),
    write(L),
    iterate_list(L).

func([]) :- nb_setval(mylist, [a,b,c,d,e,f,g,h,i]),
            nb_getval(mylist, CounterValue),write(CounterValue),
            replace(c,x,CounterValue,Rez),
            write(Rez),
            nb_setval(mylist, Rez),
            nb_getval(mylist, CounterValue),write(CounterValue),
            replace(a,x,CounterValue,Rez),
            write(Rez).


