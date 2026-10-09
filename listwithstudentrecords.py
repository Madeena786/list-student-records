names=[]
marks=[]
n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Enter student name: ")
    mark=int(input("Enter student mark: "))
    names.append(name)
    marks.append(mark)
print()
print("Student Records")
print("************************")
for i in range(len(names)):
    print(names[i], ":", marks[i])
print()
sname=input("Enter student name to search: ")
if sname in names:
    index=names.index(sname)
    print(sname, "scored", marks[index])
else:
    print("Student not found")
print()
highest=max(marks)
hindex=marks.index(highest)
print("Highest Mark:", highest)
print("Student with highest mark:", names[hindex])
print()
lowest=min(marks)
lindex=marks.index(lowest)
print("Lowest Mark:", lowest)
print("Student with lowest mark:", names[lindex])
print()
print("Marks in ascending order:", sorted(marks))
print("Marks in descending order:", sorted(marks, reverse=True))







