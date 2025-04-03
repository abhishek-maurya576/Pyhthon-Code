#Build a simple grading system where marks are input and grades (A, B, C, etc.)are assigned.
print("Grading System\nEnter marks outof 100")
sh = int(input("Enter a Hindi marks: "))
se = int(input("Enter a English marks: "))
sm = int(input("Enter a Mathematics marks: "))
ss = int(input("Enter a Science marks: "))
tmarks = sh+se+sm+ss
print("Total marks:",tmarks)
if 400<= tmarks >350:
    print("Grade A")
elif 350 <= tmarks >300:
    print("Grade B")
elif 300 <= tmarks >250:
    print("Grade C")
elif 250 <= tmarks >200:
    print("Grade D")
elif 200 > tmarks >=0:
    print("Grade F")
else:
    print("Something went wrong")

