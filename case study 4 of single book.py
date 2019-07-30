class bookstore:
    bokstona="balaji"
    
    @staticmethod
    def static():
        print(bookstore.bokstona)
        
    def det(self,bn,bna,bt,ba,bp):
        self.bn=bn
        self.bna=bna
        self.bt=bt
        self.ba=ba
        self.bp=bp
        
        
        
    def display(self):
        print(self.bn)
        print(self.bna)
        print(self.bt)
        print(self.ba)
        print(self.bp)
        

    def bill(self):
        qob=int(input("ent qob"))
        bill=qob*(self.bp)
        print("bill=",bill)
      
a=bookstore()
a.static()
a.det(1,'phy','mech','schand',500)
a.display()
a.bill()



