print("welcome to yatra.com")
date=(1,8,15,22,30)
print('choose any date among these:',date)
package=('dis_ind','hol_hun','pil_pac')
print('Available any packages',package)
cn=input('name')
npa=int(input('npa'))
temp=(input('Enter the package name:'))
print(temp)

tsd=input('start date')
dis_ind=10000
hol_hun=15000
pil_pac=20000

class Tour:
    
    @staticmethod
    def date():
        
        if temp=="dis_ind":
           return( x.dis_ind())
        elif temp=="hol_hun":
            return(x.hol_hun())
        elif temp=="pil_pac":
             return(x.pil_pac())
        else:
            print("choose correct package")     
                     
    def dis_ind(self):
        total=npa*dis_ind
        print(total)
       
    def hol_hun(self):
        
        total=npa*hol_hun
        print(total)
       
    def pil_pac(self):
       
        total=npa*20000
        print(total)

x=Tour()
Tour.date()



