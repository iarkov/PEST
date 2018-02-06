import pandas as pd
import numpy as np
import Radar

def unify(df, return_df = True, return_labels = False, return_av_0_column = False):
    dfu = df.copy()
            
    for j in range(len(dfu.columns)):
        av_0_column = None     
        array = []
        
        for i in range(1,len(dfu.index)):
            array.append(abs(dfu.iloc[i-1,j] - dfu.iloc[i,j]))
        if sum(array) == 0:
            av = 0
            av_0_column = j + 1
        else:
            av = sum(array) / len(array)
        
        ii = 1
        

        if av < 1 and av > 0:
            while av < 1:
                ii = ii * 10
                av = av * 10
            for i in range(len(dfu.index)):
                dfu.iloc[i,j] = dfu.iloc[i,j]*ii
        elif av > 10:
            av = int(av)
            avstr = str(av)
            for k in range(len(avstr)-1):
                ii = ii * 10
            for i in range(len(df.index)):
                dfu.iloc[i,j] = dfu.iloc[i,j]/ii
        elif av == 0:
            continue
        
        
    df = dfu
    dfu = None
    if return_df and return_labels:
        return df, df.columns
    elif return_av_0_column:
        if av_0_column != None:
            return av_0_column
    else:
        return df

    
class Pest:
    
    def __init__(self, df, y, x, x_labels):

        self.labels = x_labels
        self.df = df
        y = y.reshape(len(y),1)
        self.y = np.matrix(y)
        onearray = []
        for i in x:
            onearray.append(1)
        X = []
        for i in range(len(onearray)):
            e = []
            e.append(onearray[i])
            for j in x[i]:
                e.append(j)
            X.append(e)

        X = np.array(X)
        self.X = np.asmatrix(X)
        
    
    def analyze(self):
        Xt = self.X.transpose()
        b = np.dot(Xt,self.X)
        xy = np.dot(Xt, self.y)
        det = np.linalg.det(b)
       
        if det == 0:
            av_0 = unify(self.df, return_df = False, return_av_0_column = True)

            while det == 0:
                for i in range(len(self.X)):
                    self.X[i, av_0] += 0.1
                Xt = self.X.transpose()
                b = np.dot(Xt,self.X)
                xy = np.dot(Xt, self.y)
                det = np.linalg.det(b)
                    
            
        binv = np.linalg.inv(b)
        a = np.dot(binv,xy)
        sum_a = 0
        for i in range(1, len(a)):
            if sum_a == 0:
                sum_a = abs(a[i,0])
            else:
                sum_a = sum_a + abs(a[i,0])
            
        a_list = []
        av_change_list = []
        av_list = []
        ev_list = []
        
        for i in range(1, len(a)):
            a_list.append(float('{:.2f}'.format(abs(a[i,0])/sum_a)))

            array_change = []
            for j in range(1, len(self.X)):
                array_change.append(self.X[j,i] - self.X[j-1,i])
            if sum(array_change) == 0:
                av_change = 0
            else: 
                av_change = sum(array_change)/len(array_change)
            av_change_list.append(av_change)

            array_x = []
            for j in range(len(self.X)):
                array_x.append(self.X[j,i])
            if sum(array_x) == 0:
                av == 0
            else:
                av = sum(array_x)/len(array_x)
            av_list.append(av)

            last_change = self.X[-2,i] - self.X[-1,i]
            ev_av = 0
            ev_change = 0

            if a[i,0] >= 0:
                if self.X[-1,i] >= av:
                    if av_change == 0:
                        av_change = 0.01
                    if av_change > 0:
                        ev_av = 5
                        if last_change >= av_change and last_change <= (av_change*2):
                            ev_change = int(ev_av * (last_change / av_change))
                        elif last_change > (av_change * 2):
                            ev_change = ev_av * 2
                        else:
                            ev_change = ev_av
                    else:
                        ev_av = 4
                        if last_change < av_change:
                            ev_change = 1
                        elif last_change >= av_change and last_change < 0:
                            ev_change = int(ev_av  - ev_av * (last_change / av_change))
                        elif last_change == 0:
                            ev_change = ev_av
                        elif last_change > 0:
                            ev_change = int((ev_av + 1) * (last_change / abs(av_change)))

                elif self.X[-1,i] < av:
                    if av_change == 0:
                        av_change = 0.01
                    if av_change > 0:
                        ev_av = 5
                        if last_change >= av_change and last_change <= (av_change*2):
                            ev_change = int(ev_av * (last_change / av_change) * 9/10)
                        elif last_change > (av_change * 2):
                            ev_change = int(ev_av * 2 * 9/10)
                        else:
                            ev_change = int(ev_av * 9/10)
                    else:
                        ev_av = 4
                        if last_change < av_change:
                            ev_change = 0
                        elif last_change >= av_change and last_change <= 0:
                            ev_change = int(ev_av - ev_av * (last_change / av_change))
                        elif last_change > 0:
                            ev_change = int(ev_av + 1)

            else:
                if self.X[-1,i] >= av:
                    if av_change == 0:
                        av_change = -0.01
                    if av_change > 0:
                        ev_av = 3
                        if last_change > (av_change * 2):
                            ev_change = 0
                        elif last_change >= av_change and last_change <= (av_change*2):
                            ev_change = int(ev_av - ev_av * ((last_change / av_change) - 1))
                        elif last_change < av_change and last_change >= 0:
                            ev_change = int(ev_av + (1 - (last_change/av_change)))
                        else:
                            ev_change = ev_av + 1
                    else:
                        ev_av = 4
                        if last_change > 0:
                            ev_change = int(ev_av)
                        elif last_change <= 0 and last_change > av_change:
                            ev_change = int(ev_av + (last_change/av_change))
                        elif last_change <= av_change and last_change > (av_change*2):
                            ev_change = int(ev_av + 1*(last_change/av_change))
                        else:
                            ev_change = int(ev_av + 2)


                elif self.X[-1,i] < av:
                    if av_change == 0:
                        av_change = 0.01
                    if av_change > 0:
                        ev_av = 6
                        if last_change < 0:
                            ev_change = int(ev_av)
                        elif last_change >= 0 and last_change <= av_change:
                            ev_change = int(ev_av - last_change/av_change)
                        elif last_change > av_change and last_change <= (av_change*2):
                            ev_change = int(ev_av - 1*(last_change/av_change))
                        else:
                            ev_change = int(ev_av - 3)

                    else:
                        ev_av = 7
                        if last_change > 0:
                            ev_change = int(ev_av)
                        elif last_change <= 0 and last_change > av_change:
                            ev_change = int(ev_av + (last_change/av_change))
                        elif last_change <= av_change and last_change > (av_change*2):
                            ev_change = int(ev_av + 1*(last_change/av_change))
                        else:
                            ev_change = int(ev_av + 3)
            if ev_change > 10:
                ev_change = 1
                
            ev_list.append(ev_change)

            rate = 0
            
            for i in range(len(ev_list)):
                if rate == 0:
                    rate =  a_list[i] * ev_list[i]
                else:
                    rate = rate + a_list[i] * ev_list[i]
                    
            rate = float('{:.2f}'.format(rate))
            
            a_dict = {}
            i = 1
            for label in self.labels:
                a_dict[label] = [a[i,0]]
                i += 1
        return a_list, ev_list, rate, a_dict
        
