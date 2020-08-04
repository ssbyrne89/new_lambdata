"""
two functions to help automate
the cleaning and wrangling data
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
    from the date column it creates new columns in the dataset
    for each time metric i.e. year, month, week, etc...
    then deletes original date column   
    """
# reads in any column w/ date instead of (object,datetime, int64)
    for col in X.columns:
        if X[col].dtype == 'object':
            try:
                X[col] = pd.to_datetime(X[col])
            except ValueError:
                pass

# Extract components from date_recorded
    X['year'] = X[col].dt.year
    X['month'] = X['Date'].dt.month
    X['week'] = X['Date'].dt.week
    X['day'] = X['Date'].dt.day
    X['hour'] = X['Date'].dt.hour
    X['minute'] = X['Date'].dt.minute
    X['second'] = X['Date'].dt.second

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