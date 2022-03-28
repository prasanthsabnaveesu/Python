class Account:
    def __init__(self,name,bal):
        self.name=name
        self.bal=bal
    def gd(self):
        print(self.name)
        print(self.bal)
class  Bank:
    def main():
        acc1=Account('dad',5000)
        acc2=Account('mom',5200)
        acc1.gd()
        acc2.gd()
Bank.main()        
