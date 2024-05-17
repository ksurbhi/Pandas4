import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.drop_duplicates('salary')
    if len(df) < 2:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    else:
        df = df.sort_values('salary', ascending = False).head(2).tail(1)[['salary']]
        return df.rename(columns = {'salary' : 'SecondHighestSalary'})
    
