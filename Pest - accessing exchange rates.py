import pandas as pd
import quandl
import numpy as np
import math
from datetime import datetime

# df_cit_codes = pd.read_pickle("C_C.pickle")
#
# main_df = pd.DataFrame()
#
# for abbv in df_cit_codes['Code']:
#     try:
#         df = quandl.get("WWDI/"+str(abbv)+"_PA_NUS_FCRF", authtoken="QnBdjmbzJ7NxzD-FKSth",start_date="1998-12-31")
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
#         df = pd.DataFrame(df.values, index=arrays,columns=['Exchange rate (LCU per US$)'])
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
# main_df.to_pickle('Exchange_rates.pickle')

# df = pd.read_pickle('Exchange_rates.pickle')
# pattern_df = pd.read_pickle('Pattern Data Frame.pickle')
# main_df = pattern_df.join(df, how = 'left')
# main_df.to_pickle('Exchange_rates.pickle')


df = pd.read_pickle('Exchange_rates.pickle')

# df_eu_list = pd.read_html('https://europa.eu/european-union/about-eu/countries_en#tab-0-1')
# df_eu_list = df_eu_list[1]
# df_eu_list.columns = [x for x in df_eu_list.loc[0]]
# for col in df_eu_list.columns:
#     df_eu_list[col] = df_eu_list[col].shift(-1)
# df_eu_list.dropna(how='all', inplace=True)
df_eu_list= pd.read_pickle('EU_countries.pickle')
df_cit_codes = pd.read_pickle('C_C.pickle')
df_cit_codes.rename(columns={'Country of Citizenship':'Countries'}, inplace=True)
df_eu_list = pd.merge(df_eu_list, df_cit_codes, how='left')
df_eu_list = df_eu_list['Code']

eu_exc = quandl.get("WWDI/EMU_PA_NUS_FCRF", authtoken="QnBdjmbzJ7NxzD-FKSth", start_date="1998-12-31")

eu_exc.loc[datetime(year=2016, month=12, day=31)] = None
eu_exc.loc[datetime(year=1998, month=12, day=31)] = None
eu_exc.sort_index(axis=0, ascending=True, inplace = True)
eu_exc.fillna(method='ffill', inplace=True)
eu_exc.fillna(method='bfill', inplace=True)

eu_list = df_eu_list.tolist()

index_a = []
date_a = []
for index in eu_list:
    for date in df.index.levels[1]:
        index_a.append(index)
for index in eu_list:
    for date in df.index.levels[1]:
        date_a.append(date)
index_a = np.array(index_a)
date_a = np.array(date_a)

values_list = []
for index_0 in eu_list:
    values = []
    i = 0
    for index_1 in eu_exc.index:
        if math.isnan(df.loc[index_0].loc[index_1].values[0]):
            break
        a = np.float(df.loc[index_0].loc[index_1].values[0])
        values.append(a)
        i += 1
    for number in range(i, len(eu_exc.index)):
        a = eu_exc.iloc[number,0]
        values.append(a)
    for value in values:
        values_list.append(value)
arrays = [index_a, date_a]

df_eu_countries_rates = pd.DataFrame(values_list, index = arrays, columns = [df.columns[0]])

for index_0 in df.index.levels[0]:
    for index_1 in df_eu_countries_rates.index.levels[0]:
        if index_0 == index_1:
            df.drop(index_0, 0, inplace = True)
df = df.append(df_eu_countries_rates)
for index_0 in df.index.levels[0]:
    print(index_0)
    print(df.loc[index_0])
