class Comp:
    def __init__(mark,idno,name):
        mark.idn=idno
        mark.nam=name
    def you(hi):
        print(hi.idn)
        print(hi.nam)
e=Comp(100,'sai')

e.you()

#Comp(w,100,'sai')
#Comp.you(w)
