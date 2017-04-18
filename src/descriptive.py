"""Module with functions for a descriptive analyses of a dataset."""

import pandas as pd


def total_records(df):
    """Return message for total number of records in dataframe."""

    return "The total number of records in the dataframe is " + str(len(df)) + '.'

def all_data_types(df):
    """Return message for all data types in a dataframe."""

    return "All data types:\n" + str(df.dtypes)

def count_occurrences(df, ignore_variables):
    """Strip PersonID column, count values, and return message."""

    result = ""
    for column in df:
        if column not in ignore_variables:
            result += str(column) + " counts:\n" + str(df[column].value_counts()) + "\n" * 2

    return result
