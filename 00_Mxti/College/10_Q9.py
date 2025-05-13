'''
Problem 9: String Manipulation (split, join)
Task:
Take a sentence string: sentence = "This is a sample sentence for splitting".
Use the split() method to break the sentence into a list of words.
Print the resulting list of words.
Take the list of words you just created and use the join() method to recreate the original sentence string, but this time using a hyphen (-) as the separator between words.
Print the new hyphenated string.
'''
sentence = "This is a sample sentence for splitting"
splt_str = sentence.split()
print(splt_str)
join_str = '-'.join(splt_str)
print(join_str)