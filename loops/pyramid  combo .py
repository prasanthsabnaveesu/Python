'''
- - * - -
- * - * -
* - * - *
- * - * -
- - * - -
'''
h=2
for u in range(1,4,1):
    for a in range(h,0,-1):
        print(' ',end=' ')
        
    for b in range(1,u+1,1):
        print('* ',end=' ')
    print()    
    h-=1    
o=2
g=1
for c in range(1,3,1):
    for d in range(o,3,1): #2
        print(' ',end=' ')
        
    for e in range(g,3,1):
        print('* ',end=' ')
      
    print()    
    o-=1
    g+=1
    
