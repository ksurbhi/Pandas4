import pandas as pd
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee.drop_duplicates(subset = 'salary')
    if len(df) < N or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    else:
        df = df.sort_values(by='salary', ascending = False)
        df = df.head(N).tail(1)[['salary']]
        return df.rename(columns = {'salary' : f'getNthHighestSalary({N})'})
      
# Using set with time complexity of O(1) for checking duplicates
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    result_set = set()
    for i in range(len(employee)):
        salary= employee['salary'][i]
        result_set.add(salary)
    result = []
    for ele in result_set:
        result.append(ele)
    result.sort(reverse = True)
    if len(result) < N or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})':[result[N-1]]})
      
# Using longest solution with extra time complexity of O(n) for checking duplicates
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    result = []
    for i in range(len(employee)):
        salary = employee['salary'][i]
        if salary not in result:
            result.append(salary)
    result.sort(reverse = True)
    if len(result)< N or N<=0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': [result[N-1]]})
