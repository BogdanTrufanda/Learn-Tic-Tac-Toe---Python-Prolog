
readfacts:-
    open('C:\~blabla\\output.txt',read,In),
    repeat,
    read_line_to_codes(In,X),writef(" "),
    writef(X),nl,
    X=end_of_file,!,
    nl,
    close(In).


writefacts:-
    open('C:\~blabla\\output.txt',write,Out),
    write(Out,'Age(Peter,30)'),
    write(Out,'Skin(Smith,Black).'),
    close(Out).   
