'''
Problem 8: Lambda and Higher-Order Functions/List Comprehension
Task:
Start with a list of numbers: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
Use the map() function with a lambda function to create a new list where each number is squared.
Use the filter() function with a lambda function to create a new list containing only the even numbers from nums.
Rewrite steps 2 and 3 using list comprehension instead of map/filter and lambda.
Print all three resulting lists.
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = [x*x for x in nums if x%2 == 0]
print("even number squared with list comprehension",x)