df_c_c = pd.read_pickle('D:\Python\Python Diploma\pickles and excels\C_C.pickle')
   
df_p = pd.read_pickle('D:\Python\Python Diploma\pickles and excels\Political_Data.pickle')
df_p.drop('PAN', level = 0, inplace=True)
##df_p = df_p.loc[['CAN','HRV','SLV','GMB','MEX'],:]

df_e = pd.read_pickle('D:\Python\Python Diploma\pickles and excels\Joined_Economic_Data.pickle')
df_e.drop('PAN', level = 0, inplace=True)
##df_e = df_e.loc[['CAN','HRV','SLV','GMB','MEX'],:]

df_s = pd.read_pickle('D:\Python\Python Diploma\pickles and excels\Socio-Cultural_Data.pickle')
df_s.drop('PAN', level = 0, inplace=True)
##df_s = df_s.loc[['CAN','HRV','SLV','GMB','MEX'],:]

df_t = pd.read_pickle('D:\Python\Python Diploma\pickles and excels\Technological data.pickle')
df_t.drop('PAN', level = 0, inplace=True)
##df_t = df_t.loc[['CAN','HRV','SLV','GMB','MEX'],:]

country_list = []
square_dict = {}
values = []

df_main = pd.DataFrame()
df_a = pd.DataFrame()
df_a_columns_0 = []
df_a_columns_1 = []
b_p = False
b_e = False
b_s = False
b_t = False
for index_0 in df_e.index.levels[0]:
    if index_0 == 'PAN':
        continue
    country = ''
    for index_1 in df_c_c.index:
        if index_0 == df_c_c.loc[index_1, 'Code']:
            country = df_c_c.loc[index_1, 'Country of Citizenship']
            country_list.append(country)
