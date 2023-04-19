# ! DAY 25

numbers = [1, 2, 3]
new_numbers = []
for n in numbers:
    add_1 = n + 1
    new_numbers.append(add_1)

# list comprehension way
# new_list = [new_item for item in list]
new_list2 = [n + 1 for n in numbers]

name = "angela"
new_name = [letter for letter in name]

range_list = [num * 2 for num in range(1, 5)]

# Conditional list comprehension
# new_list = [new_item for item from list if test]
names = ["andres", "oscar", "allan", "fernando", "roberto"]
new_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]

# DICTIONARY COMPREHENSION
# new_dic = {new_key:new_value for (key, value) in dict.item() if test}

students = ["juan", "victoria", "angelica", "pedro"]
import random

student_scores = {student: random.randint(1, 101) for student in students}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

# PANDAS DATAFRAME
import pandas

student_dict = {"student": ["angel", "luis", "gabriel"], "score": [89, 56, 67]}
student_data_frame = pandas.DataFrame(student_dict)

# loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)


