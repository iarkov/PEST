import pandas as pd
import numpy as np

df = pd.read_html('https://www.educationcounts.govt.nz/data-services/collecting-information/code-sets-and-classifications/country_of_citizenship_codes')
df[-1].columns = ['Code','Country of Citizenship','Comment']
df_cit_codes = df[-1]

for column in df_cit_codes.columns:
    df_cit_codes[column] = df_cit_codes[column].shift(-1)
df_cit_codes = df_cit_codes.drop('Comment',1)
df_cit_codes.dropna(inplace=True)
# df_cit_codes.to_pickle('Citizenship_Codes.pickle')
t = np.where(df_cit_codes.values=='DZA')
print(t[0][0], t[1][0])
