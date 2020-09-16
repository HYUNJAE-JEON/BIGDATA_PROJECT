import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


## 자판기 후보 grid 포인트와 가장 가까운 상권정보를 연결하여 새로운 csv 만들기

MaskCand = pd.read_csv('mask_candidate_pos_5181.csv')
Market = pd.read_csv('market_beyond_market_population_total_xy.csv') # , encoding='euc-kr'
# print(len(MaskCand))
print(len(Market))

def find_nearest_market(x, y):
  Market['XDIST'] = Market['x축'] - x
  Market['YDIST'] = Market['y축'] - y
  Market['GRIDDIST'] = Market['XDIST'].abs() + Market['YDIST'].abs()
  minpos = np.argmin(Market.values[:, 6])
  #print(Market.loc[minpos])
  nearest = Market.loc[minpos]
  return (nearest["상권_코드_명"], nearest["합계"], nearest["x축"], nearest["y축"], nearest["GRIDDIST"])
  

nearest = find_nearest_market(190000, 439000)
print(nearest)


NEAR = [find_nearest_market(x, y) for x,y in zip(MaskCand["X"], MaskCand["Y"])]
MaskCand["상권이름"] = [n[0] for n in NEAR]
MaskCand["상권크기"] = [n[1] for n in NEAR]
MaskCand["상권X"] = [n[2] for n in NEAR]
MaskCand["상권Y"] = [n[3] for n in NEAR]
MaskCand["GRIDDIST"] = [n[4] for n in NEAR]

MaskCand.to_csv("마스크후보상권정보포함.csv", index=False)
  