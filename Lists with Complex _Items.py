nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
print(nested1[0])
print(len(nested1))
nested1.append(['i'])
print("-------")
for L in nested1:
    print(L)


#['a', 'b', 'c']
#3
#-------
#['a', 'b', 'c']
#['d', 'e']
#['f', 'g', 'h']
#['i']


nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
y = nested1[1]
print(y)
print(y[0])

print([10, 20, 30][1])
print(nested1[1][0])
#['d', 'e']
#d
#20
#d