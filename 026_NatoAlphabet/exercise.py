# import random
# import pandas

# # Add Number + 1 to new_numbers
# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]

# # Add each letter to new_list
# name = "Ramon"
# new_list = [letter for letter in name]
# print(new_list)

# # Double each number in range_list
# range_list = [num * 2 for num in range(1,5)]

# # Add only short names (< 5) to short_names
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]

# # Save Names in Uppercase to capital_names
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# capital_names = [name.upper() for name in names if len(name) > 5]
# print(capital_names)

# # Generate Random Score for each Student and fill in a Dictionary
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student:random.randint(1,100) for student in names}

# # Generate Random Score for each Student, and only let them with score higher or equal 60 pass and fill in passed_students dictionary
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student:random.randint(1,100) for student in names}
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

# student_dict = {
#     "student": ["Angela", "James", "Liy"],
#     "score": [56, 76, 98]
# }

# # Print All Keys or values
# for (key, value) in student_dict.items():
#     print(value)

# # Print the whole dataFrame
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # Print the key or the value from the dataFrame
# for (key, value) in student_data_frame.items():
#     print(value)

# # Print the index or row from the dataFrame
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)