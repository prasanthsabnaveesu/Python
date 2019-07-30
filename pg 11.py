e=0
for x in range(0,2):
    for y in range(0,3):
        if x==1:
            print(y,end=' ')
        elif x==0:
            print(x,end=' ')
        else:
            print(e,end=' ')
            e+=2
    print()
