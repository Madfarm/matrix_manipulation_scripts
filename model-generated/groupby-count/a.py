import pandas as pd


# Create a DataFrame
df = pd.DataFrame({
    'book_name':['Book1','Book2','Book3','Book4','Book1','Book2','Book3','Book5'],
    'book_type':['Math','Physics','Computer','Science','Math','Physics','Computer','English'],
    'book_id':[1,2,3,4,1,2,3,5]
})


# Group by 'book_name' and create a new column 'count'
df['count'] = df.groupby('book_name')['book_name'].transform('count')


# Print the updated DataFrame
print(df)