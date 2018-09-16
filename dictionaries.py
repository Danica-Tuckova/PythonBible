Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
# creat empty dictionary
>>> students = {}
>>> 
>>> students = {"Alice":25, "Bob":27, "Claire":17, "Dan":21, "Emma":22}
>>> 
>>> # look up Dan age
>>> students["Dan"]
21
>>> 
>>> # add new student Fred with the age of 25
>>> students["Fred"] = 25
>>> students["Fred"]
25
>>> 
>>> # Alice get older to 26
>>> students["Alice"] = 26
>>> students["Alice"]
26
>>> 
>>> # del Fred
>>> del students ["Fred"]
>>> students["Fred"]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    students["Fred"]
KeyError: 'Fred'
>>> 
>>> # dictionary KEYS method
>>> students.keys()
dict_keys(['Alice', 'Bob', 'Claire', 'Dan', 'Emma'])
>>> #dict_keys does not support indexing
>>> students.keys()[0]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    students.keys()[0]
TypeError: 'dict_keys' object does not support indexing
>>> 
>>> # turn dictionary students into list
>>> dic_into_list = list(students.keys())
>>> dic_into_list
['Alice', 'Bob', 'Claire', 'Dan', 'Emma']
>>> # now we can indexing
>>> dic_into_list[0]
'Alice'
>>> dic_into_list[1]
'Bob'
>>> 
>>> # dot VALUES method
>>> students.values()
dict_values([26, 27, 17, 21, 22])
>>> # turn dictionary into list
>>> list(students.values())
[26, 27, 17, 21, 22]
>>> 
>>> # dot ITEM method

>>> students.items()
dict_items([('Alice', 26), ('Bob', 27), ('Claire', 17), ('Dan', 21), ('Emma', 22)])
>>> 
