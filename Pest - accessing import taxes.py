import pandas as pd
import numpy as np
from datetime import datetime
import math

# # reading data from exce;
# main_df = pd.read_excel('DataExport_21_11_2017__10_0_13.xls')
#
# # formatting data
# main_df = main_df[['Source: Integrated Database (IDB) notifications.','Unnamed: 1','Unnamed: 8']]
# main_df.columns = ['Reporter','Year','Average of AV Duties']
# for column in main_df.columns:
#     main_df[column] = main_df[column].shift(-4)
# main_df.dropna(inplace=True)
# main_df.drop_duplicates(inplace=True)
#
# main_df.set_index(main_df['Year'], inplace=True)
# main_df = main_df.rename_axis(None)
# for index, row in main_df.iterrows():
#     if index == 2017:
#         main_df = main_df.drop(row,0)
# index_list = main_df['Year'].tolist()
# date_list = []
# for item in index_list:
#     date = datetime(year=int(item), month=12, day=31)
#     date_list.append(date)
# main_df.index=date_list
#
# main_df = main_df.drop(['Year'],1)
#
# # merging data
# df_cit_codes = pd.read_pickle('C_C.pickle')
# df_cit_codes.rename(columns={'Country of Citizenship':'Reporter'}, inplace=True)
#
# merged = pd.merge(main_df, df_cit_codes, how = 'left')
# abbv_array = np.array(merged['Code'].tolist())
# date_array = np.array(date_list)
# arrays = [abbv_array, date_array]
# df_import_tax = pd.DataFrame(merged.values, index=arrays, columns = merged.columns)
# df_import_tax = df_import_tax.drop(['Code'],1)
# # reading EU data
# df_eu_list = pd.read_html('https://europa.eu/european-union/about-eu/countries_en#tab-0-1')
# df_eu_list = df_eu_list[1]
#
# df_eu_list.columns = [x for x in df_eu_list.loc[0]]
# for col in df_eu_list.columns:
#     df_eu_list[col] = df_eu_list[col].shift(-1)
# df_eu_list.dropna(how='all', inplace=True)
# df_eu_list['Year of entry'].fillna(method='ffill',inplace=True)
#
# # merging EU data with index
# df_cit_codes.rename(columns={'Reporter':'Countries'}, inplace=True)
# merged_eu = pd.merge(df_eu_list, df_cit_codes, how='left')
#
# eu_date_list = []
# for i in merged_eu.index:
#     date = merged_eu.loc[i,'Year of entry']
#     date = datetime(year = int(date[6:]), month=int(date[3:5]), day=int(date[0:2]))
#     eu_date_list.append(date)
#
# merged_eu['Year of entry'] = eu_date_list
#
# eu_abbv_array = np.array(merged_eu['Code'])
# eu_date_array = np.array(eu_date_list)
# eu_arrays = [eu_date_array, eu_abbv_array]
# merged_eu = pd.DataFrame(merged_eu.values, index = eu_arrays, columns = merged_eu.columns)
# merged_eu.drop(['Code', 'Year of entry'],1,inplace=True)
#
# # creating table for EU contries
# date_min = datetime(year=1998, month=12, day=31)
# EU_taxes = main_df[main_df.Reporter=='European Union']
# EU_taxes = EU_taxes[EU_taxes.index >= date_min]
# EU_taxes.drop(['Reporter'],1,inplace=True)
# EU_taxes.sort_index(axis=0, ascending=True,inplace=True)
#
#
# eu_taxes_date_range = pd.date_range('19981231', periods=19, freq='A')
# eu_taxes_abbv_list = merged_eu.index.levels[1]
# eu_taxes_date_array = []
# for i in eu_taxes_abbv_list:
#     for item in eu_taxes_date_range:
#         eu_taxes_date_array.append(item)
# eu_taxes_date_array = np.array(eu_taxes_date_array)
#
# eu_taxes_abbv_array = []
# for item in eu_taxes_abbv_list:
#     for i in range(len(eu_taxes_date_range)):
#         eu_taxes_abbv_array.append(item)
# eu_taxes_abbv_array=np.array(eu_taxes_abbv_array)
# eu_taxes_arrays = [eu_taxes_abbv_array, eu_taxes_date_array]
#
# df_eu_countries_taxes = pd.DataFrame(index = eu_taxes_arrays)
#
#
# df_eu_countries_taxes = pd.merge(df_eu_countries_taxes.reset_index(), df_import_tax['Average of AV Duties'].reset_index(), on=['level_0','level_1'],
#                                     how='left').set_index(['level_0','level_1'])
#
# df_eu_countries_taxes.index.rename([None, None], level=[0,1], inplace=True)
# for index_0 in df_eu_countries_taxes.index.levels[0]:
#     for index_1 in reversed(EU_taxes.index):
#         if math.isnan(df_eu_countries_taxes.loc[index_0].loc[index_1]):
#             df_eu_countries_taxes.loc[index_0].loc[index_1] = EU_taxes.loc[index_1]
#         else:
#             break
#     df_eu_countries_taxes.loc[index_0].fillna(method='bfill', inplace = True)
#
# df_import_tax = df_import_tax.append(df_eu_countries_taxes)
# df_import_tax.drop(df_import_tax[df_import_tax.Reporter == 'European Union'].index, inplace=True)
# df_import_tax.drop(['Reporter'],1,inplace=True)
#
# df_pattern = pd.read_pickle('Pattern Data Frame.pickle')
# df_import_tax = df_pattern.join(df_import_tax, how='left')
#
# print(len(df_import_tax.index.levels[0]),len(df_import_tax.index.levels[1]))
#
# df_import_tax.to_pickle('Import taxes.pickle')

# df = pd.read_pickle('Import taxes.pickle')
# for i in df.index.levels[0]:
#     sum_nan = 0
#     for index, row in df.loc[i].iterrows():
#         if math.isnan(df.loc[i].loc[index].values[0]):
#             sum_nan+=1
#     if sum_nan < len(df.index.levels[1]):
#         df.loc[i].fillna(method='ffill', inplace=True)
#         df.loc[i].fillna(method='bfill', inplace=True)
# df.to_pickle('Import taxes.pickle')

df = pd.read_pickle('Import taxes.pickle')
print(df)
