import pandas as pd

def check_missing_values(df):
    return df.isnull().sum()

def check_invalid_age(df):
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    return df[(df['age'] < 0) | (df['age'] > 120)]

def check_missing_age(df):
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    return df[df['age'].isnull()]

def check_invalid_gender(df):
    return df[~df['gender'].isin(['M', 'F', 'Female', 'Male'])]

def check_weight_mismatch(df):
    df['admissionweight'] = pd.to_numeric(df['admissionweight'], errors='coerce')
    df['dischargeweight'] = pd.to_numeric(df['dischargeweight'], errors='coerce')
    return df[
        (df['admissionweight'].notnull()) &
        (df['dischargeweight'].notnull()) &
        (df['dischargeweight'] < df['admissionweight'] * 0.5)
    ]

def check_missing_discharge_status(df):
    return df[df['hospitaldischargestatus'].isnull()]

