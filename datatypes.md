# OBJECT TPYPES /DATATYPE

-Number : 1234,3.14,3+4j(complex number),0b111,Decimal(),Fraction()
-String : 'Spam',"Bob's",b'a\xolc',u'sp'xc4m'
-List : [1,[2,'three'],4,5],list(range(10)) 
(Its count /starts from 0,List inside List)
-Tuple : (1,'spam',4,'U'),tuple('spam'),namedtuple
-Dictonary : {'food':"spam" ,'taste' :'yam'},dict(hours = 10)
(Its not start from 0 )['key':'value']
-Set: Set('a,b,c'),{'a','b','c'} [must be unique]
-File : open('eggs.txt'),open(r'C:\ham.bin','wb')
Its use for working in excel or data extract through pdf 
-Boolean : True,False
-None : None
-Function ,modules,classes
-Advanced Decorators,Generators,Iterators,MetaProgramming


# For More detail about any import packages then use '
dir(packagename)
like dir(math)


# copy.copy() and copy.deepcopy()
1. copy.copy()

import copy
Creates a new list, but the nested objects (like lists inside lists) are still references to the original objects.
Changes in nested objects affect both the original and copied list.

h3 = [1, 2, 3, ['a', 'b'], 4]
h2 = copy.copy(h3)  # Shallow copy

h2[3][0] = 'z'  # Modifying nested list inside h2

print(h3)  # [1, 2, 3, ['z', 'b'], 4]  <- Original list also changed!
print(h2)  # [1, 2, 3, ['z', 'b'], 4]

in this we can change the copy variable it can affect the orginal variable you can change both the variable and it will affect copys vaiable also

2. copy.deepcopy()

Creates a completely independent copy, including nested objects.
Changes in the copied list do not affect the original.

h3 = [1, 2, 3, ['a', 'b'], 4]
h2 = copy.deepcopy(h3)  # Deep copy

h2[3][0] = 'z'  # Modifying nested list inside h2

print(h3)  # [1, 2, 3, ['a', 'b'], 4]  <- Original list remains unchanged!
print(h2)  # [1, 2, 3, ['z', 'b'], 4]


in this only change or affect those you want to change another copy variable is not affect 

# for clear power shell use 
ctrl + L

# NOTE
 1. m == n => it is use and its check the value of both variable
 2. m is n => it is check value and memory refrence same is or not /object same in memory


# NUMBER 

 For solve decimal problem
  like this problem
  >>> 0.1 + 0.1 +0.1

0.30000000000000004
>>> 0.1 + 0.1 +0.1 -0.3

5.551115123125783e-17

>>> from decimal import Decimal  //import this 

>>> Decimal('0.1')+ Decimal('0.1') + Decimal('0.1')

Decimal('0.3')

>>> Decimal('0.1')+ Decimal('0.1') + Decimal('0.1') - Decimal('0.3')

Decimal('0.0')

>>> from fractions import Fraction // for fraction

>>> myFra = Fraction(2,7)

>>> myFra
Fraction(2, 7)

:= if you want to show multiple variables result with all then show in TUPLE synatx [()] like this

>>> x,y,z

(2, 3, 4)

# math.floor() and math.trunc()

1. math.floor() => its show the bottoom value
>>> math.floor(3.5)
3

>>> math.floor(-3.8)
-4

2.  math.trunc() => it goes to the 0
>>> math.trunc(2.3)
2

>>> math.trunc(-3.9)
-3

=> Complex Number in python
>>> (2 + 1j)*3
(6+3j)

>>> 2+1j * 3
(2+3j)

# OCTA ,HEXA , BINARY
1.OCTA => 0o [0-7]
>>> 0o20
16

>>> 0o13
11

 another method

 >>> oct(64)
'0o100'
>>> oct(49)
'0o61'

2.HEXA => 0x
>>> 0xff
255
>>> 0xab
171
>>> 0x3f
63

another method

>>> hex(64)
'0x40'
>>> hex(40)
'0x28'

3.BINARY => 0b
>>> 0b1000
8
>>> 0b1010
10

another method
>>> bin(64)
'0b1000000'
>>> bin(45)
'0b101101'

# Integer to OCTA,HEXA ,BINARY
OCTA
>>> int('64',8)
52

>>> int('24',8)
20

HEXA
>>> int('24',16)
36

>>> int('56',16)
86

BINARY
>>> int('10000',2)
16

>>> int('10001',2)
17


# SET ({}) DATATYPE

>>> setone = {1,2,3,4}
>>> settwo = {3,4,5}

1. using Intersection use (&)

>>> setone & settwo
{3, 4}

2. using Union use (|) or
>>> setone | settwo
{1, 2, 3, 4, 5}

3. using differnce use (-)
>>> setone - settwo
{1, 2}

# Boolean Type 
True or False in python treat like 1 or 0

>>> True == 1
True

>>> False == 0
True
 
 Like Maths 

>>> True + 3

4

>>> False + 4

4

But it is different under the memory True has own object/refrence 1 has another object /refrence in memory same has false also
>>> True is 1

<python-input-188>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
  True is 1

False


