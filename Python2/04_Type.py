a = 5
t = type(a) #<class 'int'>
print(t)

b = 5.1
t = type(b) #<class 'float'>
print(t)

c = "Alex"
t = type(c) #<class 'str'>
print(t)
x = "5.6"
print(type(x))

d = True
t = type(d) #class 'bool'>
print(t)

e = None
t = type(e) #Class 'NoneType'>
print(t)

#Type conversion
# int() function is used to convert a number or a string to an integer.
# float() function is used to convert a number or a string to a floating point number.
# str() function is used to convert a number or a string to a string.
# bool() function is used to convert a number or a string to a boolean value.
# complex() function is used to convert a number or a string to a complex number.
# list() function is used to convert a number or a string to a list.
# tuple() function is used to convert a number or a string to a tuple.
# dict() function is used to convert a number or a string to a dictionary.
# set() function is used to convert a number or a string to a set.
a = "5.6"
b = float(a)
print(type(b),": ",b)
print(int(b))

y = 5.3
print(str(y))