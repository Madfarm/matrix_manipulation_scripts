import numpy as np
from scipy import stats


grades = np.array([
    [85, 90, 88, 75],  # Student 1
    [92, 88, 90, 78],  # Student 2
    [78, 85, 80, 82],  # Student 3
    [90, 95, 92, 88],  # Student 4
    [85, 80, 85, 90]   # Student 5
])


# Calculate the mean, median, mode, and standard deviation of each subject's grades.
mean_grades = np.mean(grades, axis=0)
median_grades = np.median(grades, axis=0)
mode_grades = stats.mode(grades, axis=0).mode.flatten()
std_dev_grades = np.std(grades, axis=0)


print("Mean Grades:", mean_grades)
print("Median Grades:", median_grades)
print("Mode Grades:", mode_grades)
print("Standard Deviation Grades:", std_dev_grades)


# Determine the student(s) with the highest and lowest average grade across all subjects.
average_grades = np.mean(grades, axis=1)
highest_average_grade = np.max(average_grades)
lowest_average_grade = np.min(average_grades)


print("Highest Average Grade:", highest_average_grade)
print("Student(s) with Highest Average Grade:", np.where(average_grades == highest_average_grade)[0] + 1)
print("Lowest Average Grade:", lowest_average_grade)
print("Student(s) with Lowest Average Grade:", np.where(average_grades == lowest_average_grade)[0] + 1)


# Calculate the correlation matrix between the subjects.
correlation_matrix = np.corrcoef(grades.T)


print("Correlation Matrix:\n", correlation_matrix)


# Use assertions to validate the calculations and the output.
assert np.allclose(mean_grades, np.array([84., 88.4, 87., 81.8]), atol=0.1)
assert np.allclose(median_grades, np.array([85., 89., 88., 82.]), atol=0.1)
assert np.allclose(mode_grades, np.array([85., 90., 88., 75.]), atol=0.1)
assert np.allclose(std_dev_grades, np.array([5.91607978, 4.94974747, 4.18330013, 6.22111623]), atol=0.1)
assert highest_average_grade == 91.25
assert np.allclose(lowest_average_grade, 82.5, atol=0.1)
assert np.allclose(correlation_matrix, np.array([[ 1.          ,0.47718285,  0.93226905, -0.00720608],
 [ 0.47718285,  1.          ,0.70499854 ,-0.24345405],
 [ 0.93226905,  0.70499854 , 1. ,        -0.04172233],
 [-0.00720608, -0.24345405, -0.04172233,  1.        ]]), atol=0.1)