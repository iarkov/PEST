import pandas as pd
import quandl
import numpy as np

# df_cit_codes = pd.read_pickle("C_C.pickle")
#
# main_df = pd.DataFrame()
#
# for abbv in df_cit_codes['Code']:
#     try:
#         df = quandl.get("WWDI/"+str(abbv)+"_SL_UEM_TOTL_ZS", authtoken="QnBdjmbzJ7NxzD-FKSth",start_date="1998-12-31")
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
#         df = pd.DataFrame(df.values, index=arrays,columns=['Unemployment rate of total labor force, %'])
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
#
# main_df.to_pickle('Unemployment rates.pickle')

df = pd.read_pickle('Unemployment rates.pickle')
pattern_df = pd.read_pickle('Pattern Data Frame.pickle')
main_df = pattern_df.join(df, how = 'left')

main_df.to_pickle('Unemployment rates.pickle')
