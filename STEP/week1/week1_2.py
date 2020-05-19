# -*- coding: UTF-8 -*-
# https://icanhazwordz.appspot.com/ のゲームで高得点をとれるように関数を工夫してみる

import collections
from week1_1 import binary_search_for_boundary,binary_search_for_index

# 見つけたアナグラムのなかから、できるだけ点数の高いものを返す必要がある
# 単純に、アナグラムを全部探して、その中で点数が最も高いものを返す愚直な実装にする

# 二つの辞書が条件を満たしているかを判定する関数
# 今回はQに関して注意しながら実装しないといけない
def compare(dict1,dict2):

    if 'q' in dict1:
        if 'q' in dict2 and dict1['u']-dict1['q']+dict2['q'] < dict2['u']:
            return False
        elif not 'q' in dict2 and dict1['u']-dict1['q'] < dict2['u']:
            return False

    for key in dict2:
        if not key in dict1:
            return False
        elif dict1[key]<dict2[key]:
            return False
        else:
            continue
    
    return True

# 単語のスコアを計算する関数
def calculate_score(word):

    # qに関してはquで一つ３点とカウントするため、uを重複してカウントしないようにuをqの数だけ減らしておく
    d = collections.Counter(word)
    if 'q' in d:
        d['u']-=d['q']
    
    two_points = ['c','f','h','l','m','p','v','w','y']
    three_points = ['j','k','q','x','z']

    score = 0
    for key in d:
        if key in two_points:
            score+=2*d[key]
        elif key in three_points:
            score+=3*d[key]
        else:
            score+=1*d[key]
    
    score = (score+1)**2

    return score

def homework1_2(s,method,dct,small_dct):

    # 見つかったanagramを格納するリスト
    ans = []

    # まずsを全て小文字にする
    s = s.lower()

    # 与えられた文字列sの中の各文字の出現回数をカウントした辞書を作っておく
    s_dct = collections.Counter(s)

    # 与えられた単語のnum文字目から始まる単語を、numを増やしながら順に調べていく
    num = 0
    checked_key = []

    # 二分探索を用いる
    if method==0:

        while num < len(s):
            
            key = s[num]
            if key in checked_key:
                # 既に調べた文字はもう調べない
                num += 1
                continue
            else:
                checked_key.append(key)
            
            boundary = binary_search_for_boundary(dct)
            
            # binary searchで先に探索を開始するべきindexを取得
            index1,index2 = binary_search_for_index(dct,key,boundary)

            # 辞書中の各文字の出現回数をカウント
            for j in [index1,index2]:

                while j < len(dct) and small_dct[j][0] == key:

                    dct_count = collections.Counter(small_dct[j])

                    # anagramが見つかり次第全てansに追加
                    if compare(s_dct,dct_count):
                        ans.append(small_dct[j])
                    
                    j+=1

            num += 1
    
    # 二分探索を用いず、辞書を前から順に見ていく
    # 正直二分探索のスコアがやたら低いことがあり失敗している時がある気がするのでこっちだと漏れがない
    # 時間のあるときに上の手法のデバッグをおこなう
    else:

        j=0
        while j<len(dct):

            dct_count = collections.Counter(small_dct[j])

            # anagramが見つかり次第全てansに追加
            if compare(s_dct,dct_count):
                ans.append(small_dct[j])
            
            j+=1

    # ansに格納されているanagramの中からスコアが最も高いものを返す
    score = 0
    word = ''
    for a in ans:
        s = calculate_score(a)
        if s>score:
            score = s
            word = a

    return score,word

if __name__ == '__main__':

    import time
    import argparse
    from selenium import webdriver
    import chromedriver_binary 
    from selenium.webdriver.common.by import By

    parser = argparse.ArgumentParser(description='与えられた文字列に対してAnagramを返すプログラム')
    parser.add_argument('-s','--score',type=int,help='目標得点',default=1600)
    parser.add_argument('-i','--max_iter',type=int,help='最大試行回数',default=5)
    parser.add_argument('-m','--method',type=int,help='探索方法',default=0)

    args = parser.parse_args()

    # 目標得点
    target_score = args.score
    # 最大試行回数
    max_iter = args.max_iter
    # 二分探索を用いるか否か
    method = args.method

    # 私のpc上のサイトから保存したテキストファイルのパス
    dct_path = 'dictionary.words.txt'
    with open(dct_path) as f:
        dct = [s.strip() for s in f.readlines()]
    
    small_dct = []
    for d in dct:
        small_dct.append(d.lower())

    trial=0
    my_score=0

    while my_score < target_score and trial < max_iter:

        driver = webdriver.Chrome()

        # webページにアクセス
        driver.get('https://icanhazwordz.appspot.com/')

        # 連続何回目の試行か
        trial+=1
        print('trial_time:',trial)

        # 今回の自分の累計スコア
        my_score = 0
        
        # 全部で10個のワードをつくる
        cnt = 1
        while cnt<11:

            letters=''
            # 16文字の取得
            for i in range(1,5):
                for j in range(1,5):

                    letter = driver.find_element(By.XPATH,'/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr['+str(i)+']/td['+str(j)+']/div').text
                    letters+=letter

            # 最高得点を得る単語およびその時のスコアの取得
            score,word = homework1_2(letters,method,dct,small_dct)

            # その単語を送信
            driver.find_element(By.XPATH,'/html/body/table[1]/tbody/tr/td[1]/form/input['+str(cnt+2)+']').send_keys(str(word))
            driver.find_element(By.XPATH,'/html/body/table[1]/tbody/tr/td[1]/form/input['+str(cnt+4)+']').click()

            # 累計スコアおよび作った単語の数を更新
            my_score += score
            cnt += 1

            time.sleep(0.1)
        
    # 10回終了して最終的なスコアが出たら、スコアを提出するかどうかを決定
    print('current score:',my_score)

    if my_score>target_score:

        print('high score!')
        driver.find_element(By.XPATH,'/html/body/table[1]/tbody/tr/td[1]/form/table/tbody/tr[1]/td[2]/input').send_keys('Eri Kizawa')
        driver.find_element(By.XPATH,'/html/body/table[1]/tbody/tr/td[1]/form/table/tbody/tr[2]/td[2]/input').send_keys('https://github.com/mochita314/algorithm/blob/master/STEP/week1/week1_2.py')
        #driver.find_element(By.XPATH,'/html/body/table[1]/tbody/tr/td[1]/form/table/tbody/tr[3]/td[2]/input').click()
        driver.find_element(By.XPATH,'/html/body/table[1]/tbody/tr/td[1]/form/table/tbody/tr[5]/td[2]').click()
        driver.find_element(By.XPATH,'/html/body/table[1]/tbody/tr/td[1]/form/table/tbody/tr[7]/td[2]/input').send_keys('Eri Kizawa')
        driver.find_element(By.XPATH,'/html/body/table[1]/tbody/tr/td[1]/form/table/tbody/tr[8]/td[2]/input').send_keys('eri.k.pn28@gmail.com')
        driver.find_element(By.XPATH,'/html/body/table[1]/tbody/tr/td[1]/form/input[13]').click()
    
    else:
        print('failed')

# https://icanhazwordz.appspot.com/highscores
