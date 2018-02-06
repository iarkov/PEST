import pandas as pd
import numpy as np
import knoema
import math
from Test import join_empty_frame

def rename_index_cc(df):
    df_cit_codes = pd.read_pickle('C_C.pickle')

    cit_codes_countries = df_cit_codes.iloc[:,1].tolist()
    t_countries = df.index.levels[0]

    new_index = []
    for country_0 in t_countries:
        for country_1 in cit_codes_countries:
            bool_list_0 = []
            bool_list_1 = []
            for a in range(4):
                if a > len(country_0)-1 or a > len(country_1)-1:
                    break

                if country_0[a] == country_1[a]:
                    bool_list_0.append(True)
                else:
                    bool_list_0.append(False)
                if country_0[-(a+1)] == country_1[-(a+1)]:
                    bool_list_1.append(True)
                else:
                    bool_list_1.append(False)
            if country_0[0] == country_1[0] and (False not in bool_list_0 or False not in bool_list_1):
                if country_0 != country_1:
                    ask = input('country: '+country_0+'\ncit_codes: '+country_1+'\nrename country (y/n): ')
                    if ask == 'y':
                        country_0 = country_1
        new_index.append(country_0)
    lists = [new_index, df.index.levels[1].tolist()]
    new_m_index = pd.MultiIndex.from_product(lists)
    new_dataframe = pd.DataFrame(df.values, index=new_m_index, columns=df.columns)

    return new_dataframe

##df = knoema.get('WFGCI2015', frequency='A', Country='AU;AT;BE;CA;CY;CZ;DK;EE;FR;FI;DE;GR;HK;IS;IE;IL;IT;JP;KR;LV;LT;LU;MT;NL;NZ;NO;PT;SG;SK;SI;ES;SE;CH;TW;GB;US;RU;BN;HR;HU;PL;AR;BB;CL;UY;TT;VE;BH;KW;OM;QA;SA;AE;SC;PR;KH;NP;HT;BJ;BF;BI;TD;ET;GM;GN;LR;MG;ML;MW;MZ;RW;SL;TZ;UG;ZW;AM;CD;GE;KG;TJ;MD;UA;BD;BT;IN;ID;LA;MM;PH;LK;TL;VN;BO;SV;GT;GY;HN;NI;EG;MR;MA;PK;SY;YE;CM;CV;CI;GH;KE;LS;NG;SN;SZ;ZM;CN;MY;MN;TH;AZ;KZ;AL;BA;BG;MK;ME;RO;RS;TR;BZ;BR;CO;CR;DO;EC;JM;MX;PA;PY;PE;SR;DZ;IR;JO;LB;LY;TN;AO;BW;GA;MU;NA;ZA', Indicator='KN.A122;KN.A126', Measure='KN.M2')
##
##df = df.resample('M').mean()
##df = df.resample('A').mean()
##df.columns = df.columns.droplevel(3)
##df.columns = df.columns.droplevel(2)
##
##df = df.transpose()
##df = df.stack()
##df = df.unstack(1)
##df = df.unstack(1)

# for index in df.index:
#     boo = False
#     for column_0 in df.columns.levels[0]:
#         for column_1 in df.columns.levels[1]:
#             if math.isnan(df.loc[index][column_0][column_1]):
#                 boo = True
#                 break
#         if boo:
#             break
#     if boo:
#         df.drop(index, 0, inplace = True)
#
# df = df.drop('Hong Kong SAR', 0)
# df = df.stack(1)
#
# df.to_pickle('Technological data.pickle')
# # for column_0 in df.columns.levels[0]:
# #     boo = False
# #     for index in df.index:
# #         for column_1 in df.columns.levels[1]:
# #             if math.isnan(df[column_0][column_1].loc[index]):
# #                 boo = True
# #                 break
# #         if boo:
# #             break
# #     if boo:
# #         df.drop([column_0],1,inplace=True)
#
#

# # df.index.rename([None, None], level=[0,1], inplace=True)
# # df.columns.rename(None,inplace = True)
#

# df = df.stack(1)
#
# print(df.index.levels[0])
# df = pd.read_pickle('Technological data.pickle')
# df_cit_codes = pd.read_pickle('C_C.pickle')
#
# df = rename_index_cc(df)
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
# df.to_pickle('Technological data.pickle')

# df = pd.read_pickle('Technological data.pickle')
# df.drop(['Medicaments Import (USD)'], 1, inplace=True)
# df_med_imp = pd.read_pickle('Medicaments Import (USD).pickle')
# df = df_med_imp.join(df, how='right')

# df_t = df_med_imp.join(df, how='right')
# df_t = pd.DataFrame()
# for index in df.index.levels[0]:
#     df_test = df.loc[index].copy()
#     df_test['Medicaments Import (USD)'].fillna(method='bfill', inplace=True)
#     df_test['Medicaments Import (USD)'].fillna(method='ffill', inplace=True)
#     if df_t.empty:
#         df_t = df_test
#     else:
#         df_t.append(df_test)

# print(df)
# df.to_pickle('Technological data.pickle')

# df = pd.read_pickle('Technological data.pickle')
# df  = join_empty_frame(df)
# df.to_pickle('Technological data.pickle')

df = pd.read_pickle('pickles and excels\Technological data.pickle')

df = df.loc[['CAN','HRV','SLV','GMB','MEX'],:]
df.to_excel('D:\Python\Python Diploma\pickles and excels\T_top5.xlsx')
