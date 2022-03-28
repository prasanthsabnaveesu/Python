'''
s=(x for x in range(1,6))
print(s)
for x in s:
    print(x)

r= [  x for x in range(1,5) ]
print(r)

r={1:2,3:4}
g={x*6 for x in r.values()}
print(g)

r={1:2,3:4}
g={x for x in r.items()}
print(g)
'''
r= [  x for x in range(1,5) while True  ]
print(r)
