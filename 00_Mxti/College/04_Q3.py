'''Problem 3: Tuple Unpacking and Processing

Task:
Create a list of tuples, where each tuple contains a student's name and score, like students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)].
Write a Python function display_scores(student_list) that takes this list of tuples.
Inside the function, iterate through the list. For each tuple, use tuple unpacking to extract the name and score into separate variables.
Print the name and score in a formatted way for each student, e.g., "Student: Alice, Score: 85".
'''
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
def display_scores(student_list):
    for x in student_list:
        student = x[0]
        score = x[1]
        print(f"Student: {student}, Score: {score}")
display_scores(students)