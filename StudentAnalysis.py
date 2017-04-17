from refine import *

df = pd.read_csv("./refined.csv")

num_hours_list = [7.5, 23, 39.5, 56.5]

# dataframe for all students
student_df = df[df["Student"] == 1]

# dataframe for all Economically Active Full-Time Students
child_student_df = InactiveStudent(df)

# dataframe for all Economically Inactive Students
full_student_df = FTStudent(df)

child_student_df.to_csv('test.csv')


# Total number of Students
student_total = len(student_df.index)

# Total number of Economically Inactive Students
child_student_total = len(child_student_df.index)

# Total number of Economically Active Full-Time Students
full_student_total = len(full_student_df.index)




# Total number of Students that work Part-Time < 15 hours
student_PT_total1 = len((student_df[student_df["Hours worked per week"] == 1]).index)

# Total number of Students that work Part-Time 16 hours > and < 30 hours
student_PT_total2 = len(student_df[student_df["Hours worked per week"] == 2].index)


# Total number of Economically Inactive Students that work Part-Time < 15 hours
child_student_PT_total1 = len(child_student_df[child_student_df["Hours worked per week"] == 1].index)

# Total number of Economically Inactive Students that work Part-Time > 16 hours and < 30 hours
child_student_PT_total2 = len(child_student_df[child_student_df["Hours worked per week"] == 2].index)


# Total number of Economically Active Full-Time Students that work Part-Time < 15 hours
full_student_PT_total1 = len(full_student_df[full_student_df["Hours worked per week"] == 1].index)

# Total number of Economically Active Full-Time Students that work Part-Time > 16 hours and < 30 hours
full_student_PT_total2 = len(full_student_df[full_student_df["Hours worked per week"] == 2].index)




# Total number of Students that work Full-Time > 31 hours and > 48 hours
student_FT_total3 = len(student_df[student_df["Hours worked per week"] == 3].index)

# Total number of Students that work Full-Time >= 49 hours
student_FT_total4 = len(student_df[student_df["Hours worked per week"] == 4].index)


# Total number of Economically Inactive Students that work Full-Time > 31 hours and < 48 hours
child_student_FT_total3 = len(child_student_df[child_student_df["Hours worked per week"] == 3].index)

# Total number of Economically Inactive Students that work Part-Time >= 49 hours
child_student_FT_total4 = len(child_student_df[child_student_df["Hours worked per week"] == 4].index)


# Total number of Economically Active Full-Time Students that work Full-Time > 31 hours and < 48 hours
full_student_FT_total3 = len(full_student_df[full_student_df["Hours worked per week"] == 3].index)

# Total number of Economically Active Full-Time Students that work Part-Time >= 49 hours
full_student_FT_total4 = len(full_student_df[full_student_df["Hours worked per week"] == 4].index)




# Average Part-Time hours worked by an Students
average_hours_worked_PT_S = ((student_PT_total1 * num_hours_list[0]) + (student_PT_total2 * num_hours_list[1])) \
                             / (student_PT_total1 + student_PT_total2)

# Average Full-Time hours worked by an Students
average_hours_worked_FT_S = ((student_FT_total3 * num_hours_list[2]) + (student_FT_total4 * num_hours_list[3])) \
                             / (student_FT_total3 + student_FT_total4)


# # Average Part-Time hours worked by an Economically Inactive Students
# average_hours_worked_PT_CS = ((child_student_PT_total1 * num_hours_list[0]) + (child_student_PT_total2 * num_hours_list[1])) \
#                              / (child_student_PT_total1 + child_student_PT_total2)
#
# # Average Full-Time hours worked by an Economically Inactive Students
# average_hours_worked_FT_CS = ((child_student_FT_total3 * num_hours_list[2]) + (child_student_FT_total4 * num_hours_list[3])) \
#                              / (child_student_FT_total3 + child_student_FT_total4)


# Average Part-Time hours worked by an Economically Active Full-Time Students
average_hours_worked_PT_FS = ((full_student_PT_total1 * num_hours_list[0]) + (full_student_PT_total2 * num_hours_list[1])) \
                             / (full_student_PT_total1 + full_student_PT_total2)

# Average Full-Time hours worked by an Economically Active Full-Time Students
average_hours_worked_FT_FS = ((full_student_FT_total3 * num_hours_list[2]) + (full_student_FT_total4 * num_hours_list[3])) \
                             / (full_student_FT_total3 + full_student_FT_total4)
print(student_FT_total3)
print(average_hours_worked_PT_S)
print(average_hours_worked_FT_S)
# print(average_hours_worked_PT_CS)
# print(average_hours_worked_FT_CS)
print(average_hours_worked_PT_FS)
print(average_hours_worked_FT_FS)
