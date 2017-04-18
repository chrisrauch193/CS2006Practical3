"""Module containing functions to refine a dataset."""

import pandas as pd


def filter_null(df, variable):
    """Return records not containing null values in a specified column."""

    return df[pd.notnull(df[variable])]


def filter_type(df, variable, type_list):
    """Return records where a specified variable is in a specified set of values."""

    return df[df[variable].isin(type_list)]


def filter_digits(df, variable, max_digit, no_code):
    """Return records where digits are within a range or a specified 'no code' value."""

    if no_code is not None:
        return df[(df[variable].isin(range(0, max_digit + 1))) | (df[variable] == no_code)]
    else:
        return df[df[variable].isin(range(0, max_digit + 1))]


def filter_all_types(df, all_types):
    """Return records where a list of types are filtered on."""

    for type_list in all_types:
        return filter_type(df, *type_list)


def filter_digit_variables(df, digit_variables):
    """Return records where a list of digit variables are filtered on."""

    for digit_variable in digit_variables:
        return filter_digits(df, *digit_variable)


def filter_duplicates(df, variable):
    """Return records that are not duplicated in a specified variable."""

    return df.drop_duplicates(subset=variable, keep='last')


def refine_data(df):
    """Return a refined dataset for the 2011 UK census."""

    regions = [
        "Region",
        ["E12000001", "E12000002", "E12000003", "E12000004", "E12000005",
        "E12000006","E12000007", "E12000008", "E12000009", "W92000004"]
    ]
    residence_types = ["Residence Type", ["H", "C"]]

    no_code = -9
    fill = None

    family_composition = ["Family Composition", 6, no_code]
    population_base = ["Population Base", 3, fill]
    sex = ["Sex", 2, fill]
    age = ["Age", 8, fill]
    martial_status = ["Marital Status", 5, fill]
    student = ["Student", 2, fill]
    country_of_birth = ["Country of Birth", 2, no_code]
    health = ["Health", 5, no_code]
    ethnic_group = ["Ethnic Group", 5, no_code]
    religion = ["Religion", 9, no_code]
    economic_activity = ["Economic Activity", 9, no_code]
    occupation = ["Occupation", 9, no_code]
    hours_worked_per_week = ["Hours worked per week", 4, no_code]
    approximated_social_grade = ["Approximated Social Grade", 4, no_code]

    all_types = [regions, residence_types]

    digit_variables = [
        family_composition, population_base, sex, age, martial_status, student,
        country_of_birth, health, ethnic_group, religion, economic_activity,
        occupation, hours_worked_per_week, approximated_social_grade
    ]

    # Filtering out any NaNs
    df = df.dropna()

    # Filtering Null Personal ID's
    df = filter_null(df, "Person ID")

    df = filter_all_types(df, all_types)

    df = filter_digit_variables(df, digit_variables)

    # Remove Duplicate Person ID's
    df = filter_duplicates(df, "Person ID")

    return df