##            print(country)
##    print(index)
    
    df_pt = df_p.loc[index_0]
    df_et = df_e.loc[index_0]
    df_st = df_s.loc[index_0]
    df_tt = df_t.loc[index_0]
    
    df_yp = df_pt['Medicaments Import (USD)']
    df_ye = df_et['Medicaments Import (USD)']
    df_ys = df_st['Medicaments Import (USD)']
    df_yt = df_tt['Medicaments Import (USD)']
    
    yp = np.array(df_yp)
    ye = np.array(df_ye)
    ys = np.array(df_ys)
    yt = np.array(df_yt)
    
    df_xp = df_pt.drop(['Medicaments Import (USD)'],1)
    df_xe = df_et.drop(['Medicaments Import (USD)'],1)
    df_xs = df_st.drop(['Medicaments Import (USD)'],1)
    df_xt = df_tt.drop(['Medicaments Import (USD)'],1)
    
    df_xp, labels_p = unify(df_xp, return_labels = True)
    df_xe, labels_e = unify(df_xe, return_labels = True)
    df_xs, labels_s = unify(df_xs, return_labels = True)
    df_xt, labels_t = unify(df_xt, return_labels = True)
    
##    for index, row in df_x.iterrows():
##        print(float('{:.2f}'.format(df_x.loc[index, 'GDP(LCU)'])))
    Xp = np.array(df_xp)
    Xe = np.array(df_xe)
    Xs = np.array(df_xs)
    Xt = np.array(df_xt)

    pest_p = Pest(df_xp, yp, Xp, labels_p)
    pest_e = Pest(df_xe, ye, Xe, labels_e)
    pest_s = Pest(df_xs, ys, Xs, labels_s)
    pest_t = Pest(df_xt, yt, Xt, labels_t)

