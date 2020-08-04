"""
three functions to help automate
the cleaning and wrangling of data
for the sake of ML prep
"""

from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


def helper1(X):
    """
    this will remove whitespaces in the column names
    """

# Prevent SettingWithCopyWarning; read-in as csv
    #X = pd.read_csv(X)
    X = X.copy()


# removes all whitespace from column names
    X.columns = X.columns.str.strip()

# return the dataframe
    return X


def helper2(X):
    """
    convert any column w/ date data into dt object
    from the inferred date column it creates new columns
    in the dataset for each time metric
    i.e. year, month, week, second etc...
    then deletes original date column b/c it's duplicate
    data at that point
    """
# reads in any column w/ date instead of (object,datetime, int64)
    for col in X.columns:
        if X[col].dtype == 'object':
            try:
                X[col] = pd.to_datetime(X[col])
            except ValueError:
                pass

# Extract components from date_recorded
    X['Year'] = X[col].dt.year
    X['Month'] = X[col].dt.month
    X['Week'] = X[col].dt.week
    X['Day'] = X[col].dt.day
    X['Hour'] = X[col].dt.hour
    X['Minute'] = X[col].dt.minute
    X['Second'] = X[col].dt.second

# drops the original Date column
    X = X.drop(columns='Date')

# return the dataframe
    return X


def helper3(X):
    """
    splits data into train, val, test sets
    """
    # Split train into train & val
    train_one, test = train_test_split(X, train_size=0.80, test_size=0.20,
                                       random_state=42)

    train, val = train_test_split(train_one, train_size=0.80, test_size=0.20,
                                  random_state=42)

    return train, val, test
