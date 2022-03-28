'''
1 
2 1 
4 2 1 
8 4 2 1 
16 8 4 2 1
'''
w=1
r=1
for q in range(1,6,1):
    
    for t in range(1,q+1,1):
        print(w,end=' ')
       
        w=w/2
        
    print()
    w=w*2
