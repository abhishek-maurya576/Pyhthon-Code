

**Coding Practice Problems: OOP Using Python (BCA123)**

These problems are designed to help you practice the coding aspects related to the topics in your syllabus and the provided PYQ. Attempting these will prepare you for similar questions in your exam.

**Unit 1 & 2: Python Fundamentals, Data Types, and Basic Data Structures**

*   **Problem 1: User Input, Data Types, and Basic Output with Validation**
    *   **Task:** Write a Python program that prompts the user to enter their year of birth. Calculate their approximate age and print a message like "You are approximately X years old." Implement basic validation: ensure the input is a valid integer representing a year (e.g., between 1900 and the current year). If the input is invalid, print an error message.
    *   **Relevant PYQ/Topics:** Q1 OR (a) (Input, Output, Variables, Validation), Unit 1 Basics.

*   **Problem 2: List Manipulation and Mutability**
    *   **Task:**
        1.  Create a list of numbers: `original_list = [10, 20, 30, 40, 50]`.
        2.  Create a new variable `aliased_list` and assign `original_list` to it.
        3.  Create a *shallow copy* of `original_list` called `shallow_copied_list`.
        4.  Create a *deep copy* of `original_list` called `deep_copied_list` (you'll need to import the `copy` module).
        5.  Append the number `60` to `original_list`.
        6.  Modify the element at index 1 in `shallow_copied_list` to `99`.
        7.  Print all three lists (`original_list`, `aliased_list`, `shallow_copied_list`, `deep_copied_list`) and explain the output in terms of mutability, aliasing, shallow copy, and deep copy.
    *   **Relevant PYQ/Topics:** Q1(b) (Mutability), Q2(a) (Shallow/Deep Copy), Unit 2 List Operations.

*   **Problem 3: Tuple Unpacking and Processing**
    *   **Task:**
        1.  Create a list of tuples, where each tuple contains a student's name and score, like `students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]`.
        2.  Write a Python function `display_scores(student_list)` that takes this list of tuples.
        3.  Inside the function, iterate through the list. For each tuple, use **tuple unpacking** to extract the name and score into separate variables.
        4.  Print the name and score in a formatted way for each student, e.g., "Student: Alice, Score: 85".
    *   **Relevant PYQ/Topics:** Q2(b) (Tuple Unpacking), Q2 OR (b) (List of Tuples, Function, Formatting), Unit 2 Tuples.

**Unit 3: Object-Oriented Programming in Python**

*   **Problem 4: Class and Instance Variables, Basic Methods**
    *   **Task:**
        1.  Define a class called `Dog`.
        2.  Include a **class variable** `species` and set its value to `"Canis familiaris"`.
        3.  Include an `__init__` method that takes `name` and `age` as parameters and sets them as **instance variables** (`self.name`, `self.age`).
        4.  Add a method `bark()` that prints `f"{self.name} says Woof!"`.
        5.  Add a method `description()` that returns a string describing the dog, e.g., `f"{self.name} is {self.age} years old."`.
        6.  Create two `Dog` objects with different names and ages.
        7.  Print the `species` using the class name and using one of the object names. Call the `bark()` and `description()` methods for both objects.
        8.  Briefly explain the difference in how you access class vs. instance variables and how their values differ across instances.
    *   **Relevant PYQ/Topics:** Q3(a) (Class vs. Instance Variables, Scope), Unit 3 Class/Objects.

*   **Problem 5: Single Inheritance and `super()`**
    *   **Task:**
        1.  Create a base class `Vehicle` with an `__init__` method that takes a `brand` and a `year` and stores them. Add a method `display_info()` that prints the brand and year.
        2.  Create a derived class `Car` that inherits from `Vehicle`.
        3.  The `Car` class `__init__` method should take `brand`, `year`, and `model` as parameters. Use `super().__init__(brand, year)` to call the parent class constructor, and then store the `model` as an instance variable.
        4.  Override the `display_info()` method in the `Car` class to also print the model along with the brand and year.
        5.  Add a new method `drive()` in the `Car` class that prints a message like "The [brand] [model] is driving."
        6.  Create a `Car` object and call its `display_info()` and `drive()` methods.
    *   **Relevant PYQ/Topics:** Q3(b) (super()), Q3 OR (a) (Inheritance, Code Reuse), Unit 3 Inheritance.

*   **Problem 6: Illustrating Polymorphism (Duck Typing)**
    *   **Task:**
        1.  Define two different classes, `Duck` and `Person`.
        2.  Both classes should have a method named `speak()`. The `Duck` class's `speak()` method should print "Quack", and the `Person` class's `speak()` method should print "Hello".
        3.  Write a function `make_it_speak(obj)` that takes an object `obj` as input and calls `obj.speak()`.
        4.  Create an instance of `Duck` and an instance of `Person`.
        5.  Call the `make_it_speak()` function with both the `Duck` object and the `Person` object as arguments.
        6.  Observe and explain how the same function call (`obj.speak()`) results in different behavior based on the object's type.
    *   **Relevant PYQ/Topics:** Q1(a) (Polymorphism), Unit 3 Polymorphism.

**Unit 4: Functions, Files, Strings, Dictionaries**

*   **Problem 7: Dictionary for Frequency Counting**
    *   **Task:** Write a Python program that takes a list of words (you can define the list yourself) and uses a dictionary to count the occurrences of each word. Print the resulting dictionary.
    *   **Relevant PYQ/Topics:** Unit 4 Dictionaries (as per notes), related to data processing.

*   **Problem 8: Lambda and Higher-Order Functions/List Comprehension**
    *   **Task:**
        1.  Start with a list of numbers: `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.
        2.  Use the `map()` function with a **lambda** function to create a new list where each number is squared.
        3.  Use the `filter()` function with a **lambda** function to create a new list containing only the even numbers from `nums`.
        4.  Rewrite steps 2 and 3 using **list comprehension** instead of `map`/`filter` and `lambda`.
        5.  Print all three resulting lists.
    *   **Relevant PYQ/Topics:** Q4(a) (Lambda, Higher-Order Functions, List Comprehension), Unit 4 Functions.

*   **Problem 9: String Manipulation (`split`, `join`)**
    *   **Task:**
        1.  Take a sentence string: `sentence = "This is a sample sentence for splitting"`.
        2.  Use the `split()` method to break the sentence into a list of words.
        3.  Print the resulting list of words.
        4.  Take the list of words you just created and use the `join()` method to recreate the original sentence string, but this time using a hyphen (`-`) as the separator between words.
        5.  Print the new hyphenated string.
    *   **Relevant PYQ/Topics:** Q4(b) (`str.split`, `str.join`), Unit 4 String Processing.

*   **Problem 10: File Writing, Reading, and Error Handling**
    *   **Task:**
        1.  Write a function `write_data_to_file(filename, data_lines)` that takes a filename and a list of strings. Use the `with open(...)` statement in `"w"` mode to write each string in `data_lines` to the file on a new line.
        2.  Write a function `read_file_and_check_length(filename)`.
        3.  Inside `read_file_and_check_length`, use a `try...except` block to handle a potential `FileNotFoundError`.
        4.  If the file is found, read its entire content. Check the number of characters. If the total character count (excluding newlines if you strip them, be consistent) is less than 100, raise a `ValueError` (or a custom exception if you've learned that) with the message "Characters less than the range".
        5.  Call `write_data_to_file()` to create a file with less than 100 characters.
        6.  Call `read_file_and_check_length()` on this file and observe the error handling.
        7.  (Optional) Call `write_data_to_file()` to create a file with more than 100 characters and call `read_file_and_check_length()` to see the successful case (or print a success message).
    *   **Relevant PYQ/Topics:** Q4 OR (a) (File Writing), Q4 OR (b) (File Reading, Error Handling, Raising Errors), Unit 4 File Handling.

**Unit 5: NumPy Basics**

*   **Problem 11: NumPy Array Creation and Attributes**
    *   **Task:**
        1.  Import NumPy.
        2.  Create a 1D NumPy array from the Python list `[1, 2, 3, 4, 5]`.
        3.  Create a 2x3 NumPy array filled with zeros.
        4.  Create a 3x2 NumPy array filled with ones, specifying the data type as `float64`.
        5.  Create a 1D NumPy array using `arange` that goes from 0 to 10 (exclusive) with a step of 2.
        6.  Create a 1D NumPy array using `linspace` that has 5 points between 0 and 1 (inclusive).
        7.  For each created array, print its `ndim`, `shape`, `size`, and `dtype`.
        8.  Briefly comment on why NumPy arrays are generally more efficient than Python lists for numerical operations (relating to homogeneity and underlying implementation).
    *   **Relevant PYQ/Topics:** Q5(a) (ndarray structure, difference from lists), Q5 OR (b) (Array Creation, Explain code/concepts), Unit 5 Creation Routines, Attributes.

*   **Problem 12: NumPy Indexing and Slicing**
    *   **Task:**
        1.  Create a 2D NumPy array, for example:
            ```python
            np_array = np.array([[10, 11, 12],
                                 [13, 14, 15],
                                 [16, 17, 18]])
            ```
        2.  Access and print the element at row 1, column 2.
        3.  Access and print the element at the last row, last column using negative indexing.
        4.  Print the first row of the array using slicing.
        5.  Print the last column of the array using slicing.
        6.  Print the sub-array consisting of the first two rows and the last two columns using slicing.
        7.  Use boolean indexing to select and print all elements in the array that are greater than 14.
        8.  Use integer array indexing to select and print the elements at positions (0,0), (1,1), and (2,2).
    *   **Relevant PYQ/Topics:** Q5 OR (a) (Indexing and Slicing), Unit 5 Indexing & Slicing.

*   **Problem 13: Reshaping NumPy Arrays**
    *   **Task:**
        1.  Create a 1D NumPy array using `arange` with 12 elements (e.g., from 0 to 11).
        2.  Print the initial array and its shape.
        3.  Use the `reshape()` method to reshape this 1D array into a 2D array with 3 rows and 4 columns. Print the reshaped array and its shape.
        4.  Reshape the original 1D array into a 2D array with 4 rows and 3 columns. Print this new reshaped array and its shape.
        5.  Reshape the original 1D array into a 3D array with shape (2, 2, 3). Print this array and its shape.
        6.  Attempt to reshape the original 1D array into a shape that doesn't match the total number of elements (e.g., (3, 5)). Explain the error you get.
    *   **Relevant PYQ/Topics:** Q5(b) (Reshaping ndarrays), Unit 5 Reshaping.

---

**How to Use These Problems:**

1.  **Read the Problem:** Understand exactly what the problem is asking you to do.
2.  **Plan Your Code:** Before writing, think about the steps needed. Which Python features (data types, control flow, functions, classes, methods, NumPy operations) will you need?
3.  **Write the Code:** Implement your plan in Python.
4.  **Test Your Code:** Run your program. Does it produce the correct output? Handle the specified conditions (like invalid input or file errors)?
5.  **Explain Your Code:** For exam preparation, it's often useful to add comments explaining different parts of your code, especially complex logic or where you're demonstrating specific concepts (like `super()`, slicing, error handling).
6.  **Review Relevant Notes:** If you get stuck or are unsure, refer back to your notes for the specific topic.

Solving these problems will give you hands-on experience with the core concepts covered in your syllabus and prepare you well for the practical aspects of your exam. Good luck!
