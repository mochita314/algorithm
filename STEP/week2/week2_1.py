# 宿題１
# 行列の積を計算し、行列のサイズNと実行時間の関係を調べる

# 1~9のランダムな整数を要素とするN*Nの行列を返す
def make_random_matrix(N):
    matrix = np.random.randint(1, 10, (N, N))
    return matrix

# 行列AとBの積を計算する関数
def multiply_matrix(A,B):

    # A,Bはリストの形で与えられるN*Nの行列
    N = len(A)

    # AとBの積をCとする
    C = np.zeros((N,N))

    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i,j] += A[i,k]*B[k,j]
    
    return C

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import numpy as np
    import time
    import argparse

    parser = argparse.ArgumentParser(description='行列の積の計算にかかる時間を計算するプログラム')
    parser.add_argument('-n','--MAX_N',help='検証する行列の行数(列数)の最大値',type=int,default=10)
    args = parser.parse_args()

    # Nは2から指定した数字まで検証する
    max_n = args.MAX_N

    # x軸：N
    x = [N for N in range(2,max_n)]
    # y軸：計算時間
    y = []

    for N in range(2,max_n):

        A = make_random_matrix(N)
        B = make_random_matrix(N)

        # 開始時間
        start = time.time()

        C = multiply_matrix(A,B)

        # 経過時間 = 終了時間 - 開始時間
        elapsed_time = time.time() - start
        
        # 各Nに対して実行時間を記録
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