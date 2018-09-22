# A
a = 100

def f1a():
    print(a)

def f2a():
    print(a)

f1a()
f2a()
print(a)

# D

d = 250

def f1d():
    d = 100
    print(d)

def f2d():
    d = 50
    print(d)

f1d()
f2d()
print(d)

# E

e = 250

def f1e():
    ee = e + 10
    print(ee)

def f2e():
    e = 50
    print(e)

f1e()
f2e()
print(e)

# F

def f1f():
    global f 
    f = 100
    print(f)

def f2f():
    f = 50
    print(f)

f1f()
f2f()
print(f)

# G 

g = [1, 2, 3]

def f1g():
    g = 10
    print(g)

def f2g():
    g = 50
    print(g)

f1g()
f2g()
print(g)    

# H 

h = [1, 2, 3]

def f1h():
    global h
    h[0] = 5
    print(h)

def f2h():
    h = 50
    print(h)

f1h()
f2h()
print(h)
