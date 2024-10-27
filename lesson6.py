"""
names = ['Bob', 'Alice', 'Mary', 'John']
ages = [10,20,30,40]
genders = ['male','female','female','male']
older_18 = list()

#for k in range(4):
#  if ages[k] > 18:
#    older_18.append(names[k])

for name,age,genders in zip(names, ages, genders):
  if age > 18 and genders == 'male':
    older_18.append(name)
print(older_18)


# LIST COMPREHENSION

# Упражнение 0.  


list_1 = [123,224,213,413,125,216,127,118,139,210]  ## количество пройденных км первого друга за 10 дней
list_2 = [103,243,123,234,123,456,234,345,456,567]  ## количество пройденных км второго друга за 10 дней какое наибольшее количество км они прошли вдвоем за 1 день?
total_walk = list()
value = 0

for list_one, list_two in zip(list_1, list_2):
    total_walk.append(list_one + list_two)
print(f'The maximum distance have walked {max(total_walk)} km')
    
#-----------------------------------------------------------------------------------


# newlist = [expression for item in iterable (if condition)]

Синтаксис list comprehension состоит из следующих компонентов:

iterable: перебираемый источник данных, в качестве которого может выступать список, множество, последовательность, либо даже функция, которая возвращает набор данных, например, range()

item: извлекаемый из источника данных элемент

expression: выражение, которое возвращает некоторое значение. Это значение затем попадает в генерируемый список

condition: условие, которому должны соответствовать извлекаемые из источника данных элементы. Если элемент НЕ удовлетворяет условию, то он НЕ выбирается. Необязательный параметр.


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if 'e' in x]

print(newlist)



# Упражнение 1. Создайте такое list [8,64,216,...20**3] (кубы всех четных чисел до 20 включительно)
list_for_cubes = [n**3 for n in range(21) if n%2 == 0]
print(list_for_cubes)

# Упражнение 2. Cоздайте такой list [(0,1), (1,2), (3,4), ..., (99,100)]
list_1 = [n for n in range(100)]
list_2 = [k + 1 for k in range(100)]
list_zipped = list(zip(list_1, list_2))
print(list_zipped)

#Упражнение 3. Создайте list() в котором написаны полные имена данных людей

names = ['Bob', 'Mary', 'John', 'Josh', 'Petya']
titles = ['Sir', 'Mrs', 'Mr', 'His Highness', 'Prosto']

print(list(zip(titles, names)))

# Упражнение 5. Пользователь вводит целое число, например 5.
# Вы должны напечатать пирамиду высотой равной введенному числому следующим образом:

number = int(input())
for n in range(number):
    print(n + 1, end="")
    for k in range(n):
        print(n + 1, end="")
    print()

# Упражнение 7. Азамат родился в 1993 году. Сейчас 2024 год. В четные годы Азамат тратит 12000 долларов, в нечетные он 
# тратит 12000 + 50 * возраст. Азамату нужен калькулятор, куда вы вводите сумму денег в долларах, а программа говорит до 
# какого года начиная с 2023 Азамату хватит этих денег.

money = int(input())
age = 20
current_year = 2024
print(age)
print(money)
while money >= 0:
    if current_year%2 == 0:
        age = current_year - 1993
        money = money - 12000 - 50 * age
        print(money)
        current_year = current_year + 1
    else:
        age = current_year - 1993
        money = money - 12000
        print(money)
        current_year = current_year + 1
print(current_year)

# Упражнение 8. Есть последовательность чисел: 2, 22, 222, 2222, 22222, 222222......... <br> 
# Пользователь вводит с клавиатуры число N, программа печатает на экран сумму первых n элементов этой последовательности.

number = int(input())
print(number)
i=0
for k in range(number):
    i = i + 1
    for n in range(i):
        if k != i:
            print(number, end="")
    if k != number - 1:
        print(end=",")
    else:
        print(end=".")

# Упражнение 9. Пользователь вводит строку состоящую только из двух символов 'L' и 'R'. в строке введенной пользователем обязательно равное количество 'R' и 'L'. 
# Например 'LLRR' или 'RLRLRL'. Вам нужно сказать пользователю на сколько частей можно разбить его строку таким образом чтобы в каждой части было одинаковое количество символов 'R' и 'L'.

#Например 'LRRLLLRR' можно разбить на такие части: 'LR', 'RL', 'LLRR' - ответ 3.
#Например 'LLLLRRRR' можно разбить только на одну часть 'LLLLRRRR' - ответ 1.
#Например 'LLLRRRRL' можно разбить на две части 'LLLRRR' и 'RL' - ответ 2.
""" 
letters = str(input())
#letter_list = list()
letter_list = list("".join(letters))

print(letters)
print(letter_list)
print(letter_list.count())
print(type(letter_list)) 
"NOT FINISHED"