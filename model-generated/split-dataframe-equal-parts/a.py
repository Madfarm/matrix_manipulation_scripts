import pandas as pd


df = pd.DataFrame([["A", 1], ["B", 2], ["C", 3], ["D", 4]], 
                  columns=["col_A", "col_B"])


def split_df(df, parts):
    # Calculate the size of each part
    size = len(df) // parts


    # Split the DataFrame into parts
    dfs = []
    for i in range(parts):
        start = i * size
        end = (i + 1) * size if i < parts - 1 else len(df)
        dfs.append(df.iloc[start:end])


    return dfs


# Split the DataFrame into 2 parts
df_parts = split_df(df, 2)


# Print each part
for i, part in enumerate(df_parts):
    print(f"Part {i+1}:")
    print(part)
    print()