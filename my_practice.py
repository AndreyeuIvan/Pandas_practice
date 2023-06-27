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
