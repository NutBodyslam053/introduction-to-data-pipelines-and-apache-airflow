"""xxx"""

import pandas as pd

df = pd.read_csv('titanic.csv')

dq_list = []
for col in ['Age', 'Cabin', 'Embarked']:
    dq = sum(df[col].notnull()) / len(df[col])
    dq_list.append(dq)
    print(f'Data Quality of {col}: {dq}')
    print('-'*50)

print(f'Completeness: {sum(dq_list)/3}')
