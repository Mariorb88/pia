import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.compose import make_column_selector
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

cat_pipeline = make_pipeline( # Pipeline for categorical features
    SimpleImputer(strategy="most_frequent"), # Impute missing values with the most frequent value
    OneHotEncoder(handle_unknown="ignore")) # One-hot encode the categorical features

def column_ratio(X): # Custom transformer to compute the ratio of two columns
    return X[:, [0]] / X[:, [1]]

def ratio_name(function_transformer, feature_names_in): # Custom function to name the output columns
    return ["ratio"]  # feature names out

def ratio_pipeline(): # Pipeline for ratio features (create new features by dividing two columns)
    return make_pipeline(
        SimpleImputer(strategy="median"),
        FunctionTransformer(column_ratio, feature_names_out=ratio_name),
        StandardScaler())

log_pipeline = make_pipeline(
    SimpleImputer(strategy="median"),
    FunctionTransformer(np.log, feature_names_out="one-to-one"),
    StandardScaler())

default_num_pipeline = make_pipeline(SimpleImputer(strategy="median"),
                                     StandardScaler())

preprocessing = ColumnTransformer([
        ("bedrooms", ratio_pipeline(), ["total_bedrooms", "total_rooms"]), # razón entre total_bedrooms y total_rooms (nueva feature)
        ("rooms_per_house", ratio_pipeline(), ["total_rooms", "households"]), # razón entre total_rooms y households (nueva feature)
        ("people_per_house", ratio_pipeline(), ["population", "households"]), # razón entre population y households (nueva feature)
        ("log", log_pipeline, ["total_bedrooms", "total_rooms", "population",
                               "households", "median_income"]), # logaritmo de las columnas seleccionadas (para cambiar distribuciones sesgadas -skewed- por distribuciones normales)
        ("geo", cluster_simil, ["latitude", "longitude"]), # similitud con los clusters
        ("cat", cat_pipeline, make_column_selector(dtype_include=object)), # pipeline categórico
    ],
    remainder=default_num_pipeline)  # one column remaining: housing_median_age

full_pipeline = Pipeline([
    ("preprocessing", preprocessing),
    ("random_forest", RandomForestRegressor(random_state=42, n_jobs=1)),
])