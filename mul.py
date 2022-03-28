'''def sum(n1,n2):
    return n1+n2
def sub(n1,n2):
     sum(n1,n2)
    return n1-n2

def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
y=sub(10,2)
print(y)

def sum(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    sum(n1,n2)
    print(n1-n2)
def mul(n1,n2):
    sum(n1,n2)
    sub(n1,n2)
    print(n1*n2)
def div(n1,n2):
    sum(n1,n2)
    mul(n1,n2)
    print(n1/n2)    
div(10,4) '''

def sum(n1,n2):
    q=(n1+n2)
    return q
def sub(n1,n2):
    print(sum(n1,n2))
    w=(n1-n2)
    return w
def mul(n1,n2):
    print(sum(n1,n2))
    print(sub(n1,n2))
    a=(n1*n2)
    return a
def div(n1,n2):
    print(sum(n1,n2))
    print(mul(n1,n2))
    s=(n1/n2)
    return s
print(div(10,4))

