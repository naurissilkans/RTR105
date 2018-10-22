Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def thing():
	print('Hello')
	print('Fun')

	
>>> 
>>> thing()
Hello
Fun
>>> print('Zip')
Zip
>>> thing()
Hello
Fun
>>> 
>>> 
>>> 
>>> big = max('Hello world')
>>> print(big)
w
>>> tiny = min('Hello world')
>>> print(tiny)
 
>>> 
>>> 
>>> 
>>> 
print(float(99)/100)
0.99
>>> i = 42
>>> type(i)
<class 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<class 'float'>
>>> print(1 + 2 * float(3)/4 - 5)
-2.5
>>> 

>>> 
>>> 
>>> sval = '123'
>>> type(sval)
<class 'str'>
>>> print(sval + 1)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(sval + 1)
TypeError: must be str, not int
>>> ival = int(sval)
>>> type(ival)
<class 'int'>
>>> print(ival + 1)
124
>>> nsv = 'hello bob'
>>> niv = int(nsv)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> 
>>> 
>>> 
>>> 
>>> def print_text():
	print("Kā iet?")
	print("Normāli?")

	
>>> print_text
<function print_text at 0x7f5b0833eb70>
>>> print_text():
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> print_text()
Kā iet?
Normāli?
>>> 
>>> 
>>> def greet(lang):
	if lang == 'es':
		print('Hola')
		elif lang == 'fr':
			
SyntaxError: invalid syntax
>>> 
>>> 
>>> def greet(lang):
	if lang == 'es':
		print('Hola')
		elif lang == 'fr':
			
SyntaxError: invalid syntax
>>> def greet(lang):
	if lang == 'es':
		print('Hola')
		elif lang == 'fr':
			
SyntaxError: invalid syntax
>>> def greet(lang):
	if lang == 'es':
		print('Hola')
		elif lang == 'fr':
			
SyntaxError: invalid syntax
>>> def greet(lang):
	if lang == 'es':
		print('Hola')
		elif lang == 'fr':	print('Bonjour')
		
SyntaxError: invalid syntax
>>> 
>>> def greet(lang):
	if lang == 'es':
		print('Hola')
	elif lang == 'fr':
		print('Bonjour')
	else:
		print('Hello')

		
