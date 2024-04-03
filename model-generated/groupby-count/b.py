import pandas as pd


df = pd.DataFrame({
'book_name':['Book1','Book2','Book3','Book4','Book1','Book2','Book3','Book5'],
'book_type':['Math','Physics','Computer','Science','Math','Physics','Computer','English'],
'book_id':[1,2,3,4,1,2,3,5]})


# Group by 'book_name' and create a new column 'book_count'
df['book_count'] = df.groupby('book_name')['book_name'].transform('count')


print(df)