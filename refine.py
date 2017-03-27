import pandas as pd


# Might not need...
def FilterNull(df, variable):
    return df[pd.notnull(df[variable])]


def FilterType(df, variable, type_list):
    return df[df[variable].isin(type_list)]


def FilterDigits(df, variable, max_digit, no_code):
    if no_code:
        return df[(df[variable].isin(range(0, max_digit + 1))) | (df[variable] == -9)]
    else:
        return df[df[variable].isin(range(0, max_digit + 1))]


def FilterDuplicates(df, variable):
    return df.drop_duplicates(subset=variable, keep='last')


def refineData():
    regions = ["E12000001", "E12000002", "E12000003", "E12000004", "E12000005", "E12000006",
               "E12000007", "E12000008", "E12000009", "W92000004"]
    residence_types = ["H", "C"]

    family_composition = ["Family Composition", 6, True]
    population_base = ["Population Base", 3, False]
    sex = ["Sex", 2, False]
    age = ["Age", 8, False]
    martial_status = ["Marital Status", 5, False]
    student = ["Student", 2, False]
    country_of_birth = ["Country of Birth", 2, True]
    health = ["Health", 5, True]
    ethnic_group = ["Ethnic Group", 5, True]
    religion = ["Religion", 9, True]
    economic_activity = ["Economic Activity", 9, True]
    occupation = ["Occupation", 9, True]
    hours_worked_per_week = ["Hours worked per week", 4, True]
    approximated_social_grade = ["Approximated Social Grade", 4, True]

    digit_variables = [family_composition, population_base, sex, age, martial_status, student, country_of_birth,
                       health, ethnic_group, religion, economic_activity, occupation, hours_worked_per_week,
                       approximated_social_grade]

    df = pd.read_csv("./census2011.csv")

    # Filtering out any NaNs
    df = df.dropna()

    # Might not need...
    # Filtering Null Personal ID's
    df = FilterNull(df, "Person ID")

    # Filter inaccurate Regions
    df = FilterType(df, "Region", regions)

    # Filter inaccurate Residence Types
    df = FilterType(df, "Residence Type", residence_types)

    # Filter each digit variable
    for digit_variable in digit_variables:
        df = FilterDigits(df, digit_variable[0], digit_variable[1], digit_variable[2])

    # Remove Duplicate Person ID's
    df = FilterDuplicates(df, "Person ID")

    # Create refine csv with filtered dataframe
    df.to_csv('refined.csv')


refineData()
