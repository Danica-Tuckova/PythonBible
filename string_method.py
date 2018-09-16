Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> "hello".count("e")
1
>>> text = "happy birthday"
>>> text.count("a")
2
>>> text.count("day")
1
>>> x = "Happy Birthday"
>>> x.lower()
'happy birthday'
>>> x.upper()
'HAPPY BIRTHDAY'
>>> x.capitalize()
'Happy birthday'
>>> x.title()
'Happy Birthday'
>>> 
>>> x.isalpha()
False
>>> "abcd".isalpha()
True
>>> "123".isdigit()
True
>>> y = "happybirthday123"
>>> y.isalpha()
False
>>> y.isalnum()
True
>>> y = "happybirthday!123"
>>> y.isalnum()
False
>>> x = "happy birthday"
>>> x.index("birthday")
6
>>> x.find("birthday")
6
>>> x.index("Birthday")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x.index("Birthday")
ValueError: substring not found
>>> x.find("Birthday")
-1
>>> y = "000happybirthday000"
>>> y.strip("0")
'happybirthday'
>>> y.lstrip("0")
'happybirthday000'
>>> y.rstrip("0")
'000happybirthday'
>>> 
>>> name = input("What is your name?: ")
What is your name?: Zein\
>>> print(name)
Zein\
>>> len(name)
5
>>> name = input("What is your name?: ")
What is your name?: Zein/
>>> print(name)
Zein/
>>> len(name)
5
>>> name = input("What is your name?: ").strip(0)
What is your name?: Zein
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    name = input("What is your name?: ").strip(0)
TypeError: strip arg must be None or str
>>> name = input("What is your name?: ").strip()
What is your name?: Zein/
>>> len(name)
5
>>> 
