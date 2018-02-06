import pandas as pd
df_p = pd.read_pickle('Political_Data.pickle')
df_e = pd.read_pickle('Joined_Economic_Data.pickle')
df_t = pd.read_pickle('Technological data.pickle')
df_s = pd.read_pickle('Socio-Cultural_Data.pickle')

index_p = df_p.index.levels[0]
df_p_empty = pd.DataFrame(None, index=index_p, columns=None)

index_e = df_e.index.levels[0]
df_e_empty = pd.DataFrame(None, index=index_e, columns=None)

df_p_e_empty = df_e_empty.join(df_p_empty, how='inner')

index_t = df_t.index.levels[0]
df_t_empty = pd.DataFrame(None, index = index_t, columns=None)

df_p_e_t_empty = df_p_e_empty.join(df_t_empty, how='inner')

index_s = df_s.index.levels[0]
df_s_empty = pd.DataFrame(None, index=index_s, columns=None)


df_p_e_s_t_empty = df_p_e_t_empty.join(df_s_empty, how='inner')
df_p_e_s_t_empty.to_pickle('Joined_Empty_Dataframes.pickle')

index_0 = df_s.index
index_1 = df_p_e_s_t_empty.index
index_joined = index_0.join(index_1, how='inner', level=0)
print(len(index_joined.levels[0].tolist()))
