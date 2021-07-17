
 #1
number = 4
mp = 12*12
f = 2.4
world = 'Hello'
#2
m = 'Yelena'
print (len(m))
print( m.upper())
print( m.lower())
print (m[0])
print( m.count("a"))
#3
m1 = 'My name is '
print("{} + {} = {}".format(m1,m, m1 + m))
print(f'{m1} + {m} = {m1 + m}')
#4
a = int (input ("input 1 st  number:"))
b = int (input("input 2 nd number:"))
print ("The sum a + b = ", a+b)
#5
x = int (input ("input the  number:"))
if x %2 == 0:
  print("the number is even")
else:
    print ("the number is odd")

#6
import random

list = {1,2,3,4,5}
list.add(6)
print(sum(list))
#7
my_movie = ['Titanic','Avengers','The Durassic Park','Avatar']
for movie in my_movie:
   if movie == 'Avatar':
    print("I love Avatar")
    break
#8
randoms = [random.randint(-10, 10) for x in range(10)]
print(randoms)
#9
l = []
while True:
    y = str(input('Enter world: '))
    l.append(y)
    if y == 'exit':
        break
print(l)

#10
sum = 0
while True:
    y = int(input('Enter number: '))
    sum = sum+y
    if y == -1:
        break
print(sum)

#11
for number in range (1,100):
    print(number)

#12
for number in range (1,50,3):
    print(number)

#13
import random

x = list (range(500))

#14
luckyNumber = random.randint(1,10)
myGuess = int(input("Guess the number:"))
while myGuess != luckyNumber :
   print('wrong')
   myGuess = int(input("Guess the number:"))
print('very good')

#15
import random

def double_it (x):
    return x*2
#17
my_set = set()
for x in range (1,1000):
    my_set.add(random.randint(1,10))
print(my_set)
#18
my_dict = {250:'Ironman', 88:'Sinderella',180:'War and Pease',22:'Captane America',250:'Harry Poter'}

def get_key(val):
    for key, value in my_dict.items():
        if val == value:
            return key
    return "key doesn't exist"

print(get_key('War and Pease'))

#19
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.








