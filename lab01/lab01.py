import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

housing_data = fetch_california_housing()
housing = pd.DataFrame(housing_data.data, columns=housing_data.feature_names)
housing['target'] = housing_data.target

print(housing.head())

print(housing_data.DESCR)