## **Practice Python Lists With Student Records**



### **Task 9:**



This project is a Python program that stores student names and marks using lists.



The program allows the user to enter student details and performs different list operations such as displaying student records, searching for a student, finding the highest and lowest marks, and sorting marks.



###### **Objective**



The main objective of this project is to practice Python lists and understand how lists can be used to store and process student records.



###### **Technologies Used**



Python



###### **Features**

* Accepts the number of students from the user
* Accepts student names from the user
* Accepts student marks from the user
* Stores names and marks in lists
* Displays all student records
* Searches for a student by name
* Finds the highest mark
* Finds the student with the highest mark
* Finds the lowest mark
* Finds the student with the lowest mark
* Sorts marks in ascending order
* Sorts marks in descending order



###### **Python Concepts Used**



* Lists
* `input()`
* `int()`
* `for` loop
* `range()`
* `append()`
* `len()`
* `in` operator
* `index()`
* `max()`
* `min()`
* `sorted()`
* `if-else`

&#x20;
**Program**
---



names=\[]

marks=\[]

n=int(input("Enter number of students: "))

for i in range(n):

&#x20;   name=input("Enter student name: ")

&#x20;   mark=int(input("Enter student mark: "))

&#x20;   names.append(name)

&#x20;   marks.append(mark)

print()

print("Student Records")

print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

for i in range(len(names)):

&#x20;   print(names\[i], ":", marks\[i])

print()

sname=input("Enter student name to search: ")

if sname in names:

&#x20;   index=names.index(sname)

&#x20;   print(sname, "scored", marks\[index])

else:

&#x20;   print("Student not found")

print()

highest=max(marks)

hindex=marks.index(highest)

print("Highest Mark:", highest)

print("Student with highest mark:", names\[hindex])

print()

lowest=min(marks)

lindex=marks.index(lowest)

print("Lowest Mark:", lowest)

print("Student with lowest mark:", names\[lindex])

print()

print("Marks in ascending order:", sorted(marks))

print("Marks in descending order:", sorted(marks, reverse=True))



###### **Sample Input:**

Enter number of students: 5

Enter student name: Madeena

Enter student mark: 95

Enter student name: Sravani

Enter student mark: 93

Enter student name: swathi

Enter student mark: 92

Enter student name: manjula

Enter student mark: 96

Enter student name: aswini

Enter student mark: 90



###### **Sample Output:**



Student Records

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Madeena : 95

Sravani : 93

swathi : 92

manjula : 96

aswini : 90



###### **Explanation:**

The program uses two lists:



names = \[]

marks = \[]



The names list stores student names and the marks list stores their marks.

The append() method adds each user's input to the corresponding list.

The same index is used to connect a student with their marks.

The program uses max() to find the highest mark and min() to find the lowest mark.

The sorted() function is used to arrange the marks in ascending and descending order.



###### **Conclusion**

This project helped me understand how Python lists can be used to store and process student records. I practiced searching, sorting, finding the highest and lowest values, and working with user input.









