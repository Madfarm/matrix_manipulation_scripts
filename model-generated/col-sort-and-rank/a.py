import pandas as pd


def rank_columns(df):
    # Get the column names and sort them alphabetically
    cols = sorted(df.columns)


    # Rank the columns based on their order
    ranks = list(range(1, len(cols)+1))


    # Create a new data frame with the ranks as a column
    df_ranks = pd.DataFrame({'Column': cols, 'Rank': ranks})


    return df_ranks


# Create a data frame from the given data
student_details = {'Name':['Raj', 'Raj', 'Raj', 'Aravind', 'Aravind', 'Aravind', 
                           'John', 'John', 'John', 'Arjun', 'Arjun', 'Arjun'], 
                   'Subject':['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics', 
                             'Chemistry', 'Maths', 'Physics', 'Chemistry', 'Maths', 
                                                           'Physics', 'Chemistry'], 
                   'Marks':[80, 90, 75, 60, 40, 60, 80, 55, 100, 90, 75, 70] 
               }
df = pd.DataFrame(student_details)


# Call the function and print the result
print(rank_columns(df))