import os
import random
# This line of code is added to the file to check the current working directory.
print(os.getcwd())

# 1. Read the student IDs from a text file (e.g., student_ids.txt) containing multiple student IDs, one per line, in the format YYYY-N-MM-xxx (e.g., 2024-1-05-123).
studnet_id_file = './student_ids.txt'

try:
    with open(studnet_id_file, 'r') as file:
        students_id = file.read().splitlines()
        print("The Student IDs are loaded successfully.")
except FileNotFoundError:
    print("Error: The file 'student_ids.txt' was not found.")

# 2. Maintain a list of students who haven’t been selected yet.
unselected_students = students_id[:]

# 5. Repeat steps 3 and 4 until all students have been picked.
viva_counter = 1
while True:
    # 3. Randomly select a student from the list of students who haven’t been selected yet.
    selected_student = random.choice(unselected_students)
    print(f"Viva {viva_counter}: The selected student is {selected_student}")

    # 4. Remove the selected student from the list.
    unselected_students.remove(selected_student)
    viva_counter += 1

    # 6. When all students have been selected, reset the list to include all students again.
    if not unselected_students and viva_counter >= len(students_id):
        print("All students have been selected.")
        unselected_students = students_id[:]
        break
