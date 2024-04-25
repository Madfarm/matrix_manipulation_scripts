import pandas as pd
from scipy.stats import linregress


# Step 1: Load the dataset into a Pandas DataFrame
data = {
    "Student_ID": range(1, 11),
    "Study_Hours": range(2, 12),
    "Exam_Score": [65, 75, 80, 85, 90, 92, 95, 98, 100, 102]
}
df = pd.DataFrame(data)


# Step 2: Perform exploratory data analysis (EDA) to understand the structure and characteristics of the dataset
print("DataFrame Shape:", df.shape)
print("DataFrame Columns:", df.columns)
print("DataFrame Head:", df.head())
print("DataFrame Info:", df.info())
print("DataFrame Describe:", df.describe())


# Step 3: Use linear regression from SciPy to fit a regression line to the data
slope, intercept, r_value, p_value, std_err = linregress(df["Study_Hours"], df["Exam_Score"])


# Step 4: Predict the exam scores for students who studied for 12 hours and 13 hours
predicted_score_12hrs = slope * 12 + intercept
predicted_score_13hrs = slope * 13 + intercept


# Validate the predicted scores
assert predicted_score_12hrs == 109.2
assert predicted_score_13hrs == 113.01818181818183


# Assertions to validate each step in the process
assert df.shape == (10, 3), "DataFrame shape is not as expected"
assert list(df.columns) == ["Student_ID", "Study_Hours", "Exam_Score"], "DataFrame columns are not as expected"
assert df.info() == None, "DataFrame info is not as expected"
assert df.describe().shape == (8, 3), "DataFrame describe is not as expected"
assert slope > 0, "Slope is not positive"
assert predicted_score_12hrs > 0, "Predicted score for 12 hours is not positive"
assert predicted_score_13hrs > 0, "Predicted score for 13 hours is not positive"