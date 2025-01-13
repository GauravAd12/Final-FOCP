#  3. The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but this is
# sometimes varied to create groups of similar size. Write a program that prompts for
# the number of students and group size, and then displays how many groups will be
# needed and how many will be le over in a smaller group.
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101
# students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.

students = int(input("How many students? "))  
group_size = int(input("Required group size? "))  

num_groups = students // group_size
leftover = students % group_size

group_plural = "groups" if num_groups != 1 else "group"
student_plural = "students" if leftover != 1 else "student"

print(f"There will be {num_groups} {group_plural} with {leftover} {student_plural} left over.")
# Output: There will be 5 groups with 3 students left over.
