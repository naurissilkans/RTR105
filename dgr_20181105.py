Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> str1 = "Hello"
>>> str2 = "there"
>>> bob = str1 + str2
>>> print(bob)
Hellothere
>>> 
>>> 
>>> str3 = '123'
>>> str3 = str3 + 1
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    str3 = str3 + 1
TypeError: must be str, not int
>>> x = int(str3) + 1
>>> print(x)
124
>>> 
>>> name = input('Enter:')
Enter:Chuck
>>> print(name)
Chuck
>>> apple = input('Enter:')
Enter:100
>>> x = apple - 10
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x = apple - 10
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x = int(apple) - 10
>>> print(x)
90
>>> 
>>> 
>>> 
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> x = 3
>>> w fruit[x-1]
SyntaxError: invalid syntax
>>> w = fruit[x-1]
>>> print(w)
n
>>> 
>>> 
>>> 
>>> 
>>> zot = 'abc'
>>> print(zot[5])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(zot[5])
IndexError: string index out of range
>>> 
>>> 
>>> 
>>> fruit = 'banana'
>>> print(len(fruit))
6
>>> 
>>> 
>>> 
>>> 
>>> fruit = 'banana'
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index + 1

	
0 b
1 a
2 n
3 a
4 n
5 a
>>> 
>>> 
>>> 
>>> 
>>> fruit = 'banana'
>>> for letter in fruit:
	print(letter)

	
b
a
n
a
n
a
>>> 
>>> 
>>> 
>>> 
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1
print(count)
SyntaxError: invalid syntax
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1
    print(count)
    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> 
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1print(count)
		
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> >>> word = 'banana'
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 

>>> 

>>> 


>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1
   print(count)
   
SyntaxError: unindent does not match any outer indentation level
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1

	
>>> print(count)
3
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> for letter in 'banana':
	print(letter)

	
b
a
n
a
n
a
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s = 'Monty Python'
>>> print(s[0:4])
Mont
>>> print(s[6:7])
P
>>> print(s[6:20])
Python
>>> 
>>> 
>>> 
>>> s = 'Monty Python'
>>> print(s[0:4])
Mont
>>> print(s[:2])
Mo
>>> print(s[8:])
thon
>>> print(s[:])
Monty Python
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a = 'Hello'
>>> b = a + 'There'
>>> print(b)
HelloThere
>>> c = a + '' + 'There'
>>> print(c)
HelloThere
>>> c = a + ' ' + 'There'
>>> print(c)
Hello There
>>> 
>>> 
>>> 
>>> 


>>> 

>>> 

>>> 


>>> fruit = 'banana'
>>> 'n''in frut
SyntaxError: EOL while scanning string literal
>>> fruit = 'banana''n''in frut
SyntaxError: EOL while scanning string literal
>>> fruit = 'banana'
>>> 'n' in fruit
True
>>> 'd' in fruit
False
>>> if 'a' in fruit:
	print('Found it')

	
Found it
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> if word == 'banana':
	print('All right, bananas.')

	
