# import pandas as pd

# df=pd.read_csv("C:/Users/hp/Downloads/customers-100.csv")
# print(df.head())
# print(df.info())
# print(df.describe())

#inner join
import pandas as pd

dept_df = pd.DataFrame({
    'dept_id': [1, 2, 3],
    'dept_name': ['HR', 'IT', 'Finance']
})

emp_df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'dept_id': [1, 2, 3]
})  

merged = pd.merge(emp_df, dept_df, on='dept_id', how='inner')
print(merged)


dept_df = pd.DataFrame({
    'dept_id': [1, 2, 4],
    'dept_name': ['HR', 'IT', 'Finance']
})

emp_df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'dept_id': [1, 2, 3]
})   

left_join=pd.merge(dept_df, emp_df, on='dept_id', how="left")
right_join=pd.merge(dept_df, emp_df, on='dept_id', how="right")
outer_join=pd.merge(dept_df, emp_df, on='dept_id', how="outer")
print(outer_join)

#Joins using indexing 
df4=emp_df.set_index("dept_id")
df5=dept_df.set_index("dept_id")
join_index=df5.join(df4, how='inner') 
print(join_index)

#joins on columns names
import pandas as pd
dept_df = pd.DataFrame({
    'dept_id': [1, 2, 3],
    'dept_name': ['HR', 'IT', 'Finance']
})

emp_df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'emp_id': [1, 2, 3]
})   
merged=pd.merge(dept_df, emp_df, left_on="dept_id", right_on="emp_id", how="inner")
print(merged)

# all colums from df2, and only thos columns from df1 that are not present in df2 dynamically?

# import pandas as pd

# df1=pd.DataFrame(
#     {
#         "A":[1,2],
#         "B":[3,4],
#         "C":[5,6]

#     }
# )

# df2=pd.DataFrame(
#     {
#         "B":[7,8],
#         "D":[9,10]
        
#     }
# )


# unuque_cols_df1=[col for col in df1.columns if col not in df2.columns]

# df3=pd.concat([df2,df1[unuque_cols_df1]], axis=1)
# print(df3)

df1 = pd.DataFrame({'user_id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'user_id': [1, 2, 4], 'salary': [50000, 60000, 70000]})

merged_df = pd.merge(df1, df2, on='user_id')
print(merged_df)

data = {
    "emp_id": [101, 102, 103, 104, 105],
    "name": ["Ravi", "Priya", "Kumar", "Ravi", "Sita"],
    "department": ["IT", "HR", "IT", "Finance", "HR"],
    "salary": [60000, 50000, 75000, 60000, 45000],
    "experience": [4, 3, 6, 4, 2]
}

df = pd.DataFrame(data)

print(df)

#Find the second-highest salary
second_highest=df["salary"].drop_duplicates().nlargest(2).iloc[-1]
print(second_highest)

#Find duplicate employee records
duplicates = df[df.duplicated(subset=['name'], keep=False)]
print(duplicates)

#firt duplicate record
df_unique = df.drop_duplicates(subset=["name"], keep="first")
print(df_unique)