def gridprinter(n):
    plus = "+"
    minus = "-"
    line = "|"
    print (plus + minus *n + plus+ minus *n + plus)
    for i in (range(n)):
        print (line+ " "*n + line + " "*n+line)
    print (plus + minus *n + plus+ minus *n + plus)
    for i in (range(n)):
        print (line+ " "*n + line + " "*n+line)
gridprinter(7)