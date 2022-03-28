'''
--s
-in
dhu


'''
d=int(input("rows "))  #3
e='sindhu'

#w=len(e)
h=0
for x in range(1,d+1,1): 
    for y in range(x,d,1):
        print('-',end=' ')
    
    for r in range(1,x+1,1):  # 1<4, 2<4 3<4
        print(e[h],end=' ')
        h+=1
            
    print()   
