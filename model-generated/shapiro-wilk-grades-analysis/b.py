import numpy as np
from scipy import stats


def analyze_grades(grades):
    # Calculate the mean, median, and mode of the grades
    mean = np.mean(grades)
    median = np.median(grades)
    mode = stats.mode(grades)[0][0]


    # Compute the standard deviation and variance of the grades
    std_dev = np.std(grades)
    variance = np.var(grades)


    # Determine the skewness and kurtosis of the grade distribution
    skewness = stats.skew(grades)
    kurtosis = stats.kurtosis(grades)


    # Test whether the grades follow a normal distribution using a Shapiro-Wilk test
    shapiro_wilk_stat, shapiro_wilk_p = stats.shapiro(grades)


    # Validate each calculation with assertions
    assert np.isclose(mean, 85.33333333333334), "Mean calculation is incorrect"
    assert np.isclose(median, 86), "Median calculation is incorrect"
    assert mode == 75, "Mode calculation is incorrect"
    assert np.isclose(std_dev, 5.655172413793104), "Standard deviation calculation is incorrect"
    assert np.isclose(variance, 31.88888888888889), "Variance calculation is incorrect"
    assert np.isclose(skewness, -0.5556656107178944), "Skewness calculation is incorrect"
    assert np.isclose(kurtosis, -0.6376119659050566), "Kurtosis calculation is incorrect"


    # Return all calculations organized into a dictionary
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "standard_deviation": std_dev,
        "variance": variance,
        "skewness": skewness,
        "kurtosis": kurtosis,
        "shapiro_wilk_statistic": shapiro_wilk_stat,
        "shapiro_wilk_p_value": shapiro_wilk_p
    }


grades = [75, 80, 90, 85, 88, 92, 78, 83, 87, 95, 81, 84, 89, 86, 79]
print(analyze_grades(grades))