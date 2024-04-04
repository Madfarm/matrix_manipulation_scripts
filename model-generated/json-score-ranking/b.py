import pandas as pd
import json


# Data about students
student_details = {'Name':['Raj', 'Raj', 'Raj', 'Aravind', 'Aravind', 'Aravind', 
                             'John', 'John', 'John', 'Arjun', 'Arjun', 'Arjun'], 
                   'Subject':['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics', 
                             'Chemistry', 'Maths', 'Physics', 'Chemistry', 'Maths', 
                                                           'Physics', 'Chemistry'], 
                   'Marks':[80, 90, 75, 60, 40, 60, 80, 55, 100, 90, 75, 70] 
               }


# Create a DataFrame
df = pd.DataFrame(student_details)


# Group by 'Name' and find the maximum 'Marks'
df_ranked = df.loc[df.groupby('Name')['Marks'].idxmax()]


# Reset the index
df_ranked = df_ranked.reset_index(drop=True)


# Rank the students based on 'Marks'
df_ranked['Rank'] = df_ranked['Marks'].rank(method='dense', ascending=False)


# Convert the DataFrame to JSON
json_data = df_ranked.to_json(orient='records')


# Print the JSON data
print(json.dumps(json.loads(json_data), indent=4))