##    print(pest_p.analyze())
##    print(pest_e.analyze())
##    print(pest_s.analyze())
##    print(pest_t.analyze())
    
    a_list_p, ev_list_p, rate_p, a_p = pest_p.analyze()
    a_list_e, ev_list_e, rate_e, a_e = pest_e.analyze()
    a_list_s, ev_list_s, rate_s, a_s = pest_s.analyze()
    a_list_t, ev_list_t, rate_t, a_t = pest_t.analyze()

    square = (rate_p*rate_e)/2 + (rate_e*rate_s)/2 + (rate_s*rate_t)/2  ++ (rate_t*rate_p)/2
    square_dict[country] = [float('{:.3f}'.format(square))]

    row = []
    columns_1 = []
    columns_2 = []
    columns_3 = []
    
    for i in range(len(a_list_p)):
        row.append(a_list_p[i])
        columns_3.append('U. W.')
        columns_2.append(labels_p[i])
        columns_1.append('Political Sector')
        row.append(ev_list_p[i])
        columns_3.append('Points')
        columns_2.append(labels_p[i])
        columns_1.append('Political Sector')
    row.append(rate_p)
    columns_3.append('')
    columns_2.append('Rate')
    columns_1.append('Political Sector')
    for i in range(len(a_list_e)):
        row.append(a_list_e[i])
        columns_3.append('U. W.')
        columns_2.append(labels_e[i])
        columns_1.append('Economical Sector')
        row.append(ev_list_e[i])
        columns_3.append('Points')
        columns_2.append(labels_e[i])
        columns_1.append('Economical Sector')
    row.append(rate_e)
    columns_3.append('')
    columns_2.append('Rate')
    columns_1.append('Economical Sector')
    for i in range(len(a_list_s)):
        row.append(a_list_s[i])
        columns_3.append('U. W.')
        columns_2.append(labels_s[i])
        columns_1.append('Socio-Cultural Sector')
        row.append(ev_list_s[i])
        columns_3.append('Points')
        columns_2.append(labels_s[i])
        columns_1.append('Socio-Cultural Sector')
    row.append(rate_s)
    columns_3.append('')
    columns_2.append('Rate')
    columns_1.append('Socio-Cultural Sector')
    for i in range(len(a_list_t)):
        row.append(a_list_t[i])
        columns_3.append('U. W.')
        columns_2.append(labels_t[i])
        columns_1.append('Technological Sector')
        row.append(ev_list_t[i])
        columns_3.append('Points')
        columns_2.append(labels_t[i])
        columns_1.append('Technological Sector')
    row.append(rate_t)
    columns_3.append('')
    columns_2.append('Rate')
    columns_1.append('Technological Sector')

    columns_list = [columns_1, columns_2, columns_3]
    tuples = list(zip(*columns_list))
    multi_columns = pd.MultiIndex.from_tuples(tuples)
    row = np.array(row)
    df = pd.DataFrame(row, index = multi_columns, columns = [country])
    df = df.transpose()
    
    df_main = df_main.append(df)

    df_ap = pd.DataFrame()
    for key, value in a_p.items():
        if b_p:
            break
        df_a_columns_0.append('Political Sector')
        df_a_columns_1.append(key)
    b_p = True
    df_ap = df_ap.from_dict(a_p, orient = 'columns')
    df_ap.index = [country]
##    df_a = df_a.append(df_ap)

    df_ae = pd.DataFrame()
    for key, value in a_e.items():
        if b_e:
            break
        df_a_columns_0.append('Economical Sector')
        df_a_columns_1.append(key)
    b_e = True
    df_ae = df_ae.from_dict(a_e, orient = 'columns')
    df_ae.index = [country]
    df_a_pe = df_ap.join(df_ae)
##    df_a = df_a.append(df_ae)
    df_as = pd.DataFrame()
    for key, value in a_s.items():
        if b_s:
            break
        df_a_columns_0.append('Socio-Cultural Sector')
        df_a_columns_1.append(key)
    b_s = True
    df_as = df_as.from_dict(a_s, orient = 'columns')
    df_as.index = [country]
    df_a_pes = df_a_pe.join(df_as)
##    df_a = df_a.append(df_as)
    df_at = pd.DataFrame()
    for key, value in a_t.items():
        if b_t:
            break
        df_a_columns_0.append('Technological Sector')
        df_a_columns_1.append(key)
    b_t = True
    df_at = df_at.from_dict(a_t, orient = 'columns')
    df_at.index = [country]
    df_a_pest = df_a_pes.join(df_at)
##    df_a = df_a.append(df_as)
    df_a = df_a.append(df_a_pest)
    
df_a_col_lists = [df_a_columns_0,df_a_columns_1]
tuples_a = list(zip(*df_a_col_lists))
a_multi_cols = pd.MultiIndex.from_tuples(tuples_a)
df_a.columns = a_multi_cols
df_a.loc[['Canada','Mexico','Croatia','El Salvador','Gambia'],:].to_excel('a_top5.xlsx')
##print(df_a.loc[['Canada','Croatia','El Salvador','Gambia','Mexico'],:])
##df_square = pd.DataFrame()
##df_square = df_square.from_dict(square_dict, orient = 'index')
##df_square.to_excel('D:\Python\Python Diploma\pickles and excels\square.xlsx')
##df_main.to_excel('D:\Python\Python Diploma\pickles and excels\PEST.xlsx')
##    values.append(row)
    
##    Radar.radar(country_list[-1], rate_p, rate_e, rate_s, rate_t)

