Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> (3+2j)*(4+5j)
(2+23j)
>>> (1,2,3)*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> 4*(1,2)
(1, 2, 1, 2, 1, 2, 1, 2)
>>> 'hello'*5
'hellohellohellohellohello'
>>> 3.5*4.5
15.75
>>> 3/4
0.75
>>> 3/3
1.0
>>> 3/2
1.5
>>> 3.5/34
0.10294117647058823
>>> hello/hello
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    hello/hello
NameError: name 'hello' is not defined
>>> 'hello'/'hello'
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    'hello'/'hello'
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> 10//3
3
>>> 9//5
1
>>> 10//2
5
>>> 10/3
3.3333333333333335
>>> 7/3
2.3333333333333335
>>> 7//2
3
>>> 
>>> 
>>> 
>>> (4+2)/(1+3j)
(0.6-1.7999999999999998j)
>>> (4+2j)/(1+3j)
(0.9999999999999999-1j)
>>> 3**5
243
>>> (3+5j)**(2+1j)
(-9.416917078829385-7.651631390829465j)
>>> 6 and 8
8
>>>  0 and7
SyntaxError: unexpected indent
>>> 0 and 7
0
>>> 'hello' and 'hal'
'hal'
>>> 7 and 0.1
0.1
>>> 6 and 6
6
>>> 4 and 7
7
>>> 6 or 8
6
>>> oj or 7
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    oj or 7
NameError: name 'oj' is not defined
>>> oj or 7
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    oj or 7
NameError: name 'oj' is not defined
>>> not 6
False
>>> not 0
True
>>> not ""
True
>>> ~t
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ~t
NameError: name 't' is not defined
>>> ~T
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    ~T
NameError: name 'T' is not defined
>>> 6>4
True
>>> 6>7
False
>>> 5>9
False
>>> %>2
SyntaxError: invalid syntax
>>> 5>2
True
>>> 6>4
True
>>> 9>0
True
>>> 7.5<6
False
>>> 656>5665
False
>>> 3.5<7
True
>>> 7>4.5
True
>>> 6>=6
True
>>> 6>=5
True
>>> 6<=4
False
>>> 5<=6
True
>>> 5<=2
False
>>> 6<=5
False
>>> 6<=3
False
>>> 6<=9
True
>>> 6==6
True
>>> 6==5
False
>>> 3==3
True
>>> 1--1
2
>>> 6==6
True
>>> 0==0
True
>>> 9==9
True
>>> 6!=5
True
>>> 6!=6
False
>>> 71=6
SyntaxError: can't assign to literal
>>> 7!=7
False
>>> 7!=6
True
>>> 6&5
4
>>> 6&6
6
>>> 6&8
0
>>> 5&4
4
>>> 15&7
7
>>> 13&5
5
>>> 8|1
9
>>> 8|6
14
>>> 5|7
7
>>> 5|6
7
>>> 12|15
15
>>> 23|0
23
>>> ~n=-
SyntaxError: invalid syntax
>>> ~n=-(n+1)
SyntaxError: can't assign to operator
>>> ~-15
14
>>> 14^17
31
>>> 8^4
12
>>> 14^7
9
>>> 15^7
8
>>> a
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=10
>>> b=10
>>> c=10
>>> a
10
>>> s
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> c
10
>>> b
10
a
>>> 
>>> a
10
>>> b
10
>>> c
10
>>> a=b
>>> a+=b
>>> a/=b
>>> a=a/b
>>> a
0.2
>>> a=10
>>> b=10
>>> a=a/b
>>> 
>>> a
1.0
>>> 'a' in 'has'
True
>>> 'T' in 'TUMU SURESH'
True
>>> 'C' in 'CHOWDARY'
True
>>> suresh tumu
SyntaxError: invalid syntax
>>> suresh
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    suresh
NameError: name 'suresh' is not defined
>>> a=suresh
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    a=suresh
NameError: name 'suresh' is not defined
>>> a='suresh'
>>> b='tumu'
>>> c='chowdary'
>>> a=a+b+c
>>> a='suresh'
>>> a
'suresh'
>>> a=a+b+c
>>> a
'sureshtumuchowdary'
>>> a='Tumu '
>>> b='Suresh '
>>> c='Chowdary '
>>> a=a+b+c
>>> a
'Tumu Suresh Chowdary '
>>> b=[1,2,3,4,5]
>>> b[3]
4
>>> not (a is b)
True
>>> a is not b
True
>>> c is b
False
>>> c is not b
True
>>> HELLO.lower()
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    HELLO.lower()
NameError: name 'HELLO' is not defined
>>> a='HELLO'
>>> a.lower()
'hello'
>>> 'HELLO'.lower()
'hello'
>>> a.lower()
'hello'
>>> a.islower()
False
>>> a='hello'
>>> a.islower()
True
>>> a='HELLO'
>>> a.islower()
False
>>> a.iscaps()
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    a.iscaps()
AttributeError: 'str' object has no attribute 'iscaps'
>>> a.upper()
'HELLO'
>>> a.isupper
<built-in method isupper of str object at 0x03452A20>
>>> a.isupper()
True
>>> 'AKSHAY'.isupper()
True
>>> 'suresh'.islower(0
		     )
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    'suresh'.islower(0
TypeError: islower() takes no arguments (1 given)
>>> 'suresh'.islower()
		     
True
>>> a='hello how are you'
		     
>>> a.title()
		     
'Hello How Are You'
>>> "12th world world hello".title(0
				   )
		     
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    "12th world world hello".title(0
TypeError: title() takes no arguments (1 given)
>>> 'hai hello aow are you'.title()
				   
'Hai Hello Aow Are You'
>>> a='Hai How Are You'
				   
>>> a.istitle(0

	      0
	      
SyntaxError: invalid syntax
a.istitle(0

	      0
>>> a.istitle()
	  
True
>>> b.istitle()
	  
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    b.istitle()
AttributeError: 'list' object has no attribute 'istitle'
>>> b"Suresh Chowdary"
	  
b'Suresh Chowdary'
>>> b.istitle()
	  
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    b.istitle()
AttributeError: 'list' object has no attribute 'istitle'
>>> b='Suresh Chowdary'
	  
>>> b.istitle()
	  
True
>>> a='hello'
	  
>>> a.capitalize()
	  
'Hello'
>>> 'hello'.capitalize()
	  
'Hello'
>>> a='hello'
	  
>>> a.isalpha()
	  
True
>>> "hello world".isalpha()"
	  
SyntaxError: EOL while scanning string literal
>>> 'hello world'.isalpha()
	  
False
>>> a="sureshtumu"
	  
>>> a.isalpha()
	  
True
>>> a='suresh tumu'
	  
>>> a.isalpha()
	  
False
>>> a='123'
	  
>>> a.isdigit(0
	      0
	      
SyntaxError: invalid syntax
>>> a.isdigit()
	      
True
>>> '123'.isdigit()
	      
True
>>> "hello world".startswith("he")
	      
True
>>> a='hello world'
	      
>>> a.startswith()
	      
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    a.startswith()
TypeError: startswith() takes at least 1 argument (0 given)
>>> a.startswith('w,6,11')
	      
False
>>> a.startswith(w,6,11)
	      
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    a.startswith(w,6,11)
NameError: name 'w' is not defined
>>> 'hello world'.startswith('w,6,11')
	      
False
>>> 'hello world'.startswith('w',6,11)
	      
True
>>> 'hello world'.endswith('hello',0,5)
	      
True
>>> 'hello world'.endswith("d")
	      
True
>>> 'hello world'.replace('l','L')
	      
'heLLo worLd'
>>> "hello world".replace('h','H')
	      
'Hello world'
>>> 'hello world'.replace('o','O')
	      
'hellO wOrld'
>>> a='hello world'
	      
>>> a[6]
	      
'w'
>>> a[6].replace("l"," ")
	      
'w'
>>> a
	      
'hello world'
>>> a[6,11]
	      
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    a[6,11]
TypeError: string indices must be integers
>>> a[6,10]
	      
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    a[6,10]
TypeError: string indices must be integers
>>> a[6.]
	      
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    a[6.]
TypeError: string indices must be integers
>>> a[6]
	      
'w'
>>> a[6:11]
	      
'world'
>>> a[6:11].replace("l"," ")
	      
'wor d'
>>> count()
	      
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    count()
NameError: name 'count' is not defined
>>> 'hello how are you dude and im missing you so much'.count('l')
	      
2
>>> a='hai how are you and im waiting for your return and i was eagerly waiting for tha'
	      
>>> a.count('a')
	      
9
>>> b="humans are better than roborts"
	      
>>> b.index()
	      
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    b.index()
TypeError: index() takes at least 1 argument (0 given)
>>> b.index
	      
<built-in method index of str object at 0x03463F00>
>>> b.index('t')
	      
13
>>> b="dogs are better than humans"
	      
>>> b.index('s')
	      
3
>>> 'hello world'.index('l')
	      
2
>>> b.index('t')
	      
11
>>> b="suresh chowdary"
	      
>>> b.index('s')
	      
0
>>> b.index('y')
	      
14
>>> b.index('l',6)
	      
Traceback (most recent call last):
  File "<pyshell#222>", line 1, in <module>
    b.index('l',6)
ValueError: substring not found
>>> a="hello world"
	      
>>> a.index('l',6,11)
	      
9
>>> a.index('l',6)
	      
9
>>> b
	      
'suresh chowdary'
>>> b='are you a human being or not'
	      
>>> b.split('')
	      
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    b.split('')
ValueError: empty separator
>>> b.split('1')
	      
['are you a human being or not']
>>> b.split(' ',2)
	      
['are', 'you', 'a human being or not']
>>> a=('hi hello how are you and what is your name and how you doing')
	      
>>> a.split(' ',3)
	      
['hi', 'hello', 'how', 'are you and what is your name and how you doing']
>>> a.split('3')
	      
['hi hello how are you and what is your name and how you doing']
>>> a.split('4')
	      
['hi hello how are you and what is your name and how you doing']
>>> a.split(''4)
	      
SyntaxError: invalid syntax
>>> a.split(' ',4)
	      
['hi', 'hello', 'how', 'are', 'you and what is your name and how you doing']
>>> a
	      
'hi hello how are you and what is your name and how you doing'
>>> a
	      
'hi hello how are you and what is your name and how you doing'
>>> a.join(a)
	      
'hhi hello how are you and what is your name and how you doingihi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doinghhi hello how are you and what is your name and how you doingehi hello how are you and what is your name and how you doinglhi hello how are you and what is your name and how you doinglhi hello how are you and what is your name and how you doingohi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doinghhi hello how are you and what is your name and how you doingohi hello how are you and what is your name and how you doingwhi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doingahi hello how are you and what is your name and how you doingrhi hello how are you and what is your name and how you doingehi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doingyhi hello how are you and what is your name and how you doingohi hello how are you and what is your name and how you doinguhi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doingahi hello how are you and what is your name and how you doingnhi hello how are you and what is your name and how you doingdhi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doingwhi hello how are you and what is your name and how you doinghhi hello how are you and what is your name and how you doingahi hello how are you and what is your name and how you doingthi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doingihi hello how are you and what is your name and how you doingshi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doingyhi hello how are you and what is your name and how you doingohi hello how are you and what is your name and how you doinguhi hello how are you and what is your name and how you doingrhi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doingnhi hello how are you and what is your name and how you doingahi hello how are you and what is your name and how you doingmhi hello how are you and what is your name and how you doingehi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doingahi hello how are you and what is your name and how you doingnhi hello how are you and what is your name and how you doingdhi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doinghhi hello how are you and what is your name and how you doingohi hello how are you and what is your name and how you doingwhi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doingyhi hello how are you and what is your name and how you doingohi hello how are you and what is your name and how you doinguhi hello how are you and what is your name and how you doing hi hello how are you and what is your name and how you doingdhi hello how are you and what is your name and how you doingohi hello how are you and what is your name and how you doingihi hello how are you and what is your name and how you doingnhi hello how are you and what is your name and how you doingg'
>>> 'hello'.join(a)
	      
'hhelloihello hellohhelloehellolhellolhelloohello hellohhelloohellowhello helloahellorhelloehello helloyhelloohellouhello helloahellonhellodhello hellowhellohhelloahellothello helloihelloshello helloyhelloohellouhellorhello hellonhelloahellomhelloehello helloahellonhellodhello hellohhelloohellowhello helloyhelloohellouhello hellodhelloohelloihellonhellog'
>>> "121".join(a)
	      
'h121i121 121h121e121l121l121o121 121h121o121w121 121a121r121e121 121y121o121u121 121a121n121d121 121w121h121a121t121 121i121s121 121y121o121u121r121 121n121a121m121e121 121a121n121d121 121h121o121w121 121y121o121u121 121d121o121i121n121g'
>>> a
	      
'hi hello how are you and what is your name and how you doing'
>>> " ".join()
	      
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    " ".join()
TypeError: join() takes exactly one argument (0 given)
>>> " ".join(a)
	      
'h i   h e l l o   h o w   a r e   y o u   a n d   w h a t   i s   y o u r   n a m e   a n d   h o w   y o u   d o i n g'
>>> "121".join(a)
	      
'h121i121 121h121e121l121l121o121 121h121o121w121 121a121r121e121 121y121o121u121 121a121n121d121 121w121h121a121t121 121i121s121 121y121o121u121r121 121n121a121m121e121 121a121n121d121 121h121o121w121 121y121o121u121 121d121o121i121n121g'
>>> a="my name is {} and my age is{}".format("suresh","23")
	      
>>> a.format("suresh","23")
	      
'my name is suresh and my age is23'
>>> a
	      
'my name is suresh and my age is23'
>>> b="hai how are you"
	      
>>> a=a+b
	      
>>> a.format("suresh","23")
	      
'my name is suresh and my age is23hai how are you'
>>> a
	      
'my name is suresh and my age is23hai how are you'
>>> a="hai {} how are you and your age is {}"
	      
>>> b="welcome to tumu's land"
	      
>>> a=a+b
	      
>>> a.format("venky","23")
	      
"hai venky how are you and your age is 23welcome to tumu's land"
>>> a="hai suresh how are"
	      
>>> a.append("you")
	      
Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    a.append("you")
AttributeError: 'str' object has no attribute 'append'
>>> a=('hai how are')
	      
>>> a.append('you')
	      
Traceback (most recent call last):
  File "<pyshell#260>", line 1, in <module>
    a.append('you')
AttributeError: 'str' object has no attribute 'append'
>>> a.append(you)
	      
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    a.append(you)
AttributeError: 'str' object has no attribute 'append'
>>> a=[1,2,3,4]
	      
>>> a[4]=5
	      
Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    a[4]=5
IndexError: list assignment index out of range
>>> a.append(5)
	      
>>> a
	      
[1, 2, 3, 4, 5]
>>> a.append("hello")
	      
>>> a
	      
[1, 2, 3, 4, 5, 'hello']
>>> a=("hello how are")
	      
>>> a.append("you")
	      
Traceback (most recent call last):
  File "<pyshell#269>", line 1, in <module>
    a.append("you")
AttributeError: 'str' object has no attribute 'append'
>>> a=['hai']
	      
>>> a
	      
['hai']
>>> a(1,2,3,4)
	      
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    a(1,2,3,4)
TypeError: 'list' object is not callable
>>> a=
	      
SyntaxError: invalid syntax
>>> 
	      
>>> a="hello world"
	      
>>> a
	      
'hello world'
>>> a.append(a)
	      
Traceback (most recent call last):
  File "<pyshell#277>", line 1, in <module>
    a.append(a)
AttributeError: 'str' object has no attribute 'append'
>>> a=[1,24,4,5,,5]
	      
SyntaxError: invalid syntax
>>> a=[21,4,5,4,3,4]
	      
>>> a.append('hai hello how are you')
	      
>>> a
	      
[21, 4, 5, 4, 3, 4, 'hai hello how are you']
>>> a.extend("hai")
	      
>>> a
	      
[21, 4, 5, 4, 3, 4, 'hai hello how are you', 'h', 'a', 'i']
>>> a.extend([7,8,9])
	      
>>> a
	      
[21, 4, 5, 4, 3, 4, 'hai hello how are you', 'h', 'a', 'i', 7, 8, 9]
>>> a.extend({'a':1,'b':2,'c':3})
	      
>>> a
	      
[21, 4, 5, 4, 3, 4, 'hai hello how are you', 'h', 'a', 'i', 7, 8, 9, 'a', 'b', 'c']
>>> a
	      
[21, 4, 5, 4, 3, 4, 'hai hello how are you', 'h', 'a', 'i', 7, 8, 9, 'a', 'b', 'c']
>>> operations on list
	      
SyntaxError: invalid syntax
>>> print("operations on list")
	      
operations on list
>>> print('insert()')
	      
insert()
>>> a
	      
[21, 4, 5, 4, 3, 4, 'hai hello how are you', 'h', 'a', 'i', 7, 8, 9, 'a', 'b', 'c']
>>> a=[1,2,3,4]
	      
>>> a.index(1,5)
	      
Traceback (most recent call last):
  File "<pyshell#294>", line 1, in <module>
    a.index(1,5)
ValueError: 1 is not in list
>>> a.insert(1,5)
	      
>>> a
	      
[1, 5, 2, 3, 4]
>>> a.insert(3,"hai")
	      
>>> a
	      
[1, 5, 2, 'hai', 3, 4]
>>> a.insert(4,4)
	      
>>> a
	      
[1, 5, 2, 'hai', 4, 3, 4]
>>> a
	      
[1, 5, 2, 'hai', 4, 3, 4]
>>> a.pop()
	      
4
>>> a
	      
[1, 5, 2, 'hai', 4, 3]
>>> a.pop()
	      
3
>>> a.pop()
	      
4
>>> a
	      
[1, 5, 2, 'hai']
>>> a.pop()
	      
'hai'
>>> a
	      
[1, 5, 2]
>>> a.pop()
	      
2
>>> a
	      
[1, 5]
>>> a=[1,2,3,4,5,6,7,8,9]
	      
>>> a
	      
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.remove()
	      
Traceback (most recent call last):
  File "<pyshell#314>", line 1, in <module>
    a.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> a.remove(9)
	      
>>> a
	      
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a.remove(4)
	      
>>> a
	      
[1, 2, 3, 5, 6, 7, 8]
>>> a.add(4,5)
	      
Traceback (most recent call last):
  File "<pyshell#319>", line 1, in <module>
    a.add(4,5)
AttributeError: 'list' object has no attribute 'add'
>>> a,push(6)
	      
Traceback (most recent call last):
  File "<pyshell#320>", line 1, in <module>
    a,push(6)
NameError: name 'push' is not defined
>>> a.push(8)
	      
Traceback (most recent call last):
  File "<pyshell#321>", line 1, in <module>
    a.push(8)
AttributeError: 'list' object has no attribute 'push'
>>> a
	      
[1, 2, 3, 5, 6, 7, 8]
>>> a.clear()
	      
>>> a
	      
[]
>>> a=[1,2,3,4,5,6,7,7,6]
	      
>>> a
	      
[1, 2, 3, 4, 5, 6, 7, 7, 6]
>>> a.clesr()
	      
Traceback (most recent call last):
  File "<pyshell#327>", line 1, in <module>
    a.clesr()
AttributeError: 'list' object has no attribute 'clesr'
>>> a.clesr()
	      
Traceback (most recent call last):
  File "<pyshell#328>", line 1, in <module>
    a.clesr()
AttributeError: 'list' object has no attribute 'clesr'
>>> a.clear()
	      
>>> a
	      
[]
>>>  a
	      
SyntaxError: unexpected indent
>>> a
	      
[]
>>> a[1,2,3,4,5]
	      
Traceback (most recent call last):
  File "<pyshell#333>", line 1, in <module>
    a[1,2,3,4,5]
TypeError: list indices must be integers or slices, not tuple
>>> a=[1,2,3,4]
	      
>>> a.reverse()
	      
>>> a
	      
[4, 3, 2, 1]
>>> a[::-1]
	      
[1, 2, 3, 4]
>>> a[::-1]
	      
[1, 2, 3, 4]
>>> a
	      
[4, 3, 2, 1]
>>> a.reverse()
	      
>>> a
	      
[1, 2, 3, 4]
>>> a.sort()
	      
>>> a
	      
[1, 2, 3, 4]
>>> a.sort(rreverse=True)
	      
Traceback (most recent call last):
  File "<pyshell#345>", line 1, in <module>
    a.sort(rreverse=True)
TypeError: 'rreverse' is an invalid keyword argument for sort()
>>> a.sort(reverse=True)
	      
>>> a
	      
[4, 3, 2, 1]
>>> a=[1,3,4,5,2,8,9,6]
	      
>>> a
	      
[1, 3, 4, 5, 2, 8, 9, 6]
>>> a.sort()
	      
>>> a
	      
[1, 2, 3, 4, 5, 6, 8, 9]
>>> a.sort(reverse=atarue)
	      
Traceback (most recent call last):
  File "<pyshell#352>", line 1, in <module>
    a.sort(reverse=atarue)
NameError: name 'atarue' is not defined
>>> a.sort(reverse.True)
	      
SyntaxError: invalid syntax
>>> a.sort(reverse=True)
	      
>>> a
	      
[9, 8, 6, 5, 4, 3, 2, 1]
>>> print('count')
	      
count
>>> a
	      
[9, 8, 6, 5, 4, 3, 2, 1]
>>> a=sort()
	      
Traceback (most recent call last):
  File "<pyshell#358>", line 1, in <module>
    a=sort()
NameError: name 'sort' is not defined
>>> a.sort()
	      
>>> a
	      
[1, 2, 3, 4, 5, 6, 8, 9]
>>> a=[1,2,3,4,5,35,7,3,23,67,9,3,5,7,8,9]
	      
>>> a
	      
[1, 2, 3, 4, 5, 35, 7, 3, 23, 67, 9, 3, 5, 7, 8, 9]
>>> a.count(2)
	      
1
>>> a.count(3)
	      
3
>>> a
	      
[1, 2, 3, 4, 5, 35, 7, 3, 23, 67, 9, 3, 5, 7, 8, 9]
>>> a.index(2)
	      
1
>>> a.index(2,2)
	      
Traceback (most recent call last):
  File "<pyshell#367>", line 1, in <module>
    a.index(2,2)
ValueError: 2 is not in list
>>> a.index(7)
	      
6
>>> a.index(9)
	      
10
>>> a.index(2,3)
	      
Traceback (most recent call last):
  File "<pyshell#370>", line 1, in <module>
    a.index(2,3)
ValueError: 2 is not in list
>>> a.index(4)
	      
3
>>> a.index(2,3,len(a))
	      
Traceback (most recent call last):
  File "<pyshell#372>", line 1, in <module>
    a.index(2,3,len(a))
ValueError: 2 is not in list
>>> a.index(2,3,len(a))
	      
Traceback (most recent call last):
  File "<pyshell#373>", line 1, in <module>
    a.index(2,3,len(a))
ValueError: 2 is not in list
>>> a.index(2,3)
	      
Traceback (most recent call last):
  File "<pyshell#374>", line 1, in <module>
    a.index(2,3)
ValueError: 2 is not in list
>>> a
	      
[1, 2, 3, 4, 5, 35, 7, 3, 23, 67, 9, 3, 5, 7, 8, 9]
>>> a.index(2,3)
	      
Traceback (most recent call last):
  File "<pyshell#376>", line 1, in <module>
    a.index(2,3)
ValueError: 2 is not in list
>>> a.index(5)
	      
4
>>> a.index(6)
	      
Traceback (most recent call last):
  File "<pyshell#378>", line 1, in <module>
    a.index(6)
ValueError: 6 is not in list
>>> a.len(a)
	      
Traceback (most recent call last):
  File "<pyshell#379>", line 1, in <module>
    a.len(a)
AttributeError: 'list' object has no attribute 'len'
>>> a
	      
[1, 2, 3, 4, 5, 35, 7, 3, 23, 67, 9, 3, 5, 7, 8, 9]
>>> a.index(2,3)
	      
Traceback (most recent call last):
  File "<pyshell#381>", line 1, in <module>
    a.index(2,3)
ValueError: 2 is not in list
>>> a=[1,2,3,4,5,6]
	      
>>> a.index('3',1,5)
	      
Traceback (most recent call last):
  File "<pyshell#383>", line 1, in <module>
    a.index('3',1,5)
ValueError: '3' is not in list
>>> a.index(6)
	      
5
>>> a.index(q,6,len(a))
	      
Traceback (most recent call last):
  File "<pyshell#385>", line 1, in <module>
    a.index(q,6,len(a))
NameError: name 'q' is not defined
>>> a.index(1,6,len(a))
	      
Traceback (most recent call last):
  File "<pyshell#386>", line 1, in <module>
    a.index(1,6,len(a))
ValueError: 1 is not in list
>>> a=["dog", "cat", "bat", "mat", "dog"]
	      
>>> a.index("dog")
	      
0
>>> a.index("dog",1,4)
	      
Traceback (most recent call last):
  File "<pyshell#389>", line 1, in <module>
    a.index("dog",1,4)
ValueError: 'dog' is not in list
>>> a.index("dog", 1, 5)
	      
4
>>> a=[1,2,3,4,5,6,7,8,9,3,2,1]
	      
>>> a.index(3,3,7)
	      
Traceback (most recent call last):
  File "<pyshell#392>", line 1, in <module>
    a.index(3,3,7)
ValueError: 3 is not in list
>>> a.index("3",1,3)
	      
Traceback (most recent call last):
  File "<pyshell#393>", line 1, in <module>
    a.index("3",1,3)
ValueError: '3' is not in list
>>> a
	      
[1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 1]
>>> b.copy(a)
	      
Traceback (most recent call last):
  File "<pyshell#395>", line 1, in <module>
    b.copy(a)
AttributeError: 'str' object has no attribute 'copy'
>>> b.copy('a')
	      
Traceback (most recent call last):
  File "<pyshell#396>", line 1, in <module>
    b.copy('a')
AttributeError: 'str' object has no attribute 'copy'
>>> a.copy("a")
	      
Traceback (most recent call last):
  File "<pyshell#397>", line 1, in <module>
    a.copy("a")
TypeError: copy() takes no arguments (1 given)
>>> b.copy("a")
	      
Traceback (most recent call last):
  File "<pyshell#398>", line 1, in <module>
    b.copy("a")
AttributeError: 'str' object has no attribute 'copy'
>>> a
	      
[1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 1]
>>> b=a.copy()
	      
>>> b
	      
[1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 1]
>>> a=[1,2,3,4]
	      
>>> b
	      
[1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 1]
>>> a=b
	      
>>> a
	      
[1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 1]
>>> b[1,2,3,4]
	      
Traceback (most recent call last):
  File "<pyshell#406>", line 1, in <module>
    b[1,2,3,4]
TypeError: list indices must be integers or slices, not tuple
>>> b=[1,2,3,4,5]
	      
>>> a
	      
[1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 1]
>>> a
	      
[1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 1]
>>> a=[1,2,3,4,5]
	      
>>> b=a
	      
>>> b
	      
[1, 2, 3, 4, 5]
>>> b=copy.(a)
	      
SyntaxError: invalid syntax
>>> b=b.copy(a)
	      
Traceback (most recent call last):
  File "<pyshell#414>", line 1, in <module>
    b=b.copy(a)
TypeError: copy() takes no arguments (1 given)
>>> a
	      
[1, 2, 3, 4, 5]
>>> b
	      
[1, 2, 3, 4, 5]
>>> b=[1,3,5,7,9]
	      
>>> c=copy.deepcopy(a)
	      
Traceback (most recent call last):
  File "<pyshell#418>", line 1, in <module>
    c=copy.deepcopy(a)
NameError: name 'copy' is not defined
>>> c=copy.deepcopy("a")
	      
Traceback (most recent call last):
  File "<pyshell#419>", line 1, in <module>
    c=copy.deepcopy("a")
NameError: name 'copy' is not defined
>>> copy.deepcopy(a)
	      
Traceback (most recent call last):
  File "<pyshell#420>", line 1, in <module>
    copy.deepcopy(a)
NameError: name 'copy' is not defined
>>> a
	      
[1, 2, 3, 4, 5]
>>> b=copy.deepcopy
	      
Traceback (most recent call last):
  File "<pyshell#422>", line 1, in <module>
    b=copy.deepcopy
NameError: name 'copy' is not defined
>>> b=copy.deepcopy(a)
	      
Traceback (most recent call last):
  File "<pyshell#423>", line 1, in <module>
    b=copy.deepcopy(a)
NameError: name 'copy' is not defined
>>> list1 = [1,2,3,4]
	      
>>> list2 = copy.deepcopy(list1)
	      
Traceback (most recent call last):
  File "<pyshell#425>", line 1, in <module>
    list2 = copy.deepcopy(list1)
NameError: name 'copy' is not defined
>>> import copy
	      
>>> list1=[1,2,3,4]
	      
>>> list2=copy.deepcopy(list1)
	      
>>> list2
	      
[1, 2, 3, 4]
>>> list2=list1.copy()
	      
>>> list2
	      
[1, 2, 3, 4]
>>> a=["hello","how","are","you"]
	      
>>> import copy
	      
>>> c=copy.deepcopy(a)
	      
>>> c
	      
['hello', 'how', 'are', 'you']
>>> b=a.copy()
	      
>>> a
	      
['hello', 'how', 'are', 'you']
>>> b
	      
['hello', 'how', 'are', 'you']
>>> c
	      
['hello', 'how', 'are', 'you']
>>> a=['a':1,'b':2,'c':3]
	      
SyntaxError: invalid syntax
>>> a=['a':'1']
	      
SyntaxError: invalid syntax
>>> a=[1,2,[3,4],"hai"]
	      
>>> import copy
	      
>>> b=copy.deepcopy()
	      
Traceback (most recent call last):
  File "<pyshell#444>", line 1, in <module>
    b=copy.deepcopy()
TypeError: deepcopy() missing 1 required positional argument: 'x'
>>> b.copy.deepcopy(a)
	      
Traceback (most recent call last):
  File "<pyshell#445>", line 1, in <module>
    b.copy.deepcopy(a)
AttributeError: 'builtin_function_or_method' object has no attribute 'deepcopy'
>>> import copy
	      
>>> b=copy.deepcopy(a)
	      
>>> b
	      
[1, 2, [3, 4], 'hai']
>>> a=[a:1, b:2]
	      
SyntaxError: invalid syntax
>>> a{'a':1,'b':2}
	      
SyntaxError: invalid syntax
>>> a={'a':1, 'b':2, 'c':3}
	      
>>> import copy
	      
>>> b=copy.deepcopy(a)
	      
>>> b
	      
{'a': 1, 'b': 2, 'c': 3}
>>> b=a.copy()
	      
>>> b
	      
{'a': 1, 'b': 2, 'c': 3}
>>> a
	      
{'a': 1, 'b': 2, 'c': 3}
>>> b=a.copy()
	      
>>> b
	      
{'a': 1, 'b': 2, 'c': 3}
>>> 
              a
	      
SyntaxError: unexpected indent
>>> a
	      
{'a': 1, 'b': 2, 'c': 3}
>>> a=(10,20,30,40)
	      
>>> a
	      
(10, 20, 30, 40)
>>> a.index(10)
	      
0
>>> a.index(40)
	      
3
>>> len(a)
	      
4
>>> 
