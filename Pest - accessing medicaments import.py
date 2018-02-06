import pandas as pd
import numpy as np
import quandl
import math

df_cit_codes = pd.read_pickle("C_C.pickle")

# main_df = pd.DataFrame()
#
# for abbv in df_cit_codes['Code']:
#     try:
#         df = quandl.get("UCOM/PHAR_"+str(abbv), authtoken="QnBdjmbzJ7NxzD-FKSth", start_date="1998-12-31")
#         df = df['Medicaments nes; formulated; in bulk - Import - Trade (USD)']
#     except BaseException:
#         continue
#     try:
#         date_array = np.array(df.index)
#         abbv_array = []
#         for date in df.index:
#             abbv_array.append(str(abbv))
#         abbv_array = np.array(abbv_array)
#
#         arrays = [abbv_array,date_array]
#         df = pd.DataFrame(df.values, index=arrays,columns=['Medicaments Import (USD)'])
#         # abbv_loc = np.where(df_cit_codes.values==str(abbv))
#         # country_name = str(df_cit_codes.iloc[abbv_loc[0][0],abbv_loc[1][0]+1])
#         # df = df.rename(columns={'Value':'Unemployment rate of total labor force, % - '+country_name})
#     except BaseException:
#         continue
#     try:
#         if main_df.empty:
#             main_df = df
#         else:
#             main_df = main_df.append(df)
#     except BaseException:
#         continue
# main_df.to_pickle('Medicaments Import (USD).pickle')

# df = pd.read_pickle('Medicaments Import (USD).pickle')
# df_cit_codes = df_cit_codes['Code']
#
# date_range = pd.date_range('19981231','20161231', freq = 'A')
# date_range_list = []
# for i in df_cit_codes:
#     for j in date_range:
#         date_range_list.append(j)
# date_range_array = np.array(date_range_list)
# abbv_list = []
# for i in df_cit_codes:
#     for j in date_range:
#         abbv_list.append(i)
# abbv_array = np.array(abbv_list)
#
# df_pattern = pd.DataFrame(index = [abbv_array,date_range_array])
# main_df = df_pattern.join(df, how='left')
# print(main_df)
# main_df.to_pickle('Medicaments Import (USD).pickle')
# df_pattern.to_pickle('Pattern Data Frame.pickle')

df = pd.read_pickle('Medicaments Import (USD).pickle')

for index in df.index.levels[0]:
    df.loc[index].fillna(method='ffill',inplace = True)
    df.loc[index].fillna(method='bfill',inplace = True)

df.to_pickle('Medicaments Import (USD).pickle')
