import pandas as pd
import numpy as np
from Test import join_empty_frame
# df_med_imp = pd.read_pickle('Medicaments Import (USD).pickle')
#
# df_gdp = pd.read_pickle('GDP.pickle')
# df_exc_rates = pd.read_pickle('Exchange_rates.pickle')
# df_unem = pd.read_pickle('Unemployment rates.pickle')
# df_import_tax = pd.read_pickle('Import taxes.pickle')
#
# joined = df_med_imp.join(df_gdp, how='inner')
# joined = joined.join(df_exc_rates, how='inner')
# joined = joined.join(df_unem, how='inner')
# joined = joined.join(df_import_tax, how='inner')
#
#
# for index_0 in joined.index.levels[0]:
#     boolean = False
#     for column in joined.columns:
#         a = joined.loc[index_0][column].isnull().values.sum()
#         if a > 4:
#             boolean = True
#         if boolean:
#             break
#     if boolean:
#         joined = joined.reset_index().set_index('level_0')
#         for index in joined.index:
#             if index == index_0:
#                 joined.drop(index, 0, inplace=True)
#         joined = joined.reset_index().set_index(['level_0', 'level_1'])
#
# joined.index.rename([None, None], level=[0,1], inplace=True)
#
# for index_0 in joined.index.levels[0]:
#     for column in joined.columns:
#         joined.loc[index_0][column].fillna(method='bfill', inplace=True)
#         joined.loc[index_0][column].fillna(method='ffill', inplace=True)
# joined.rename(columns={'GDP': 'GDP(LCU)'}, inplace=True)
# joined.to_pickle('Joined_Economic_Data.pickle')
# joined.to_excel('joined.xlsx')

# df_e = pd.read_pickle('Joined_Economic_Data.pickle')
# df_je = pd.read_pickle('Joined_Empty_Dataframes.pickle')
#
# index = df_e.index.join(df_je.index, how='right', level=0)
# df_for_join = pd.DataFrame(None, index = index, columns=None)
# df_e = df_e.join(df_for_join, how = 'right')
# df_e.to_pickle('Joined_Economic_Data.pickle')

# df = pd.read_pickle('Joined_Economic_Data.pickle')
# df  = join_empty_frame(df)
# print(df)
# print(len(df.index.levels[0].tolist()))
# df.to_pickle('Joined_Economic_Data.pickle')

df = pd.read_pickle('D:\Python\Python Diploma\pickles and excels\Joined_Economic_Data.pickle')
# for column in df.columns:
#     if True not in df[column].isnull().tolist():
#         print('lol')
#     else:
#         print('kek')


df = df.loc[['CAN','HRV','SLV','GMB','MEX'],:]
df.to_excel('D:\Python\Python Diploma\pickles and excels\E_top5.xlsx')
