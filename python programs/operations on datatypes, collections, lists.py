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
>>> 
