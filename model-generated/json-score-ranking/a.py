import pandas as pd
import json


student_details = {'Name':['Raj', 'Raj', 'Raj', 'Aravind', 'Aravind', 'Aravind', 
                           'John', 'John', 'John', 'Arjun', 'Arjun', 'Arjun'], 
                   'Subject':['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics', 
                             'Chemistry', 'Maths', 'Physics', 'Chemistry', 'Maths', 
                                                           'Physics', 'Chemistry'], 
                   'Marks':[80, 90, 75, 60, 40, 60, 80, 55, 100, 90, 75, 70] 
               }


# Create a DataFrame
df = pd.DataFrame(student_details)


# Rank the students based on the highest score they've received
df = df.loc[df.groupby('Name')['Marks'].idxmax()]


# Convert the DataFrame to JSON
json_data = df.to_json(orient='records')


# Print the JSON data
print(json.dumps(json.loads(json_data), indent=4))