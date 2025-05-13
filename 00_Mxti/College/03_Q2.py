''' 
Problem 2: List Manipulation and Mutability

Task:
Create a list of numbers: original_list = [10, 20, 30, 40, 50].
Create a new variable aliased_list and assign original_list to it.
Create a shallow copy of original_list called shallow_copied_list.
Create a deep copy of original_list called deep_copied_list (you'll need to import the copy module).
Append the number 60 to original_list.
Modify the element at index 1 in shallow_copied_list to 99.
Print all three lists (original_list, aliased_list, shallow_copied_list, deep_copied_list) and explain the output in terms of mutability, aliasing, shallow copy, and deep copy.
'''
import copy as c
lst = [10, 20, [30,500], 40, 50]
lst2 = lst
sallow_cpy = lst.copy()
lst.append(60)
sallow_cpy[1] = 99
print("org list ",lst)
print("aliased list ",lst)
print("sallow_cpy list ",lst)

