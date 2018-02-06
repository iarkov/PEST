import pandas as pd
import numpy as np
import math
import knoema
from Test import rename_index_cc, rename_index_to_abbv, join_empty_frame

# df = knoema.get('WFGCI2015', timerange='2006-2016', frequency='A', Country='AU;AT;BE;CA;CY;CZ;DK;EE;FI;FR;DE;GR;IS;IE;IL;IT;JP;KR;LV;LT;LU;MT;NL;NZ;NO;PT;SG;SK;SI;ES;SE;CH;TW;GB;US;RU;BN;HR;HU;PL;AR;BB;CL;TT;UY;VE;BH;KW;OM;QA;SA;AE;SC;PR;HT;BJ;BF;BI;TD;ET;GM;GN;LR;MG;MW;ML;MZ;RW;SL;TZ;UG;ZW;AM;CD;GE;KG;MD;TJ;UA;BD;BT;IN;ID;LA;MM;PH;LK;TL;VN;BO;SV;GT;GY;HN;NI;EG;MR;MA;PK;SY;YE;CM;CV;CI;GH;KE;LS;NG;SN;SZ;ZM;AZ;KZ;CN;MY;MN;TH;AL;BA;BG;MK;ME;RO;RS;TR;BR;CO;CR;DO;EC;JM;MX;PA;PY;PE;SR;DZ;IR;JO;LB;LY;TN;AO;BW;GA;MU;NA;ZA', Indicator='KN.A59;KN.A56;KN.A54;KN.A160;KN.A68', Measure='KN.M2')
#
# df.to_pickle('Socio-Cultural_Data.pickle')
# df = pd.read_pickle('Socio-Cultural_Data.pickle')
#
# df = df.resample('M').mean()
# df = df.resample('A').mean()
# df.columns = df.columns.droplevel(2)
# df.columns = df.columns.droplevel(2)
# df.rename_axis([None,None],axis=1,inplace=True)
#
# df_filled = pd.DataFrame(None, index = df.index, columns = df.columns)
#
# for column_0 in df.columns.levels[0]:
#     new_df = df[column_0].copy()
#     for column_1 in new_df.columns:
#         if False in new_df[column_1].isnull().tolist():
#             new_df[column_1].fillna(method='ffill',inplace=True)
#             new_df[column_1].fillna(method='bfill',inplace=True)
#     df_filled[column_0] = new_df
#
# df_filled.to_pickle('Socio-Cultural_Data.pickle')

# df = pd.read_pickle('Socio-Cultural_Data.pickle')
#
# df = df.transpose()
# df = df.unstack(1)
# df = df.stack(0)
# df = rename_index_cc(df)
# df.to_pickle('Socio-Cultural_Data.pickle')


# df = pd.read_pickle('Socio-Cultural_Data.pickle')
# df = df.unstack(1)
# df.drop('Puerto Rico', 0, inplace=True)
# df.to_pickle('Socio-Cultural_Data.pickle')

# df = pd.read_pickle('Socio-Cultural_Data.pickle')
# df = df.stack(1)
# df = rename_index_to_abbv(df)

# df_med_imp = pd.read_pickle('Medicaments Import (USD).pickle')
# df = df_med_imp.join(df, how='inner')
# df.to_pickle('Socio-Cultural_Data.pickle')

# df = pd.read_pickle('Socio-Cultural_Data.pickle')
# df  = join_empty_frame(df)
# df.to_pickle('Socio-Cultural_Data.pickle')

df = pd.read_pickle('pickles and excels\Socio-Cultural_Data.pickle')
df = df.loc[['CAN','HRV','SLV','GMB','MEX'],:]
df.to_excel('D:\Python\Python Diploma\pickles and excels\S_top5.xlsx')
