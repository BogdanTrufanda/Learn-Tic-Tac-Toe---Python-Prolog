win(Board, Who) :- row_case_win(Board, Who).
win(Board, Who) :- col_case_win(Board, Who).
win(Board, Who) :- diag_case_win(Board, Who).

row_case_win(Board, Who) :- Board = [Who,Who,Who,_,_,_,_,_,_].
row_case_win(Board, Who) :- Board = [_,_,_,Who,Who,Who,_,_,_].
row_case_win(Board, Who) :- Board = [_,_,_,_,_,_,Who,Who,Who].

col_case_win(Board, Who) :- Board = [Who,_,_,Who,_,_,Who,_,_].
col_case_win(Board, Who) :- Board = [_,Who,_,_,Who,_,_,Who,_].
col_case_win(Board, Who) :- Board = [_,_,Who,_,_,Who,_,_,Who].

diag_case_win(Board, Who) :- Board = [Who,_,_,_,Who,_,_,_,Who].
diag_case_win(Board, Who) :- Board = [_,_,Who,_,Who,_,Who,_,_].

move([b,B,C,D,E,F,G,H,I], Who, [Who,B,C,D,E,F,G,H,I]).
move([A,b,C,D,E,F,G,H,I], Who, [A,Who,C,D,E,F,G,H,I]).
move([A,B,b,D,E,F,G,H,I], Who, [A,B,Who,D,E,F,G,H,I]).
move([A,B,C,b,E,F,G,H,I], Who, [A,B,C,Who,E,F,G,H,I]).
move([A,B,C,D,b,F,G,H,I], Who, [A,B,C,D,Who,F,G,H,I]).
move([A,B,C,D,E,b,G,H,I], Who, [A,B,C,D,E,Who,G,H,I]).
move([A,B,C,D,E,F,b,H,I], Who, [A,B,C,D,E,F,Who,H,I]).
move([A,B,C,D,E,F,G,b,I], Who, [A,B,C,D,E,F,G,Who,I]).
move([A,B,C,D,E,F,G,H,b], Who, [A,B,C,D,E,F,G,H,Who]).

x_can_win_in_one(Board) :- move(Board, x, Newboard), win(Newboard, x).
o_can_win_in_one(Board) :- move(Board, '0', Newboard), win(Newboard, '0').

x_response(Board,Newboard) :-
  move(Board, x, Newboard),
  win(Newboard, x),
  !.
x_response(Board,Newboard) :-
  move(Board, x, Newboard),
  not(o_can_win_in_one(Newboard)).
x_response(Board,Newboard) :-
  move(Board, x, Newboard).
x_response(Board,Newboard) :-
  not(member(b,Board)),
  !,
  open('output.txt',append,OS),
  write(OS,'Cats game!'),
  close(OS),
  Newboard = Board.

o_response(Board,Newboard) :-
  move(Board, '0', Newboard),
  win(Newboard, '0'),
  !.
o_response(Board,Newboard) :-
  move(Board, '0', Newboard),
  not(x_can_win_in_one(Newboard)).
o_response(Board,Newboard) :-
  move(Board, '0', Newboard).
o_response(Board,Newboard) :-
  not(member(b,Board)),
  !,
  open('output.txt',append,OS),
  write(OS,'Cats Game!'),
  close(OS),
  Newboard = Board.

respond('0', Board, Newboard) :-
  o_response(Board, Newboard).
respond(x, Board, Newboard) :-
  x_response(Board, Newboard).

read_from_file(File) :-
    open('output.txt',write,OS),
    write(OS,''),
    close(OS),

    open(File, read, Stream),
   % nb_setval(last,'0'),
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
   %Last = '0',
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


