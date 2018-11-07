Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> stuff = 'Hello\nWorld'
>>> stuff
'Hello\nWorld'
>>> print(stuff)
Hello
World
>>> stuff = 'X\nWorld'
>>> print(stuff)
X
World
>>> len(stuff)
7
>>> 
>>> 
>>> xfile = open('mbox.txt')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    xfile = open('mbox.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox.txt'
>>> fhand = open('mbox.txt')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fhand = open('mbox.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox.txt'
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


>>> fhand = open('mbox.txt','w')
>>> fhand = open('mbox.txt')
>>> print(fhand)
<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>
>>> 
>>> xfile = open('mbox.txt')
>>> for cheese in xfile:
	print(cheese)

	
>>> nano mbox-short.txt
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

>>> fhand = open('ņbox.txt')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    fhand = open('ņbox.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'ņbox.txt'
>>> fhand = open(mbox.txt','w')
		 
SyntaxError: invalid syntax
>>> fhand = open('mbox.txt','w')
		 
>>> fhand = open('mbox.txt')
		 
>>> print(fhand)
		 
<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>
>>> 
		 
>>> xfile = open('mbox.txt')
		 
>>> for cheese in xfile:
		 print(cheese)

		 
>>> fhand = open('mbox.txt')
		 
>>> for cheese in xfile:
		 print(cheese)
		 9

		 
>>> fhand = open('mbox.txt')
		 
>>> 
		 
>>> 
		 
>>> 
		 


>>> 
		 

>>> fhand = open('mbox.txt')
		 
>>> fhand = open('mbox-short.txt')
		 
>>> print(fhand)
		 
<_io.TextIOWrapper name='mbox-short.txt' mode='r' encoding='UTF-8'>
>>> 
		 
>>> 
		 
>>> 
		 
>>> fhand = open('mbox.txt')
		 
>>> count = 0
		 
>>> fot line in fhand:
		 
SyntaxError: invalid syntax
>>> fhand = open('mbox.txt')
		 
>>> count = 0
		 
>>> for line in fhand:
		 count = count + 1

		 
>>> print('Line Count:',count)
		 
Line Count: 1
>>> 
		 
>>> 
		 
>>> fhand = open('mbox-short.txt')
		 
>>> inp = fhand.read()
		 
>>> print(len(inp))
		 
94654
>>> print(inp[:20])
		 

py4inf.com
86-109 m
>>> 
		 
>>> fhand = open('mbox-short.txt')
		 
>>> for line in fhand:
		 if line.startswith('From:'):
		 print(line)
		 
SyntaxError: expected an indented block
>>> fhand = open('mbox-short.txt')
		 
>>> for line in fhand:
		 if line.startswith('From:'):
		     print(line)

		 
From: stephen.marquard@uct.ac.za

From: louis@media.berkeley.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: gsilver@umich.edu

From: gsilver@umich.edu

From: zqian@umich.edu

From: gsilver@umich.edu

From: wagnermr@iupui.edu

From: zqian@umich.edu

From: antranig@caret.cam.ac.uk

From: gopal.ramasammycook@gmail.com

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: stephen.marquard@uct.ac.za

From: louis@media.berkeley.edu

From: louis@media.berkeley.edu

From: ray@media.berkeley.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

>>> fhand = open('mbox-short.txt')
		 
>>> for line in fhand:
		 line = line.rstrip()
		 if line.startswith('From:'):
		     print(line)

		 
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: gsilver@umich.edu
From: gsilver@umich.edu
From: zqian@umich.edu
From: gsilver@umich.edu
From: wagnermr@iupui.edu
From: zqian@umich.edu
From: antranig@caret.cam.ac.uk
From: gopal.ramasammycook@gmail.com
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: louis@media.berkeley.edu
From: ray@media.berkeley.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
>>> 
		 
>>> fhand = open('mbox-short.txt')for line in fhand:
		 line = line.rstrip()
		 
SyntaxError: invalid syntax
>>> fhand = open('mbox-short.txt')
		 for line in fhand:
		 
SyntaxError: multiple statements found while compiling a single statement
>>> fhand = open('mbox-short.txt')
		 
>>> for line in fhand:
		 line = line.rstrip()
		 if not line.startswith('From:'):
		     continue

		 
>>> print(line)
		 

>>> fhand = open('mbox-short.txt')
		 
>>> for line in fhand:
		 line = line.rstrip()
		 if not '@uct.ac.za'in line:
		     continue

		 
>>> print(line)
		 

>>> for line in fhand:
		 line = line.rstrip()
		 if not '@uct.ac.za'in line:
		     continue
		 print(line)

		 
>>> 
		 
>>> print(line)
		 

>>> fhand = open('mbox-short.txt')
		 
>>> for line in fhand:
		 line = line.rstrip()
		 if not '@uct.ac.za'in line:
		     continue
		 print(line)

		 
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
From david.horwitz@uct.ac.za Fri Jan  4 07:02:32 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
r39753 | david.horwitz@uct.ac.za | 2008-01-04 13:05:51 +0200 (Fri, 04 Jan 2008) | 1 line
From david.horwitz@uct.ac.za Fri Jan  4 06:08:27 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Jan  4 04:49:08 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Jan  4 04:33:44 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
>>> 
		 
>>> 
		 
>>> fname = input('Enter the file name: ')
		 
Enter the file name: mbox.txt
>>> 
		 
>>> fname = input('Enter the file name: ')
		 
Enter the file name: mbox.txt
>>> fhand = open(fname)
		 
>>> count = 0
		 
>>> for line in fhand:
		 if line.startswith('Subject:'):
		     count = count + 1

		 
>>> print('There were' count, 'šubject lines in', fname)
		 
SyntaxError: invalid syntax
>>> fname = input('Enter the file name: ')
		 
Enter the file name: mbox.txt
>>> fhand = open(fname)
		 
>>> count = 0
		 
>>> for line in fhand:
		 if line.startswith('Subject:'):
		     count = count + 1
		 print('There were' count, 'šubject lines in', fname)
		 
SyntaxError: invalid syntax
>>> for line in fhand:
		 if line.startswith('Subject:'):
		     count = count + 1
		 print('There were'count, 'šubject lines in', fname)
		 
SyntaxError: invalid syntax
>>> for line in fhand:
		 if line.startswith('Subject:'):
		     count = count + 1
		 print('There were', count, 'šubject lines in', fname)

		 
There were 0 šubject lines in mbox.txt
>>> 
		 
>>> 
		 
>>> 
		 
>>> fname = input('Enter the file name: ')
		 
Enter the file name: mbox.txt
>>> try:
		 fhand = open(fname)
		 except:
		 
SyntaxError: invalid syntax
>>> fname = input('Enter the file name: ')
		 
Enter the file name: mbox.txt
>>> try:
		 fhand = open(fname)
	except:
		 
SyntaxError: unindent does not match any outer indentation level
>>> fname = input('Enter the file name: ')
		 
Enter the file name: 
		 mbox.txt
>>> try:
		 fhand = open(fname)
except:
		 print('File cannot be opened:', fname)
		 quit()

		 
File cannot be opened: 
>>> 
