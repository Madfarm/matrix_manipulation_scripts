import pandas as pd
from scipy.stats import linregress
import numpy as np


# Load the dataset into a Pandas DataFrame
data = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Study_Hours': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'Exam_Score': [65, 75, 80, 85, 90, 92, 95, 98, 100, 102]
}
df = pd.DataFrame(data)


# Perform exploratory data analysis (EDA) to understand the structure and characteristics of the dataset
assert df.shape == (10, 3), "DataFrame should have 10 rows and 3 columns"
assert df['Student_ID'].dtype == int, "Student_ID column should be of type int"
assert df['Study_Hours'].dtype == int, "Study_Hours column should be of type int"
assert df['Exam_Score'].dtype == int, "Exam_Score column should be of type int"


# Use linear regression from SciPy to fit a regression line to the data
slope, intercept, r_value, p_value, std_err = linregress(df['Study_Hours'], df['Exam_Score'])


# Predict the exam scores for students who studied for 12 hours and 13 hours
def predict_score(hours):
    return slope * hours + intercept


predicted_score_12_hours = predict_score(12)
predicted_score_13_hours = predict_score(13)


print(f"Predicted exam score for a student who studied 12 hours: {predicted_score_12_hours}")
print(f"Predicted exam score for a student who studied 13 hours: {predicted_score_13_hours}")


# Write assertions to validate each step in the process
assert np.isclose(slope, 5.681818181818182), "Incorrect slope value"
assert np.isclose(intercept, 43.63636363636364), "Incorrect intercept value"
assert np.isclose(r_value, 0.9983838545202813), "Incorrect R-value"
assert np.isclose(p_value, 1.877365751484844e-08), "Incorrect p-value"
assert np.isclose(std_err, 0.3434343434343434), "Incorrect standard error value"
assert np.isclose(predicted_score_12_hours, 111.0909090909091), "Incorrect predicted score for 12 hours"
assert np.isclose(predicted_score_13_hours, 116.77272727272728), "Incorrect predicted score for 13 hours"