import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import sys
import glob
import warnings
from sklearn.model_selection import train_test_split
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, cross_validate
import seaborn as sns
import pyarrow
import pickle

# Read in parquet files and drop NAs
df_selected = pd.read_parquet('data/events_with_hit_features_[cut_off_time=0.5].parquet').dropna()

# Filter for muons only for the training set
df_muons = df_selected.query('`class`== "muon"')

# Train test split (muon data)
train_df, test_df_muon = train_test_split(df_muons, random_state=42)

# Append pion data to the test set
test_df = pd.concat([test_df_muon, df_selected.query('`class`== "pion"')])

# Define X and y
X_train = train_df.iloc[:, 1:19]
y_train = train_df['ring_radius_cal']
X_test = test_df.iloc[:, 1:19]
y_test = test_df['ring_radius_cal']

# Define the model
xgb_reg = xgb.XGBRegressor()

# Fit the model
xgb_reg.fit(X_train, y_train)

# Save the trained model
model_path = "saved_models/xgb_regressor_model.ubj"
xgb_reg.save_model(model_path)
