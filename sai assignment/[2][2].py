'''
7 6 5  4 3 2 1  
7 6 5 4 3 2
7 6 5 4 3
7 6 5 4
7 6 5
7 6
7
'''


for c in range(7,0,-1):
    g=7
    for d in range(1,c+1,1):
        print(g,end=' ')
        g-=1
    print()    
