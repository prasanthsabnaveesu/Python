#Q)6
print(' * even and odd numbers from a sequence')
n=1,2,3,4,5,6,7
o=0
e=0
for x in n:
    if x%2==0:
        e+=1
    else:
        o+=1
print(o)
print(e)
print()  
print(' * printing each element and type from list')
#Q)7
v=[1452,11.23,1+2j,True,'sathya',(0,-1),[5,12],{'class':'v','sec':'A'}]
for x in v:
    print(x,type(x))
print()    
print(' * skipping 3 and 6 from range')
#Q)8
for x in range(0,7):
    if x==3 or x==6:
        continue
    print(x)  
     
    
           
   
    
