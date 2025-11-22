#Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci. Zadanie należy wykonać w 2 wersjach:
#Wykorzystując pętle for.
""" v1
numbers = [12,32,11,73,8]
for number in numbers:
    print(number*2)
    v2
numbers = [12,32,11,73,8]
numbers_2 = []
for number in numbers:
    numbers_2.append(number*2)

print(numbers_2)
"""

#Wykorzystując listę składaną.
"""
numbers = [12,32,11,73,8]
numbers_2= [(number)*2 for number in numbers]
print(numbers_2)
"""