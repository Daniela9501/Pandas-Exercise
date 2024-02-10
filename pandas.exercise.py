import pandas as pd
import numpy as np

series = pd.Series([1,3,5,7,9])
print("series:\n", series)

data = {'Name':['Alice', 'Bob','Charlie'],'Age':[25,30,35]}
df = pd.DataFrame(data)
print("\n DataFrame:\n", df)

ages = df['Age']
print("\n Ages column: \n", ages)

adults = df[df['Age']>=30]
print("\n Adults: \n", adults)

df2 = pd.DataFrame({'Name':['Dave','Eve'], 'Age':[40,22]})
combined_df = pd.concat([df, df2], ignore_index=True)
print("\nCombined DataFrame:\n", combined_df)

sales_data = {
    'Salesperson':['Alice','Bob','Alice','Bob'],
    'Sales': [200, 150, 300, 100]
}

sales_df = pd.DataFrame(sales_data)

grouped_sales = sales_df.groupby('Salesperson').sum()
print("\nGrouped Sales:\n", grouped_sales)

pivot = sales_df.pivot_table(values = 'Sales', index = 'Salesperson', aggfunc='sum')
print("\n Pivot Table:\n", pivot)

dates = pd.date_range('20230101', periods = 6)
time_df = pd.DataFrame(np.random.randn(6,4),index=dates, columns = list('ABCD'))
print("\n Time Series DataFrame: \n", time_df)

print("\nDataFrame with missing values: \n", df)
df_filled = df.fillna(value = 0)
print("\n DataFrame after filling Missing Values\n",df_filled)
