""" Create a dictionary of 3 students with their names as keys and marks as values. Print only the names of students who scored more than 50."""
d = {'Alex':50,'Smith':45,'Shreya':65,'Tasu':45,'Amreen':55}
for i in d:
    if d[i]>=50:
        print(d.keys())