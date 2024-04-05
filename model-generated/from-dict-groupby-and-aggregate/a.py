import pandas as pd


def group_and_aggregate(data, group_by, aggregate_dict):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)


    # Group the data by the given column and aggregate using the given functions
    df_grouped = df.groupby(group_by).agg(aggregate_dict)


    return df_grouped


data = {'Subject': ['Science', 'Math', 'Math', 'LIT', 'Econ', 'History'],
        'Avg_student_scores': [65, 51, 45, 82, 55, 85],
        'Years_of_Experience': [2, 5, 1, 7, 3, 4]}


group_by = 'Subject'
aggregate_dict = {'Avg_student_scores': 'mean', 'Years_of_Experience': 'max'}


df_grouped = group_and_aggregate(data, group_by, aggregate_dict)
print(df_grouped)