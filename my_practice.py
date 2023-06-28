import pandas as pd


series = pd.Series(
    [x for x in range(1,6)],
     index = ['row_1', 'row_2', 'row_3', 'row_4', 'row_5'],
     name = 'my_list_comp'
)

#creating DataFrames

df = pd.DataFrame({x:x^2 for x in range(1,6)})

#indexed

ind = pd.Index(['a', 'b', 'c', 'd', 'e'])

#indexes & columns

cols = df.columns
ind = df.index 

# indexe with dicts
dict_in = {'col_1': [1, 2, 3, 4, 5],
           'col_2': [1, 2, 3, 4, 5],
           'col_3': [1, 2, 3, 4, 5]}
df = pd.DataFrame(dict_in)
df.index = ['row_1', 'row_2', 'row_3', 'row_4', 'row_5']

# unique indexes
unique_ind = df.index.unique()
unique_cols = df.columns.unique()

# rename columns

new_df = df.rename(columns={'col_2':'new_col_2', 'col_3':'new_col_3'})

# make_indexes

new_df = df.set_index(['data'])

new_df = df.set_index(['data', 'age']) # double index

# change_indexes from columns

df.set_index(df['data'], inplace=True)

# series vs df

series = df['name']
df_1 = df[['name']]

df[ "new_col" ] = df["age"] # change columns value

# Multiindexes

arr = [['a', 's', 'd', 'f'], [1, 2, 3, 4]]
int = pd.MultiIndex.from_arrays(arr)

# filtering df ! It is better to use query() also @ is used for assigning element

new_df = df[(df['стаж работы'] > 4) & (df['зарплата'] < 95000)] 

new_df = df.query('`стаж работы` <= 4')

new_df = df.query('not `год рождения` > 91 or `зарплата` > 70000')

# working with na

new_df = df.dropna(how='any') # any for 1 or more Na in a row(axis=0) or column(axis=1)
new_df = df.dropna(subset=['name', 'age']) # sub set stands for coluns, what we are working with/ axis=1 stand for row, subset[1]
new_df = df.dropna(subset=[2, 3, 7], axis=1) # on indexes

df.fillna(value=
    {
    'name': 'No_name',
    'count': 10
    },
    inplace = True
)
# for providing columns and rows we are using k:v pair, as column(k) and row(v)

# isna()

new_df = df[df['name'].isna()]

new_df = df[~ df['name'].isna() & (df['count'] <= 5)]
