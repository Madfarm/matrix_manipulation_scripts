import numpy as np
from scipy import stats


def analyze_grades(grades):
    # Calculate mean
    mean = np.mean(grades)
    assert np.isclose(mean, 84.8), f"Mean is incorrect: {mean}"


    # Calculate median
    median = np.median(grades)
    assert np.isclose(median, 85.0), f"Median is incorrect: {median}"


    # Calculate mode
    mode = stats.mode(grades)[0][0]
    assert mode == 75, f"Mode is incorrect: {mode}"


    # Calculate standard deviation
    std_dev = np.std(grades)
    assert np.isclose(std_dev, 5.3814496188294845), f"Standard deviation is incorrect: {std_dev}"


    # Calculate variance
    variance = np.var(grades)
    assert np.isclose(variance, 28.960000000000004), f"Variance is incorrect: {variance}"


    # Calculate skewness
    skewness = stats.skew(grades)
    assert np.isclose(skewness, 0.030696816260761626), f"Skewness is incorrect: {skewness}"


    # Calculate kurtosis
    kurtosis = stats.kurtosis(grades)
    assert np.isclose(kurtosis, -0.7799975580720986), f"Kurtosis is incorrect: {kurtosis}"


    # Perform Shapiro-Wilk test
    shapiro_stat, shapiro_p = stats.shapiro(grades)
    assert np.isclose(shapiro_stat, 0.9911456108093262), f"Shapiro statistic is incorrect: {shapiro_stat}"
    assert np.isclose(shapiro_p, 0.999754011631012), f"Shapiro p-value is incorrect: {shapiro_p}"


    return {
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Standard Deviation": std_dev,
        "Variance": variance,
        "Skewness": skewness,
        "Kurtosis": kurtosis,
        "Shapiro Statistic": shapiro_stat,
        "Shapiro p-value": shapiro_p
    }


grades = [75, 80, 90, 85, 88, 92, 78, 83, 87, 95, 81, 84, 89, 86, 79]
print(analyze_grades(grades))