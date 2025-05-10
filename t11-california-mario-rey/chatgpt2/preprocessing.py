
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd

def get_preprocessor(df):
    num_attribs = df.select_dtypes(include=["float64", "int"]).columns.drop("median_house_value")
    cat_attribs = df.select_dtypes(include=["object"]).columns

    num_pipeline = Pipeline([
        ('std_scaler', StandardScaler())
    ])

    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(handle_unknown='ignore'), cat_attribs),
    ])

    return full_pipeline
