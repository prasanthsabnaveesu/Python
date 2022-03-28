'''
  p
 y t
h o n
'''
t=input('ent string')
w=0
u=2
y=0
for b in range(1,4,1):
    for f in range(u,0,-1):
        print(' ',end=' ')
    for j in range(1,b+1,1):
            
        print(t[w] ,end=' ')
        w+=1
    print()
    u-=1
    w=y+w
    
