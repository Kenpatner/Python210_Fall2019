def gridprinter(x,y):
    plus = "+"
    minus = "-"
    line = "|"
    for i in range (x):
        for i in range (x):
            print (plus + y*minus,end = "")
        print (plus)
        for i in range (y):
            for i in range (x):
                print (line + y * " ",end = "")
            print (line)
    for i in range (x):
        print (plus + y*minus,end = "")
    print (plus)
gridprinter(19,3)   
