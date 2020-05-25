init :- 					nb_setval(database, "").

learn(LISTA) :- 			nb_getval(database, LISTA_MARE), 
							atomics_to_string(LISTA, STRING),
							string_concat(LISTA_MARE, STRING, LISTA_MARE2),
							string_concat(LISTA_MARE2, "\n", LISTA_MARE3),
							nb_setval(database, LISTA_MARE3).

display(A) :- 				nb_getval(database, LISTA_MARE),
							A = LISTA_MARE.
				
verify(LISTA, Result) :- 	nb_getval(database, LISTA_MARE), 
							atomics_to_string(LISTA, Search),
							sub_string(LISTA_MARE, Before, _, _, Search),
							length(LISTA, LEN),
							Index is Before + LEN * 2,
							sub_string(LISTA_MARE, Index, 1, _, Result).
				