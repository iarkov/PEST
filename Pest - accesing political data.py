import pandas as pd
import numpy as np
import knoema
import math
from Test import join_empty_frame

# df = knoema.get('WFGCI2015', timerange='2006-2017', frequency='A', Country='AU;AT;BE;CA;CY;CZ;DK;EE;FI;FR;DE;GR;HK;IS;IE;IL;IT;JP;KR;LV;LT;LU;MT;NL;NZ;NO;PT;SG;SK;SI;ES;SE;CH;TW;GB;US;RU;BN;HR;HU;PL;AR;BB;CL;TT;UY;VE;BH;KW;OM;QA;SA;AE;SC;PR;KH;NP;HT;BJ;BF;BI;TD;ET;GM;GN;LR;MG;MW;ML;MZ;RW;SL;TZ;UG;ZW;AM;CD;GE;KG;MD;TJ;UA;BD;BT;IN;ID;LA;MM;PH;LK;TL;VN;BO;SV;GT;GY;HN;NI;EG;MR;MA;PK;SY;YE;CM;CV;CI;GH;KE;LS;NG;SN;SZ;ZM;AZ;KZ;CN;MY;MN;TH;AL;BA;BG;MK;ME;RO;RS;TR;BZ;BR;CO;CR;DO;EC;JM;MX;PA;PY;PE;SR;DZ;IR;JO;LB;LY;TN;AO;BW;GA;MU;NA;ZA', Indicator='KN.A3;KN.A6;KN.A10;KN.A19', Measure='KN.M2')
# df.to_pickle('Political_Data.pickle')


# df = pd.read_excel('kk.xlsx')
# df_cit_codes = pd.read_pickle('C_C.pickle')
# abbv_list = []
#
# for country_0 in df_cit_codes['Country of Citizenship']:
#     for country_1 in df.index.levels[0]:
#         if country_0 == country_1:
#             country_loc = np.where(df_cit_codes.values==str(country_0))
#             abbv = str(df_cit_codes.iloc[country_loc[0][0],country_loc[1][0]-1])
#             abbv_list.append(abbv)
#
# new_index_list = [abbv_list,df.index.levels[1].tolist()]
# new_index = pd.MultiIndex.from_product(new_index_list)
#
# new_df = pd.DataFrame(df.values, index = new_index, columns = df.columns)
# df = new_df
# print(df)
# df.to_pickle('Political_Data.pickle')


# df = pd.read_pickle('Political_Data.pickle')
#
# # df = pd.DataFrame(df.values, index = df.index, columns=df.columns.droplevel(2))
# df.columns = df.columns.droplevel(3)
# df.columns = df.columns.droplevel(2)
# for column_0 in df.columns.levels[0]:
#     boo = False
#     for index in df.index:
#         for column_1 in df.columns.levels[1]:
#             if math.isnan(df[column_0][column_1].loc[index]):
#                 boo = True
#                 break
#         if boo:
#             break
#     if boo:
#         df.drop([column_0],1,inplace=True)
# # df.to_excel('kk.xlsx')
# # df.drop(('Albania','Ethics and corruption'),axis=1, inplace=True)
#
# df = df.stack()
# df = df.stack()
# df = df.unstack(1)
# df.index.rename([None, None], level=[0,1], inplace=True)
# df.columns.rename(None,inplace = True)
#
# df = df.swaplevel(i=-2, j=-1, axis=0)
# df.sort_index(level=0,inplace=True)
#
# df.to_excel('kk.xlsx')
# list_ = pd.read_excel('kkk.xlsx')
# list_ = list_.values
# index_list_0 = []
# for value in list_:
#     try:
#         a = value[0]
#         index_list_0.append(a)
#         i += 1
#     except BaseException:
#         continue
# # df_cit_codes = pd.read_pickle('C_C.pickle')
# # df_test = pd.merge(index_list_0, df_cit_codes, on='Country of Citizenship', how='inner')
# index_list_1 = df.index.levels[0]
# iterables = [index_list_0, index_list_1]
# index_product = pd.MultiIndex.from_product(iterables)
# df_new = pd.DataFrame(df.values, index = index_product, columns = df.columns)
#
# df_p = pd.read_pickle('Political_Data.pickle')
# df_resampled = pd.DataFrame()
# df_je = pd.read_pickle('Joined_Empty_Dataframes.pickle')
#
# index = df_p.index.join(df_je.index, how='right', level=0)
# df_for_join = pd.DataFrame(None, index = index, columns=None)
# df_p = df_p.join(df_for_join, how = 'right')
# for index in df_p.index.levels[0]:
#     df_r = df_p.loc[index]
#     df_r = df_r.resample('M').mean()
#     df_r = df_r.resample('Y').mean()
#     index_0 = [index]
#     index_1 = df_r.index.tolist()
#     index_list = [index_0,index_1]
#     multiindex = pd.MultiIndex.from_product(index_list)
#     new_df = pd.DataFrame(df_r.values, index=multiindex, columns=df_r.columns)
#     if df_resampled.empty:
#         df_resampled=new_df
#     else:
#         df_resampled = df_resampled.append(new_df)
# print(df_resampled)
# df_resampled.to_pickle('Political_Data.pickle')

# df_med_imp = pd.read_pickle('Medicaments Import (USD).pickle')
# df_p = df_med_imp.join(df_p, how='right')
# for index in df_p.index.levels[0]:
#     df_p.loc[index]['Medicaments Import (USD)'].fillna(method='ffill', inplace=True)
#     df_p.loc[index]['Medicaments Import (USD)'].fillna(method='bfill', inplace=True)
# print(df_p)
# df_p.to_pickle('Political_Data.pickle')

# df = pd.read_pickle('Political_Data.pickle')
# df_med_imp = pd.read_pickle('Medicaments Import (USD).pickle')
# df  = join_empty_frame(df)
# df = df_med_imp.join(df, how = 'right')
# print(df)
# print(len(df.index.levels[0].tolist()))
# df.to_pickle('Political_Data.pickle')

df = pd.read_pickle('pickles and excels\Political_Data.pickle')
# if False in df.isnull().tolist():
#     print('kek')
##for column in df.columns:
##    if True not in df[column].isnull().tolist():
##        print('lol')
##    else:
##        print('kek')

df = df.loc[['CAN','HRV','SLV','GMB','MEX'],:]
df.to_excel('D:\Python\Python Diploma\pickles and excels\P_top5.xlsx')
