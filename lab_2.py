#Boolean Values
a = 100
b = 27

if b > a:
    print("b is greater than a")
elif(b == a):
    print("b is equal to a")
else:   
    print("a is greater than b")

#Python Operators
x = 3
y = 5
#(+)Addition:
x + y	
#(-)Subtraction:
x - y
#(*)Multiplication:
x * y
#(/)Division:
x / y	
#(%)Modulus:
x % y
#(**)Exponentiation:
x ** y	
#(//)Floor division:
x // y
#(=)
x = 5	
#(+=)
x = x + 3	
#(-=)
x = x - 3	
#(*=)
x = x * 3	
#(/=)
x = x / 3	
#(%=)
x = x % 3	
#(//=)
x = x // 3	
#(**=)
x = x ** 3	
#(&=)
x = x & 3	
#(|=)
x = x | 3	
#(^=)
x = x ^ 3	
#(>>=)
x = x >> 3	
#(<<=)
x = x << 3	
#(:=)
print(x := 3)	
x = 3


#List
list = ["Ann", "Kate", "Sophie"]
print(list)

#Access Items
list = ["Ann", "Kate", "Sophie"]
print(list[1])

#Change Item Value
list = ["Ann", "Kate", "Sophie"]
list[1] = "Viktoria"
print(list)

#Append Items
list = ["Ann", "Kate", "Sophie"]
list.append("Viktoria")
print(list)

#Remove Specified Item
list = ["Ann", "Kate", "Sophie"]
list.remove("Kate")
print(list)

#Loop Through a List
list = ["Ann", "Kate", "Sophie"]
for x in list:
  print(x)

#List Comprehension
cars = ["porshe", "bmw", "mersedes", "ferrari", "ford"]
newlist = []
for x in cars:
  if "e" in x:
    newlist.append(x)
print(newlist)

#Sort List Alphanumerically
list = ["Ann", "Kate", "Sophie"]
list.sort()
print(list)

#Copy Lists
list = ["Ann", "Kate", "Sophie"]
mylist = list.copy()
print(mylist)

#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#List Methods
"append()	Adds an element at the end of the list"
"clear()	Removes all the elements from the list"
"copy()	Returns a copy of the list"
"count()	Returns the number of elements with the specified value"
"extend()	Add the elements of a list (or any iterable), to the end of the current list"
"index()	Returns the index of the first element with the specified value"
"insert()	Adds an element at the specified position"
"pop()	Removes the element at the specified position"
"remove()	Removes the item with the specified value"
"reverse()	Reverses the order of the list"
"sort()	Sorts the list"


#Tuple
tuple = ("Ann", "Kate", "Sophie")
print(tuple)

#Access Tuple Items
tuple = ("Ann", "Kate", "Sophie")
print(tuple[1])

#Change Tuple Values
x = ("Ann", "Kate", "Sophie")
y = list(x)
y[1] = "Viktoria"
x = tuple(y)
print(x)

#Unpacking a Tuple
tuple = ("Ann", "Kate", "Sophie")
(green, yellow, red) = tuple
print(green)
print(yellow)
print(red)

#Loop Through a Tuple
tuple = ("Ann", "Kate", "Sophie")
for x in tuple:
  print(x)

#Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Tuple Methods
"count()	Returns the number of times a specified value occurs in a tuple"
"index()	Searches the tuple for a specified value and returns the position of where it was found"


#Set
set = {"Ann", "Kate", "Sophie"}

#Access Items
set = {"Ann", "Kate", "Sophie"}
for x in set:
  print(x)

#Add Items
set = {"Ann", "Kate", "Sophie"}
set.add("orange")
print(set)

#Remove Item
set = {"Ann", "Kate", "Sophie"}
set.remove("banana")
print(set)

#Loop Items
set = {"Ann", "Kate", "Sophie"}
for x in set:
  print(x)

#Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#Set Methods
"add()	 	                         Adds an element to the set"
"clear()	 	                    Removes all the elements from the set"
"copy()	 	                        Returns a copy of the set"
"difference()	                -	Returns a set containing the difference between two or more sets"
"difference_update()        	-=	Removes the items in this set that are also included in another, specified set"
"discard()	 	                    Remove the specified item"
"intersection()	                &   Returns a set, that is the intersection of two other sets"
"intersection_update()	        &=	Removes the items in this set that are not present in other, specified set(s)"
"isdisjoint()	 	                Returns whether two sets have a intersection or not"
"issubset()	                    <=	Returns whether another set contains this set or not"
"                                <  Returns whether all items in this set is present in other, specified set(s)"
"issuperset()	                 >  Returns whether this set contains another set or not"
" 	                             >	Returns whether all items in other, specified set(s) is present in this set"
"pop()	 	                        Removes an element from the set"
"remove()	 	                    Removes the specified element"
"symmetric_difference()	        ^	Returns a set with the symmetric differences of two sets"
"symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another"
"union()	                    |	Return a set containing the union of sets"
"update()	                    |=	Update the set with the union of this set and others"

#Dictionary
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Accessing Items
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = dict["model"]

#Change Values
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict["year"] = 2018

#Adding Items
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict["color"] = "red"
print(dict)

#Removing Items
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict.pop("model")
print(dict)

#Loop Through a Dictionary
for x in dict:
  print(x)

#Copy a Dictionary
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict.copy()
print(mydict)

#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Roman",
    "year" : 2000
  },
  "child2" : {
    "name" : "Veronika",
    "year" : 2007
  }
}

#Dictionary Methods
"clear()	Removes all the elements from the dictionary"
"copy()	Returns a copy of the dictionary"
"fromkeys()	Returns a dictionary with the specified keys and value"
"get()	Returns the value of the specified key"
"items()	Returns a list containing a tuple for each key value pair"
"keys()	Returns a list containing the dictionary's keys"
"pop()	Removes the element with the specified key"
"popitem()	Removes the last inserted key-value pair"
"setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value"
"update()	Updates the dictionary with the specified key-value pairs"
"alues()	Returns a list of all the values in the dictionary"

#Python If ... Else
a = 27
b = 100
if b > a:
  print("b is greater than a")

#While loop
i = 1
while i < 11:
  print(i)
  i += 1

#For loop
cars = ["porshe", "bmw", "mersedes", "ferrari", "ford"]
for x in cars:
  print(x)






