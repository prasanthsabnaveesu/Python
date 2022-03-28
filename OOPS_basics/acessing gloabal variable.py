a=10
class test:
    a=20
    def f1():
        a=30
        print("class",test.a)
        print("local",a)
    def f2():
        print("class test",test.a)
        print("local",a)
    def main():
        test.f1()
        test.f2()
        return

test.main()        
