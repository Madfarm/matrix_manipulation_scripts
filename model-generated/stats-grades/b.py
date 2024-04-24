import numpy as np
from scipy import stats


def analyze_grades(grades):
    # Calculate the mean, median, mode, and standard deviation of each subject's grades
    means = np.mean(grades, axis=0)
    medians = np.median(grades, axis=0)
    modes = stats.mode(grades, axis=0).mode[0]
    std_devs = np.std(grades, axis=0)


    # Determine the student(s) with the highest and lowest average grade across all subjects
    avg_grades = np.mean(grades, axis=1)
    max_avg_grade = np.max(avg_grades)
    min_avg_grade = np.min(avg_grades)
    max_avg_students = np.where(avg_grades == max_avg_grade)[0] + 1
    min_avg_students = np.where(avg_grades == min_avg_grade)[0] + 1


    # Calculate the correlation matrix between the subjects
    corr_matrix = np.corrcoef(grades.T)


    return means, medians, modes, std_devs, max_avg_students, min_avg_students, corr_matrix


# Test the function
grades = np.array([
    [85, 90, 88, 75],  # Student 1
    [92, 88, 90, 78],  # Student 2
    [78, 85, 80, 82],  # Student 3
    [90, 95, 92, 88],  # Student 4
    [85, 80, 85, 90]   # Student 5
])


means, medians, modes, std_devs, max_avg_students, min_avg_students, corr_matrix = analyze_grades(grades)


# Validate the calculations and output
assert np.allclose(means, [86, 87.6, 87, 82.6])
assert np.allclose(medians, [85, 88, 88, 82])
assert np.allclose(modes, [85, 80, 80, 75])
assert np.allclose(std_devs, [4.85798312, 5.0039984,  4.19523539, 5.71314274])
assert np.allclose(max_avg_students, [4])
assert np.allclose(min_avg_students, [3])
assert np.allclose(corr_matrix, [[ 1. ,         0.47718285 , 0.93226905, -0.00720608],
 [ 0.47718285,  1. ,         0.70499854, -0.24345405],
 [ 0.93226905 , 0.70499854,  1.    ,     -0.04172233],
 [-0.00720608, -0.24345405, -0.04172233  ,1.        ]])
