'''
Problem 10: File Writing, Reading, and Error Handling
Task:
Write a function write_data_to_file(filename, data_lines) that takes a filename and a list of strings. Use the with open(...) statement in "w" mode to write each string in data_lines to the file on a new line.
Write a function read_file_and_check_length(filename).
Inside read_file_and_check_length, use a try...except block to handle a potential FileNotFoundError.
If the file is found, read its entire content. Check the number of characters. If the total character count (excluding newlines if you strip them, be consistent) is less than 100, raise a ValueError (or a custom exception if you've learned that) with the message "Characters less than the range".
Call write_data_to_file() to create a file with less than 100 characters.
Call read_file_and_check_length() on this file and observe the error handling.
(Optional) Call write_data_to_file() to create a file with more than 100 characters and call read_file_and_check_length() to see the successful case (or print a success message).
'''
data = ['Hello','Python','How','Are','You']
def write_data_to_file(filename, data_lines):
    with open(filename,'w') as f:
        f = filename.write(data_lines)
write_data_to_file('text.txt',data)
    