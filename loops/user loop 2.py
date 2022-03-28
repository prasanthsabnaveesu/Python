'''
n
oh
typ
'''  
j='python'
#j.reverse()
k=len(j)-1

for x in range(1,4,1) :
    for y in range(1,x+1,1): # 1<4, 2<4, 3<4
        print(j[k],end=' ')
        k=k-1
    print()    
        
