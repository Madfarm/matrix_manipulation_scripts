import pandas as pd


def convert_dict_to_df(data):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)


    return df


def group_and_aggregate(df, group_by, agg_func):
    # Group the DataFrame by the given column and aggregate the data using the given function
    grouped_df = df.groupby(group_by).agg(agg_func)


    return grouped_df


def main():
    data = {'Subject': ['Science', 'Math', 'Math', 'LIT', 'Econ', 'History'],
            'Avg_student_scores': [65, 51, 45, 82, 55, 85],
            'Years_of_Experience': [2, 5, 1, 7, 3, 4]}


    # Convert the dictionary to a DataFrame
    df = convert_dict_to_df(data)


    # Group the DataFrame by 'Subject' and aggregate 'Avg_student_scores' using 'mean' and 'Years_of_Experience' using 'max'
    grouped_df = group_and_aggregate(df, 'Subject', {'Avg_student_scores': 'mean', 'Years_of_Experience': 'max'})


    print(grouped_df)


if __name__ == "__main__":
    main()