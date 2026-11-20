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


import pandas as pd
#joines using merge function
emp_df = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "emp_name": ["John", "David", "Smith", "Peter"],
    "dept_id": [101, 102, 103, 104]
})

dept_df = pd.DataFrame({
    "dept_id": [101, 102, 103, 105],
    "dept_name": ["Python", "Java", "AWS", "DevOps"]
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


import pandas as pd

df = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": ["John", "Alice", "Bob", "David", "Sam", "Mike", "Sara", "Tom"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "IT"],
    "salary": [50000, 70000, 60000, 80000, 70000, 90000, 85000, 60000],
    "experience": [2, 5, 3, 8, 4, 10, 6, 3],
    "city": ["Chennai", "Bangalore", "Chennai", "Hyderabad",
             "Bangalore", "Chennai", "Hyderabad", "Chennai"]
})


"""1. Display the first 5 employee records.
2. Find the total number of employees.
3. Find employees whose salary is greater than 60000.
4. Find employees working in the IT department.
5. Display only name, salary, and department columns.
6. Sort employees by salary in descending order.
7. Find the average salary of all employees.
8. Find the maximum and minimum salary.
9. Find employees with more than 5 years of experience.
10. Count employees in each department.

Find the second-highest salary.

Find the third-highest unique salary.

Find the highest-paid employee in each department.

Find the average salary department-wise.

Find employees earning more than their department's average salary.

Find duplicate employee records.

Remove duplicate employee records based on emp_id.

Find the department with the highest average salary.

Find the top 2 highest-paid employees in each department.

Find employees whose salary is between 50000 and 80000.

Find employees who belong to Chennai or Bangalore.

Find the number of employees in each city.

Find employees whose names start with S.
Replace missing salary values with the department's average salary.
Find the percentage contribution of each department to total salary expenditure.

1	Find the highest salary in each department	groupby()
2	Find the top 2 employees per department	nlargest()
3	Calculate department-wise salary ranking	rank()
4	Find the second-highest salary per department	groupby() + rank()
5	Find employees earning above company average	Boolean filtering
6	Find employees with duplicate email IDs	duplicated()
7	Merge employee and department datasets	merge()
8	Find employees without a matching department	Left join
9	Calculate cumulative salary by department	cumsum()
10	Find the difference between employee salary and department average	transform()
11	Calculate monthly hiring trends	groupby() + dates
12	Find missing values column-wise	isnull()
13	Convert categorical department names into numeric values	map() / encoding
14	Find the top 3 departments based on total salary	Aggregation
15	Identify salary outliers using IQR"""