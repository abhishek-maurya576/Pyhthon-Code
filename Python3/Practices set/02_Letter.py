# Write a program to fill in a letter template given below with name and date.
# letter = ''' 
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
letter1 = '''Dear Alex
You are selected!
27 Dec 2024'''
print(letter1)

letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Alex").replace("<|Date|>","28 Dec 2024")) #this called chaining od .replace() function