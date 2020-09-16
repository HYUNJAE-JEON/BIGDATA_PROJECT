import numpy as np
import numpy.random
import pandas as pd
import matplotlib.pyplot as plt

## 조정 파라미터
GRID_STEP = 50
RADIUS = 1000
MIN_NEIGHBOR_PHARM = 5
MAX_NEIGHBOR_PHARM = 100

## 바둑판 만들기
Xgrid = np.arange(180000, 216000, GRID_STEP)
Ygrid = np.arange(435000, 466000, GRID_STEP)
XX, YY  = np.meshgrid(Xgrid, Ygrid, sparse=False)
Grid = np.dstack((XX, YY))
print(Grid.shape)
Grid = Grid.reshape(-1, 2)
print(Grid.shape)



## 약국데이터
PharmPos = pd.read_csv('CONV_DRUG_total_xy.csv', encoding='euc-kr')
PharmPos = PharmPos.filter(items=['x', 'y'])


DIST_TO_PHARM = []
for i in range(Grid.shape[0]):
    X = Grid[i][0]
    Y = Grid[i][1]
    # 반경내 약국/편의점 찾음
    data_in_radius = PharmPos[(PharmPos['x'] >= X-RADIUS) & (PharmPos['x'] <= X+RADIUS) &
                         (PharmPos['y'] >= Y-RADIUS) & (PharmPos['y'] <= Y+RADIUS)]
    candidates = data_in_radius.values
    num_cand = candidates.shape[0]
    
    if num_cand > 0:
      print(i, num_cand)
      
    if num_cand  < MIN_NEIGHBOR_PHARM or num_cand > MAX_NEIGHBOR_PHARM:
      # 제외하게 됨
      DIST_TO_PHARM.append((0, num_cand))
    else:
      # 가장 가까운 약국/편의점 5개를 뽑아서, 그들과의 평균 거리를 구함
      dist_to_pharms = [np.linalg.norm(Grid[i] - candidates[j], ord = 1) for j in range(num_cand)]
      dist_to_pharms.sort()
      top_5 = dist_to_pharms[:5]
      avg_dist = sum(top_5) / len(top_5)
      DIST_TO_PHARM.append((avg_dist, num_cand))
      
##
print(Grid.shape)
print(PharmPos.shape)


merged = [(gr[0], gr[1], dist[0], dist[1])   for gr, dist in zip(Grid, DIST_TO_PHARM) if dist != 0]
# D 순으로 내림차순.
merged.sort(key=lambda e: e[2], reverse=True)
df = pd.DataFrame(merged, columns=["X", "Y", "D", "N"])
df.to_csv("mask_candidate_pos.csv", index=False)