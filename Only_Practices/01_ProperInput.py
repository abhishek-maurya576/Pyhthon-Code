# Write a program to collect and display a user’s name, age, and height, ensuring proper type casting.
name = input("Enter User's Name: ")
age = int(input("Enter user's Age: "))
height = float(input("Enter user's Height (in meters): "))
print("User's name: ",name)
print("User's Age: ",age)
print("User's height: ",height,"meters")

print("===========================================")

print("name ",name,"age ",age,"height ",height, sep="-")