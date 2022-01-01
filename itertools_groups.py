''' GROUP 1 '''

#count()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from itertools import count

pet_names = ["Biscoff", "Foxx", "Broccoli"]

# count prints out integers for
# each value in my list
for i in zip(count(start=1,
                   step=1), pet_names):
    # prints tuple in an enumerated
    # format
    print(i)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#compress()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import itertools

Answers = ['Patterdale', 'Persian', 'Alsatian', 'Ragdoll', 'Jack Russel']
Are_dog_breeds = [True, False, True, False, True]
Are_cat_breed = [False, True, False, True]
Are_great_pets = [True, True, True, True, True]


Dog_Breed_Correct_Answers = itertools.compress(Answers, Are_dog_breeds)
Cat_breeds_correct_answers = itertools.compress(Answers, Are_cat_breed)
Great_breed_correct_answers = itertools.compress(Answers, Are_great_pets)
for each in Dog_Breed_Correct_Answers:
    print(each + ' is a dog breed')

for each in Cat_breeds_correct_answers:
    print(each + ' is a breed of cat')

for each in Great_breed_correct_answers:
    print(each + ' is a great pet')

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#permutations()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
string = "Tea"

p = permutations(string)

for j in list(p):
    print(j)

# From a set of possible answers

answer_choices = {".append()", ".addition()", ".plus()", ".addon()"}

ac = permutations(answer_choices)

for j in set(ac):
    print("What method do you use to add an item to the end of a list?")
    print(j)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



''' GROUP 2 '''

#cycle()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import itertools
x=itertools.cycle([1,2,3])

# On-demand cycle
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


# Infinite loop
# for i in x:
#     print(i)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#iSlice()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
str_ = "CFGNanodegree"

print("Example 1")
for i in islice(str_, 5):
    print(i)
    
print("Example 2")
for i in islice(str_, 1, len(str_),2):
    print(i)
   
   
print("Example 3")
for i in islice(str_, 1, 5, 2):
    print(i)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#combinations()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Version 1 
from itertools import combinations

ingredients = ['glyceryl stearate', 'glycerine', 'stearaikonium chloride', 'stearyl alcohol', 'myristal myristate']

# size of combination is set to 3
a = combinations(ingredients, 3)
y = [', '.join(i) for i in a]

print(y)

# Version 2 
from itertools import combinations

letters = "ABCDEF"

# size of combination is set to 3
a = combinations(letters, 3)
y = [' '.join(i) for i in a]

print(y)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


''' GROUP 3 '''

# TO DE ADDED


''' GROUP 4 '''

#dropwhile()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import itertools

my_list = [1,2,3,4,5,6,7,8,9,10]

new_list = itertools.dropwhile(lambda x: x<6, my_list)

#will drop every element while the condition is true
#on the first element where the condition is false -> when reaches 6, it stop dropping elements,
#and for there on, it returns every element on the list / iterable

print(list(new_list))

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#takewhile()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import itertools

my_other_list = itertools.takewhile(lambda x: x<6, my_list)

#will return every element as long as the condition is true -> when reaches 6, stop returning elements, and
#for there on, drops every element on the list / iterable

print(list(my_other_list))

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#chain() 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
first_list_of_numbers = [1,2,3,4]
second_list_of_numbers = [5,6,7,8]

list_of_all_numbers = itertools.chain(first_list_of_numbers, second_list_of_numbers)

#Chain method will return all elements of the first iterable, then all the elements of the second iterable
#treating both as a single sequence.

print(list(list_of_all_numbers))

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<











