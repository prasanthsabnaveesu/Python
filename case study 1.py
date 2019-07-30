class bank:
    def details(self,acna,acno,toa,inbal):
        self.acna=acna
        self.acno=acno
        self.toa=toa
        self.inbal=inbal
    def dis(self):
        print(self.acna)
        print(self.acno)
        print(self.toa)
        print(self.inbal)
    def deposit(self):
        deposit=int(input("ent depo ant"))
        self.inbal=deposit+self.inbal
        print(self.inbal)
    def wdac(self):
        wda=int(input("ent wda"))
        fbal=self.inbal-wda
        print(fbal)

a=bank()
a.details('sai',234,'sav',10000)
a.dis()
a.deposit()
a.wdac()
