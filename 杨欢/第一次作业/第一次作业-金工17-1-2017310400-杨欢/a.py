numbers=list(range(2,100))
squares=[]
for a in numbers:
    dividers=list(range(2,a))
    for b in dividers:
        c=a%b
        if c!=0:
            squares.append(c)
            d=len(squares)
            print(d)
