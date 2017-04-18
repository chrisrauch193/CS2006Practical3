import refine


def digit_discrepancies_query_filter(df, investigation_variable, investigation_values, discrepancy_variable, discrepancy_values):
    """Return records where two specified variables are into two specified sets."""

    return df[(df[investigation_variable].isin(investigation_values)) & (df[discrepancy_variable].isin(discrepancy_values))]



num_hours_list = [7.5, 23, 39.5, 56.5]

# dataframe for all students
df_students = df[df["Student"] == 1]

# dataframe for all Economically Active Full-Time Students
df_child_students = digit_discrepancies_query_filter(df, "Student", [1], "Economic Activity", [6])

# dataframe for all Economically Inactive Students
df_full_students = digit_discrepancies_query_filter(df, "Student", [1], "Economic Activity", [4])


def hours_categories(df):

    codes = range(1, 5)

    return map(lambda i: len((df[df["Hours worked per week"] == i])), codes)

categories_students = hours_categories(df_students)
categories_child_students = hours_categories(df_child_students)
categories_full_students = hours_categories(df_full_students)

def elemwise_product(a, b):

    return sum(map(lambda x, y: x * y, zip(a, b)))

hours_students = elemwise_product(num_hours_list, categories_students)
hours_child_students = elemwise_product(num_hours_list, categories_child_students)
hours_full_students = elemwise_product(num_hours_list, categories_full_students)

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