>>> greet('en'°
	  
SyntaxError: invalid character in identifier
>>> greet('en')
	  
Hello
>>> 
	  
>>> greet('es')
	  
Hola
>>> greet('fr')
	  
Bonjour
>>> 
	  
>>> 
	  
>>> 
	  
>>> def greet():
	  return "Hello"

	  
>>> print(greet(), "Glenn")
	  
Hello Glenn
>>> 
	  
>>> 
	  
>>> 
	  
>>> def greet(lang):
	  if lang == 'es':
	  return 'Hola'
	  
SyntaxError: expected an indented block
>>> def greet(lang):
	  if lang == 'es':
	return 'Hola'
	  
SyntaxError: unindent does not match any outer indentation level
>>> 
	  
>>> 
	  
>>> def greet(lang):
	  if lang == 'es':
		  return 'Hola'
	  elif lang == 'fr':
		  return 'Bonjour'
	  else:
		  return 'Hello'

	  
>>> print(greet('en'), 'Glenn')
	  
Hello Glenn
>>> print(greet('es'), 'Šally')
	  
Hola Šally
>>> 
	  
>>> 
	  
>>>  def computepay():
	  
SyntaxError: unexpected indent
>>> hrs = input('Ievadiet savas nostrādātās stundas.')
	  
Ievadiet savas nostrādātās stundas.45
>>> rate = input('Īevadiet savu stundas likmi.')
	  
Īevadiet savu stundas likmi.10
>>> def computepay():
	  if hrs > 40;
	  
SyntaxError: invalid syntax
>>> def computepay():
	  if hrs > 40:
	  print(hrs * rate)
	  
SyntaxError: expected an indented block
>>> 
	  
>>> def computepay():
	  if hrs > 40:
	  return hrs * rate
	  
SyntaxError: expected an indented block
>>> 
	  
>>> 
	  
>>> 
	  



>>> 
	  
>>> 
	  
>>> def computepay():
	  hrs = input('Ievadiet savas darba stundas.')
	  rate = input('Īevadiet savu stundas likmi.')
	  if hrs > 40:
		  ohp = hrs * rate
	  else
	  
SyntaxError: invalid syntax
>>> def computepay():
	  hrs = input('Ievadiet savas darba stundas.')
	  rate = input('Īevadiet savu stundas likmi.')
	  if hrs > 40:
		  ohp = hrs * rate
	  else:
		  np = hrs * rate

	  
>>> computepay()
	  
Ievadiet savas darba stundas.45
Īevadiet savu stundas likmi.10
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    computepay()
  File "<pyshell#132>", line 4, in computepay
    if hrs > 40:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> def computepay():
	  hrs = input(float('Ievadiet savas darba stundas.'))
	  rate = input(float('Īevadiet savu stundas likmi.'))
	  if hrs > 40:
		  ohp = hrs * rate
	  else:
		  np = hrs * rate

	  
>>> 
	  
>>> 
	  

>>> 
	  

>>> 
	  

>>> 
	  

>>> 
	  
>>> computepay()
	  
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    computepay()
  File "<pyshell#135>", line 2, in computepay
    hrs = input(float('Ievadiet savas darba stundas.'))
ValueError: could not convert string to float: 'Ievadiet savas darba stundas.'
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
	  


>>> 
	  
>>> def computepay():
	  hrs == int(input('Ievadiet savas darba stundas.')
		     rate == int(input('Īevadiet savu stundas likmi.')
				 
SyntaxError: invalid syntax
>>> def computepay():
	  hrs == int(input('Ievadiet savas darba stundas.')
	rate == int(input('Īevadiet savu stundas likmi.')
		    
SyntaxError: invalid syntax
>>> def computepay():
		  hrs = int(input('Ievadiet savas darba stundas.'))
		  rate = int(input('Īevadiet savu stundas likmi.'))
		  if hrs > 40:
			  ohp = hrs * rate
		  else:
			  np = hrs * rate

		    
>>> computepay()
		    
Ievadiet savas darba stundas.45
Īevadiet savu stundas likmi.10
>>> def computepay():
		  hrs = int(input('Ievadiet savas darba stundas.'))
		  rate = int(input('Īevadiet savu stundas likmi.'))
		  if hrs > 40:
			  ohp = hrs * rate
		    return ohp
		  else:
			  np = hrs * rate
		    
SyntaxError: unindent does not match any outer indentation level
>>> def computepay():
		  hrs = int(input('Ievadiet savas darba stundas.'))
		  rate = int(input('Īevadiet savu stundas likmi.'))
		  if hrs > 40:
			  ohp = hrs * rate
		return ohp
		  else:
			  np = hrs * rate
		    
SyntaxError: unindent does not match any outer indentation level
>>> def computepay():
		  hrs = int(input('Ievadiet savas darba stundas.'))
		  rate = int(input('Īevadiet savu stundas likmi.'))
		  if hrs > 40:
			  ohp = hrs * rate
		    return ohp

		  else:
			  np = hrs * rate
		    
SyntaxError: unindent does not match any outer indentation level
>>> def computepay():
		  hrs = int(input('Ievadiet savas darba stundas.'))
		  rate = int(input('Īevadiet savu stundas likmi.'))
		  if hrs > 40:
			  ohp = hrs * rate
		    print(ohp):
		    
SyntaxError: unindent does not match any outer indentation level
>>> def computepay():
		  hrs = int(input('Ievadiet savas darba stundas.'))
		  rate = int(input('Īevadiet savu stundas likmi.'))
		  if hrs > 40:
			  print(ohp = hrs * rate);
		    else:
		    
SyntaxError: unindent does not match any outer indentation level
>>> def computepay():
		  hrs = int(input('Ievadiet savas darba stundas.'))
		  rate = int(input('Īevadiet savu stundas likmi.'))
		  if hrs > 40:
			  print(ohp = hrs * rate);
		else:
		    
SyntaxError: unindent does not match any outer indentation level
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
		    

>>> def computepay():
		    hrs = int(input('Ievadiet savas darba stundas.')
		    rate = int(input('Īevadiet savu stundas likmi.')
			       
SyntaxError: invalid syntax
>>> def computepay():
		    hrs = int(input('Ievadiet savas darba stundas.')
		rate = int(input('Īevadiet savu stundas likmi.')
			   
SyntaxError: invalid syntax
>>> def computepay():
	  hrs = int(input('Ievadiet savas darba stundas.'))
	  rate = int(input('Īevadiet savu stundas likmi.'))
			   if hrs > 40:
			   
SyntaxError: unexpected indent
>>> def computepay():
	  hrs = int(input('Ievadiet savas darba stundas.'))
	  rate = int(input('Īevadiet savu stundas likmi.'))
		if hrs > 40:
			   
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
