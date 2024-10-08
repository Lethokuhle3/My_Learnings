**PYTHON INTRODUCTION** 

**Python Collections (Arrays)**
There are four collection data types in the Python programming language

*TUPLES:*

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable and they allow duplicates values.
Tuples are written with round brackets.


```py
mytuple = ("apple", "banana", "cherry")
 print(mytuple)

#To check how many items are in this tuple use:
print(len(mytuple))


#To create a tuple with only one item(if you dont put the comma, python will think its a string)
thistuple = ("apple",) #add a comma
 print(type(thistuple)) #tuple 

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

........#Check if Item Exists:

if "apple" in tuple1:
 print("Yes, 'apple' is in the fruits tuple")

#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple. 
tuple1 = ("apple", "banana", "cherry")
y = list(tuple1)
y[1] = "kiwi"
x = tuple(y)

print(x)

#you can also add stuff
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


#When we create a tuple, we normally assign values to it. This is called "packing" a tuple
fruits = ("apple", "banana", "cherry")

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```



*List:*

Lists are used to store multiple items in a single variable.List Items, Ordered, Changeable and allow Duplicates.
```py
mylist = ["apple", "banana", "cherry"]


nums=[1,2,3,4,5,6]
nums.reverse()
print(nums)

```

*Set:*

Sets are used to store multiple items in a single variable.A set is a collection which is unordered, unchangeable*, and unindexed, no duplicates.
```py
myset = {"apple", "banana", "cherry"}


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
```

*Dictionary:*

Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

```py
band={"Vocals":"plants",
       "Guitar":"page"}

       
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
```
You can also write it like this:
```py
band2 = dict(vocals="plants", guitar ="page")
```





**PYTHON LAMBDA:**

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

*Laambda arguments : expression*
```py
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
--------------------

def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))
```

**CLASS:**

 Class is like an object constructor, or a "blueprint" for creating objects.
 ```py
class MyClass:
  x = 5

  #Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)
 ```

 *Python Inheritance:*
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

```py
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```