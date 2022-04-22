#When each item is transformed we say that the operation is a mapping, or just a map of the original list.
# When some items are omitted, we call it a filter.

#Python provides built-in functions map and filter. Python also provides a new syntax, called list comprehensions
def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)
#[2, 5, 9]
#[4, 10, 18]


def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)
#[6, 15, 27]
#[8, 20, 36]

things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))
#[8, 20, 36]
#[5, 10, 15]


#filter

def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = list(filter((lambda x: "w" in x), lst_check))

    #LIST COMPREHENSION
things = [2, 5, 9]

yourlist = [value * 2 for value in things]

print(yourlist)


things = [3, 4, 6, 7, 0, 1]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])


#print names
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

compri=[d['name'] for d in tester["info"]]
print(compri)


#The zip function takes multiple lists and turns them into a list of tuples (actually, an iterator, but they work like
# lists for most practical purposes), pairing up all the first items as one tuple, all the second items as a tuple, and so on.

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L4 = list(zip(L1, L2))
print(L4)
#[(3, 1), (4, 2), (5, 3)]

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L4 = list(zip(L1, L2))

for (x1, x2) in L4:
    L3.append(x1+x2)

print(L3)
#[4, 6, 8]

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)
#[4, 6, 8]

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
l3 = zip(l1, l2)
opposites=list(filter(lambda s:len(s[0])>3 and len(s[1]) >3 ,l3))
print(opposites)
#[('left', 'right'), ('front', 'back')]