import pandas as pd


def rank_columns(df):
    # Get the column names and sort them alphabetically
    columns = sorted(df.columns)


    # Rank the columns based on their order
    ranks = {column: i+1 for i, column in enumerate(columns)}


    # Add the ranks as a new column in the data frame
    df['Rank'] = df.apply(lambda row: ranks[row.name], axis=1)


    return df


# Create a data frame from the given data
student_details = {'Name':['Raj', 'Raj', 'Raj', 'Aravind', 'Aravind', 'Aravind', 
                           'John', 'John', 'John', 'Arjun', 'Arjun', 'Arjun'], 
                   'Subject':['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics', 
                             'Chemistry', 'Maths', 'Physics', 'Chemistry', 'Maths', 
                                                           'Physics', 'Chemistry'], 
                   'Marks':[80, 90, 75, 60, 40, 60, 80, 55, 100, 90, 75, 70] 
               }
df = pd.DataFrame(student_details)


# Call the function to rank the columns
df = rank_columns(df)


# Print the resulting data frame
print(df)