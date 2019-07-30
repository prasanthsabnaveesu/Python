class classname:
    outof=300
    @staticmethod
   
    def marks(self,name,rol,ms,mm,me):
        self.name=name
        self.rol=rol
        self.ms=ms
        self.mm=mm
        self.me=me
        (self.total)=self.ms+self.me+self.mm
        self.percen=(self.total/self.outof)*100
    def display(self):
        print(self.name)
        print(self.rol)
        print(self.ms)
        print(self.mm)
        print(self.me)
        print(self.total)
        print(self.percen)
a=classname()

a.marks("pavan",1,90,98,95)
a.display()
print()
b=classname()
b.marks("sai",2,96,94,97)
b.display()
print()
c=classname()
c.marks("Prasanth",3,95,92,99)
c.display()
d=classname()
d.marks("sabnaveesu",4,95,92,99)
d.display()
e=classname()
e.marks("spsp",5,95,92,99)
e.display()
         
