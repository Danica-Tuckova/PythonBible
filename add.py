Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> A = [5, 12, 72, 55, 89]
>>> A
[5, 12, 72, 55, 89]
>>> # add number 1
>>> A = A + [1]
>>> A
[5, 12, 72, 55, 89, 1]
>>> # add string "BCD"
>>> A = A + ["BCD"]
>>> A
[5, 12, 72, 55, 89, 1, 'BCD']
>>> 
>>> # List Method
>>> 
>>> # add B, C, D
>>> A = A + list("BCD")
>>> A
[5, 12, 72, 55, 89, 1, 'BCD', 'B', 'C', 'D']
>>> list("Hello")
['H', 'e', 'l', 'l', 'o']
>>> 
>>> # add list of numbers
>>> A = A + [5, 6, 7]
>>> A
[5, 12, 72, 55, 89, 1, 'BCD', 'B', 'C', 'D', 5, 6, 7]
>>> A = A + [[6, 7, 8]]
>>> A
[5, 12, 72, 55, 89, 1, 'BCD', 'B', 'C', 'D', 5, 6, 7, [6, 7, 8]]
>>> 
>>> # append Method
>>> A = [5, 12, 72, 55, 89]
>>> A.append([10, 11, 12, 13])
>>> A
[5, 12, 72, 55, 89, [10, 11, 12, 13]]
>>> 
>>> # insert method
>>> # insert number 2 between 12 and 72
>>> A.insert(2, 100)
>>> A
[5, 12, 100, 72, 55, 89, [10, 11, 12, 13]]
>>> A.insert(2, 2)
>>> A
[5, 12, 2, 100, 72, 55, 89, [10, 11, 12, 13]]
>>> A.insert(2,[10, 20, 30])
>>> A
[5, 12, [10, 20, 30], 2, 100, 72, 55, 89, [10, 11, 12, 13]]
>>> 
>>> # remove method
>>> A = [1, 2, 3]
>>> A.remove(3)
>>> A
[1, 2]
>>> 