All right, bananas.
>>> if word == 'banana':
	print('Your word,''+ word + ' comes before banana.')
	      
SyntaxError: invalid syntax
>>> if word == 'banana':
	print('Your word,''+ word + ', comes before banana.')
	      
SyntaxError: invalid syntax
>>> if word < 'banana')
	print('Your word,' + word + ', comes before banana.')
	      
SyntaxError: invalid syntax
>>> if word < 'banana':
	print('Your word,' + word + ', comes before banana.')
    elif word > 'banana':
	      
SyntaxError: unindent does not match any outer indentation level
>>> if word < 'banana':
	print('Your word,' + word + ', comes before banana.')

	      
>>> elif word > 'banana':
	      
SyntaxError: invalid syntax
>>> if word < 'banana':
	print('Your word,' + word + ', comes before banana.')
    elif word > 'banana':
	      
SyntaxError: unindent does not match any outer indentation level
>>> if word < 'banana':
	print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
	      print('Your word,' + word + ', comes after banana.')
else:
	      print('All right, bananas.')

	      
All right, bananas.
>>> 
	      
>>> 
	      
>>> 
	      


>>> 
	      

>>> 
	      

>>> 
	      

>>> 
	      

>>> 
	      

>>> 
	      

>>> greet = 'Hello Bob'
	      
>>> zap = greet.lower()
	      
>>> print(zap)
	      
hello bob
>>> print('Hi There'·lower())
	      
SyntaxError: invalid character in identifier
>>> print('Hi There'.lower())
	      
hi there
>>> 
	      
>>> 
	      
>>> 
	      
>>> stuff = 'Hello world'
	      
>>> type(stuff)
	      
<class 'str'>
>>> dir(stuff)
	      
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> print(stuff.capitilize)
	      
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    print(stuff.capitilize)
AttributeError: 'str' object has no attribute 'capitilize'
>>> print(stuff)
	      
Hello world
>>> stuff.lower
	      
<built-in method lower of str object at 0x7f13390b04f0>
>>> stuff.capitilize
	      
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    stuff.capitilize
AttributeError: 'str' object has no attribute 'capitilize'
>>> stuff.capitalize
	      
<built-in method capitalize of str object at 0x7f13390b04f0>
>>> 
	      
>>> 
	      
>>> 
	      


>>> 
	      

>>> 
	      

>>> 
	      


>>> 
	      

>>> 
	      

>>> 
	      


>>> 
	      
>>> 
	      
>>> 
	      
>>> print(stuff.lower.__doc__)
	      
S.lower() -> str

Return a copy of the string S converted to lowercase.
>>> stuff.lower
	      
<built-in method lower of str object at 0x7f13390b04f0>
>>> 
	      
>>> stuff.lower()
	      
'hello world'
>>> stuff.capitalize()
	      
'Hello world'
>>> stuff.casefold()
	      
'hello world'
>>> stuff.center()
	      
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    stuff.center()
TypeError: center() takes at least 1 argument (0 given)
>>> stuff.count()
	      
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    stuff.count()
TypeError: count() takes at least 1 argument (0 given)
>>> 
	      
>>> (stuff.center.__doc__)
	      
'S.center(width[, fillchar]) -> str\n\nReturn S centered in a string of length width. Padding is\ndone using the specified fill character (default is a space)'
>>> (stuff.count.__doc__)
	      
'S.count(sub[, start[, end]]) -> int\n\nReturn the number of non-overlapping occurrences of substring sub in\nstring S[start:end].  Optional arguments start and end are\ninterpreted as in slice notation.'
>>> stuff.swapcase()
	      
'hELLO WORLD'
>>> stuff.translate()
	      
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    stuff.translate()
TypeError: translate() takes exactly one argument (0 given)
>>> 
	      
>>> 
	      


>>> 
	      

>>> 
	      

>>> 
	      

>>> 
	      


>>> 
	      

>>> 
	      

>>> 
	      


>>> 
	      
>>> 
	      


>>> fruit = 'banana'
	      
>>> pos = fruit.find('na'°
		     
SyntaxError: invalid character in identifier
>>> pos = fruit.find('na')
		     
>>> print(pos)
		     
2
>>> aa = fruit.find('z')
		     
>>> print(aa)
		     
-1
>>> 
		     
>>> 
		     
>>> greet = 'Hello Bob'
		     
>>> nnn = greet.upper()
		     
>>> print(nnn)
		     
HELLO BOB
>>> www = greet.lower()
		     
>>> print(www)
		     
hello bob
>>> 
		     
>>> 
		     
>>> greet = 'Hello Bob'
		     
>>> nstr = greet.replace('Bob','Jane')
		     
>>> print(nstr)
		     
Hello Jane
>>> nstr = greet.replace('o','X')
		     
>>> print(nstr)
		     
HellX BXb
>>> 
		     
>>> 
		     
>>> greet = '   Hello Bob   '
		     
>>> greet.lstrip()
		     
'Hello Bob   '
>>> greet.rstrip()
		     
'   Hello Bob'
>>> greet.strip()
		     
'Hello Bob'
>>> 
		     
>>> 
		     
>>> line = 'Please have a nice day'
		     
>>> line.startswitith('Please')
		     
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    line.startswitith('Please')
AttributeError: 'str' object has no attribute 'startswitith'
>>> line.startswith('Please')
		     
True
>>> line.startswith('p')
		     
False
>>> 
		     
>>> 
		     
>>> 
