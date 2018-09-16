Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
our_list = [27, 46, -5, 17, 99]
>>> print(our_list)
[27, 46, -5, 17, 99]
>>> type(our_list)
<class 'list'>
>>> 
>>> jackson = ["A", "B", "C", 1, 2, 3, "Do", "Rey", "Mi", True, False]
>>> jakson[4]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    jakson[4]
NameError: name 'jakson' is not defined
>>> jackson[4]
2
>>> jackson[7]
'Rey'
>>> jackson[-1]
False
>>> jackson[-2]
True
>>> x = jackson[6]
>>> x
'Do'
>>> jackson[0:3:1]
['A', 'B', 'C']
>>> jackson[0:3]
['A', 'B', 'C']
>>> 
>>> our_list = [1, 2, [3, 4, 5], 6, 7, 8]
>>> our_list[2]
[3, 4, 5]
>>> our_list[2][0]
3
>>> our_list[2][2]
5
>>> our_list[2][1:]
[4, 5]
>>> our_list[2][0::2]
[3, 5]
>>> 
>>> #Table
>>> 
our_table = [[1,2,3], [4,5,6], [7,8,9]]
>>> our_table[0]
[1, 2, 3]
>>> our_table[1]
[4, 5, 6]
>>> our_table[2]
[7, 8, 9]
>>> our_table[1][2]
6
>>> our_table[0][2]
3
>>> our_table[1][1:]
[5, 6]
>>> 
