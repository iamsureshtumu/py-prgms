Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
print("operations on sets")
operations on sets
>>> a={1,2,3,4}
>>> a.add(5)
>>> a
{1, 2, 3, 4, 5}
>>> a
{1, 2, 3, 4, 5}
>>> a.add(4)
>>> a
{1, 2, 3, 4, 5}
>>> a.add("suresh chowdary")
>>> 
>>> a
{1, 2, 3, 4, 5, 'suresh chowdary'}
>>> a
{1, 2, 3, 4, 5, 'suresh chowdary'}
>>> a.pop()
1
>>> a.pop()
2
>>> >pop()
SyntaxError: invalid syntax
>>> a.pop()
3
>>> a
{4, 5, 'suresh chowdary'}
>>> a.remove(4)
>>> a
{5, 'suresh chowdary'}
>>> a.remove(5)
>>> a
{'suresh chowdary'}
>>> a.remove('suresh chowdary')
>>> a
set()
>>> a=[1,3,4,5,5]
>>> a.clear()
>>> a
[]
>>> a
[]
>>> a=[1,2,3,4,5]
>>> b=[3,6,9,12]
>>> a.union(b)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.union(b)
AttributeError: 'list' object has no attribute 'union'
>>> a.union('b')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.union('b')
AttributeError: 'list' object has no attribute 'union'
>>> import sets
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    import sets
ModuleNotFoundError: No module named 'sets'
>>> import set
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    import set
ModuleNotFoundError: No module named 'set'
>>> import union
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    import union
ModuleNotFoundError: No module named 'union'
>>> a and b
[3, 6, 9, 12]
>>> a or b
[1, 2, 3, 4, 5]
>>> a.union(b)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.union(b)
AttributeError: 'list' object has no attribute 'union'
>>> s={1,2,3}
>>> t={1,2,3,4,5}
>>> s.union(t)
{1, 2, 3, 4, 5}
>>>  a={1,2,3}
SyntaxError: unexpected indent
>>> a={1,2,3}
>>> b={2,3,4}
>>> a.intersection(b)
{2, 3}
>>> a
{1, 2, 3}
>>> b
{2, 3, 4}
>>> a.differecne(b)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.differecne(b)
AttributeError: 'set' object has no attribute 'differecne'
>>> a.difference(b)
{1}
>>> a
{1, 2, 3}
>>> b
{2, 3, 4}
>>> a.isdisjoint()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.isdisjoint()
TypeError: isdisjoint() takes exactly one argument (0 given)
>>> a.isdisjoint(b)
False
>>> b={4,5,6}
>>> a.disjoint()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.disjoint()
AttributeError: 'set' object has no attribute 'disjoint'
>>> a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'
>>> a.isdisjoint(b)
True
>>> a=[1,2,4,5,3,6,7]
>>> a=[1,2,3]
>>> c[1,2,3]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    c[1,2,3]
NameError: name 'c' is not defined
>>> c=[1,2,3]
>>> a.issuperset(b)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.issuperset(b)
AttributeError: 'list' object has no attribute 'issuperset'
>>> a={1,2,3,4,5,6,7}
>>> b={1,2,3,4}
>>> c={1,2,3}
>>> b.issuperset(a)
False
>>> b=issuperset(c)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    b=issuperset(c)
NameError: name 'issuperset' is not defined
>>> b.issuperset(c)
True
>>> c.issuperset(b)
False
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> b=a.copy()
>>> b
{1, 2, 3, 4, 5, 6, 7}
>>> c=copy.deepcopy(a)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    c=copy.deepcopy(a)
NameError: name 'copy' is not defined
>>> import copy
>>> c=copy.deepcopy(a)
>>> c
{1, 2, 3, 4, 5, 6, 7}
>>> print("operations on dictionary")
operations on dictionary
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> a.clear()
>>> a
set()
>>> a=(1,2,3,4,5)
>>> a.clear()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.clear()
AttributeError: 'tuple' object has no attribute 'clear'
>>> a={1,2,3,4,5}
>>> a.clear()
>>> a
set()
>>> a={'a':1,'b':2,'c':3}
>>> a.pop
<built-in method pop of dict object at 0x006DE0C0>
>>> a.pop(a)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.pop(a)
TypeError: unhashable type: 'dict'
>>> import dict
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    import dict
ModuleNotFoundError: No module named 'dict'
>>> import dictionary
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    import dictionary
ModuleNotFoundError: No module named 'dictionary'
>>> a
{'a': 1, 'b': 2, 'c': 3}
>>> a.pop('a')
1
>>> a.pop('a',element not found)
SyntaxError: invalid syntax
>>> a.pop('a',"element not found")
'element not found'
>>> a.pop9('b',)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.pop9('b',)
AttributeError: 'dict' object has no attribute 'pop9'
>>> a.pop('b',"element not found")
2
>>> a.pop('c')
3
>>> a
{}
>>> a=
SyntaxError: invalid syntax
>>> a={'a':1,'b':2,'c':3}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> a.popitem()
('c', 3)
>>> a.popitem()
('b', 2)
>>> a.popitem()
('a', 1)
>>> a.popitem()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.popitem()
KeyError: 'popitem(): dictionary is empty'
>>> a
{}
>>> a{'a':1,'b':2,'c':3,'d':4}
SyntaxError: invalid syntax
>>> a={'a':1,'b':2,'c':3,'d':4,'e':5}
>>> a.get('a')
1
>>> a.get('f')
>>> a
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>> a.get('f','element not found')
'element not found'
>>> a={'a':1,'b':b,'c':3}
>>> a.setdefault('a')
1
>>> a.setdefault('d')
>>> a
{'a': 1, 'b': {1, 2, 3, 4, 5, 6, 7}, 'c': 3, 'd': None}
>>> a
{'a': 1, 'b': {1, 2, 3, 4, 5, 6, 7}, 'c': 3, 'd': None}
>>> a.setdefault('w','hello')
'hello'
>>> a
{'a': 1, 'b': {1, 2, 3, 4, 5, 6, 7}, 'c': 3, 'd': None, 'w': 'hello'}
>>> a
{'a': 1, 'b': {1, 2, 3, 4, 5, 6, 7}, 'c': 3, 'd': None, 'w': 'hello'}
>>> a.items()
dict_items([('a', 1), ('b', {1, 2, 3, 4, 5, 6, 7}), ('c', 3), ('d', None), ('w', 'hello')])
>>> a.keys()
dict_keys(['a', 'b', 'c', 'd', 'w'])
>>> a.value()
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    a.value()
AttributeError: 'dict' object has no attribute 'value'
>>> a.values()
dict_values([1, {1, 2, 3, 4, 5, 6, 7}, 3, None, 'hello'])
>>> 
