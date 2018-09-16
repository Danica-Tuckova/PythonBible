Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> word = "supercalifragilisticexpialidocious"
>>> word[0]
's'
>>> word[2]
'p'
>>> word[0:5:1]
'super'
>>> word[0:5:2]
'spr'
>>> word[5:9:1]
'cali'
>>> word[5:]
'califragilisticexpialidocious'
>>> word[5::2]
'clfaiitcxildcos'
>>> word[:7]
'superca'
>>> word[:8]
'supercal'
>>> word[::-1]
'suoicodilaipxecitsiligarfilacrepus'
>>> word.index{"cali")
SyntaxError: invalid syntax
>>> word.index("cali")
5
>>> word.index("fragi")
9
>>> word[word.index("cali"):word.index("fragi")]
'cali'
>>> word[word.index("docious"):]
'docious'
>>> word[word.index("fragi"):word.index("list")]
'fragi'
>>> 
>>> #vypisat cali viacero sposobmi
>>> word[5:9:1]
'cali'
>>> word[word.index("cali"):word.index("frag")]
'cali'
>>> 
