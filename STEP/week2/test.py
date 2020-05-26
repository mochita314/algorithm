'''
import numpy as np
import time
import matplotlib.pyplot as plt

x = [i for i in range(2,1001)]
y = []

for i in range(2,1001):

    if i%10 == 0:
        print(i)
    li1 = np.random.randint(1,9,(i,1))
    li2 = np.random.randint(1,9,(i,1))

    start = time.time()
    combined3 = [(x, y) for x in li1 for y in li2]
    elapsed_time = time.time() - start
    y.append(elapsed_time)

# 図の初期化
fig = plt.figure(figsize=(12,8))

# 図にAxesを追加
ax = fig.add_subplot(111)
ax.plot(x,y,label="elapsed time")

# 凡例の表示
plt.legend()

# グラフの表示
plt.show()

'''

