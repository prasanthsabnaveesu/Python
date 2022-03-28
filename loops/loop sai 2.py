'''
* * * * *
* * * *
* * *
* *
*'''

for x in range(1,6,1):   #a<b  
    for y in range(6,x,-1):  # a>b
        print('*', end=' ')
    print()
'''
      x     y                       o/p
      1     6, 5,4,3,2,1              * * * * ter
      2      5,4,3,2                * * * ter
      3      5,4,3                     * * ter
      4       5,4                       * ter
      5       5                            ter


'''
