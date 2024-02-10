#Import the pandas library, which provides data structures and data analysis tools for python
import pandas as pd

#Creation of the first dataset using a dictionary
data1 = {
    'work_year':[2023]*20,
    'experience_level': ['EN','MI','SE','EX','EN','MI','SE','EX','EN','MI','SE','EX','EN','MI','SE','EX','EN','MI','SE','EX'],
    'job_titles': ['Data Analyst','Data Analyst','Data Analyst','Data Analyst',
                   'Data Manager','Data Manager','Data Manager','Data Manager',
                   'Data Scientist','Data Scientist','Data Scientist','Data Scientist',
                   'Data Architect','Data Architect','Data Architect','Data Architect',
                   'Data Developer','Data Developer','Data Developer','Data Developer'],
    'salary':[80000, 93000, 15000, 160000, 90000, 115500, 130400, 150000, 145000, 156450, 196760, 220000, 120000, 150000, 180000,
              185000, 69139, 75000, 90000, 144700],
    'salary_currency': ['USD']*20,
    'remote_ratio': [0, 100, 100, 100, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 100, 100, 100, 0],
    'number_of_employee': [2, 5, 4, 5, 3, 2, 1, 1, 5, 4, 2, 6 , 5 , 5, 2, 1, 8, 5, 4, 3]
         }

#Convert the dictionary 'data1' to a pandas DataFrame for easier manipulation and analysis
df1 = pd.DataFrame(data1)

#Creation of the second dataset using a dictionary
data2 = {
    'work_year': [2023]*4,
    'experience_level': ['EN','MI','SE','EX'],
    'job_titles': ['Data Engineer','Data Engineer','Data Engineer','Data Engineer'],
    'salary': [120000, 143000, 155000, 250000],
    'salary_currency': ['USD']*4,
    'remote_ratio': [0]*4,
    'number_of_employee': [5, 4, 2, 1]
}

#Convert the dictionary 'data2' to a pandas DateFrame
df2 = pd.DataFrame(data2)

#Concatenate the two DataFrame, 'df1' and 'df2', into a single DataFrame
#The 'ignore_index=True'ensure that the index is reset and continuous in the resulting DataFrame
final_df = pd.concat([df1, df2], ignore_index=True)

# #Display the combined DataFrame
print(final_df)

#Group the data by 'experience_level' and calculates the average salary for each group
avg_salary_by_experience = final_df.groupby('experience_level')['salary'].mean()

# Display the average salary for each experience level
print(avg_salary_by_experience)

#Iteration through each salary in the DataFrame
#The loop will update the threshold salary with the first salary it finds that is greater than 150000
threshold_salary = 100000
for salary in final_df['salary']:
    if salary > 150000:
        threshold_salary = salary
        break;

#Filter and display jobs with salaries greater than the determined threshold
high_salary_jobs = final_df[final_df['salary'] > threshold_salary]
print(high_salary_jobs)

#Display the threshold salary value
print(threshold_salary)

#Calculate the total number of employees across all job titles
total_employes = final_df['number_of_employee'].sum()
print(f"Total number of employees across all job titles: {total_employes}")

#Identify and print the job titles that are fully remote
remote_jobs = final_df[final_df['remote_ratio'] == 100]['job_titles'].unique()
print(f"Job Titles that are fully remote: {' '.join(remote_jobs)}")

#Replace the job title 'Data Analysis' with 'Data Analytics Manager'in the 'job_title' column
final_df['job_titles'] = final_df['job_titles'].replace('Data Analyst','Data Analytics Manager')

#Display the DataFrame after updating the job titles
print(final_df)

#Check and display the number of missing values for each column in the DataFrame
missing_data = final_df.isnull().sum()
print(missing_data)

#Display unique values for 'experience_level' and 'job_title' column
print(final_df['experience_level'].unique())
print(final_df['job_titles'].unique())

#Display the data type of the 'job_title' column in the DataFrame
print(final_df['job_titles'].dtypes)