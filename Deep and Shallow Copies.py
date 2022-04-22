original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = original[:]
print(copied_version)
print(copied_version is original)
print(copied_version == original)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_version)
#[['dogs', 'puppies'], ['cats', 'kittens']]
#False
#True
#[['dogs', 'puppies', ['canines']], ['cats', 'kittens']]
#-------- Now look at the copied version -----------
#[['dogs', 'puppies', ['canines']], ['cats', 'kittens']]


original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = []
    for item in inner_list:
        copied_inner_list.append(item)
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)

original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = inner_list[:]
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)


#[['dogs', 'puppies'], ['cats', 'kittens']]
#[['dogs', 'puppies', ['canines']], ['cats', 'kittens']]
#-------- Now look at the copied version -----------
#[['dogs', 'puppies'], ['cats', 'kittens']]



#This process above works fine when there are only two layers or levels in a nested list. However,
# if we want to make a copy of a nested list that has more than two levels, then we recommend using the copy module.
# In the copy module there is a method called deepcopy that will take care of the operation for you.

import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])
print("-------- Original -----------")
print(original)
print("-------- deep copy -----------")
print(deeply_copied_version)
print("-------- shallow copy -----------")
print(shallow_copy_version)


#------- Original -----------
#[['canines', ['dogs', 'puppies'], ['marsupials']], ['felines', ['cats', 'kittens']], 'Hi there']
#-------- deep copy -----------
#[['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
#-------- shallow copy -----------
#[['canines', ['dogs', 'puppies'], ['marsupials']], ['felines', ['cats', 'kittens']]]
