import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mask_candidate_pos_5181.csv', encoding='euc-kr')
#print(df[:10])

df_2 = df[(df.D>0)]
df_3 = df_2[:135000]
#print(df_2[:30])

df_3.to_csv("130000.csv", encoding = 'euc-kr', index=False)

data_c = pd.read_csv('CONV_DRUG_total_xy.csv', encoding='euc-kr')
data_conx = data_c['x']
data_cony = data_c['y']
#plt.scatter(data_conx, data_cony, marker = 'o', c = 'g', s = 2, alpha=0.5)

data_f = pd.read_csv('market_beyond_market_population_total_xy.csv', encoding='utf-8')
data_fx = data_f['x']
data_fy = data_f['y']

data_filx = df_3['X']
data_fily = df_3['Y']


plt.title("Seoul")
plt.scatter(data_filx, data_fily, marker='o', c='y', s = 3, alpha=0.5)
plt.scatter(data_fx, data_fy, marker='o', c='b', s = 10, alpha=1)

plt.xlabel("X")
plt.ylabel('Y')

plt.ylim(437000, 467000)
plt.xlim(182000, 217000)
plt.grid(True)
plt.show()

