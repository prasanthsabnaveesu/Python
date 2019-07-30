class classname:
    stu_name="sai"
    roll_no=473281
    outof=300
    @staticmethod
    def static():
        print(classname.stu_name)
        print(classname.roll_no)
    
    def marks(self,ms,mm,me):
        
        self.ms=ms
        self.mm=mm
        self.me=me
        (self.total)=self.ms+self.me+self.mm
        self.percen=(self.total/self.outof)*100
        

        
       
    def display(self):
        print(self.ms)
        print(self.mm)
        print(self.me)
        print(self.total)
        print(self.percen)
a=classname()

a.marks(90,90,90)
a.display()        
         
