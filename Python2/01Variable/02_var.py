x = 5
y = 'alex'

print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
z = 5 # z is of type int
z = 'Variable' # z is now of type str

print(z)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.

# Example

a = str(3)
b = int(3)
c = float(3)

print(type(a))
print(type(b))
print(type(c))

e = 'john'
E = "john"
f = '''jonh'''
g = """john"""
#all are same
print(type(e))
print(type(E))
print(type(f))
print(type(g))