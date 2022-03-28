
for i in range(1,4):
    pin =int(input('pin'))
    if pin== 1234:
        print('welcome')
        break
    else:
        print('invalid pin')
        if  i==3:
            print('acc block')
            break
        else:
            i<3
            print(' do you continue press 1')
            co=int(input(' press'))
            if co==1  :
                continue
            if co!=1:
                print('thank you')
                break
            else:
                print('Thank you')
        
       
            
            
1
