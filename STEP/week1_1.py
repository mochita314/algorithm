# -*- coding: UTF-8 -*-

# 与えられた文字列のAnagramを辞書ファイルから探して返す
# 文字は全て使わなくても良いように関数をアップグレード
# https://icanhazwordz.appspot.com/ のゲームで高得点をとれるように関数を工夫してみる

import collections

'''各単語の文字数をカウントして比較する方法で実装'''

# 二分探索の関数を用途に合わせて2つ用意

# 小文字と大文字の境界のindexを見つけるための二分探索
def binary_search_for_boundary(dct):
    left = 0
    right = len(dct)

    while left!=right and left != right-1:
        mid = (left+right)//2
        if dct[mid][0] == 'a':
            right = mid
        elif  dct[mid][0].upper() != dct[mid][0]:
            right = mid
        else:
            left = mid+1
    
    if dct[left][0]!='a' and dct[right][0]=='a':
        return right

    return left

def binary_search_for_index(dct,key,boundary):
    # 各文字の最初の単語のインデックスを見つけるために行う
    # 辞書は、大文字の単語A-Z -> 小文字の単語a-zで並んだ仕様になっているので、インデックスを2つ返す必要がある
    # boundaryは、頭文字が小文字にきりかわるindex

    # mid番目の単語の最初の文字と、sの最初の文字=keyを比較する
    left1 = 0
    right1 = boundary-1
    left2 = boundary
    right2 = len(dct)

    # sの最初の文字=keyから始まる単語のなかで、辞書で最初に出てくる単語がみつかるまで続ける
    while left1!=right1 and left1 != right1-1:
        mid = (left1+right1)//2
        if dct[mid][0]==key:
            right1 = mid
        elif key < dct[mid][0]:
            right1 = mid
        else:
            left1 = mid+1
    
    while left2!=right2 and left2 != right2-1:
        mid = (left2+right2)//2
        if dct[mid][0]==key:
            right2 = mid
        elif key < dct[mid][0]:
            right2 = mid
        else:
            left2 = mid+1

    if dct[left1][0]!=key and dct[right1][0]==key:
        index1 = right1
    else:
        index1 = left1

    if dct[left2][0]!=key and dct[right2][0]==key:
        index2 = right2
    else:
        index2 = left2

    return index1,index2

# 二つの辞書が条件を満たしているかを判定する関数
def compare(dict1,dict2):
    for key in dict2:
        if not key in dict1:
            return False
        elif dict1[key]<dict2[key]:
            return False
        else:
            continue
    return True

def homework1_1(s):

    # まずsを全て小文字にする
    s = s.lower()

    # 与えられた文字列sの中の各文字の出現回数をカウントした辞書を作っておく
    s_dct = collections.Counter(s)

    # 私のpc上のサイトから保存したテキストファイルのパス
    dct_path = 'dictionary.words.txt'
    with open(dct_path) as f:
        dct = [s.strip() for s in f.readlines()]
    
    new_dct = []
    for i in range(len(dct)):
        new_dct.append(dct[i].lower())

    # 与えられた単語のnum文字目から始まる単語を、numを増やしながら順に調べていく
    # 見つかった時点でループを抜ける
    num = 0
    checked_key = []
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
        index1,index2 = binary_search_for_index(new_dct,key,boundary)

        # 辞書中の各文字の出現回数をカウント
        for j in [index1,index2]:
            while j < len(dct) and new_dct[j][0] == key:

                dct_count = collections.Counter(new_dct[j])
                
                if compare(s_dct,dct_count) and s!=new_dct[j]:

                    # 見つかった時点でその単語を返す実装とした
                    # もともと頭文字が大文字で辞書に格納されていた場合は、一応その形で返す（そのためにnew_dctを設けたので)
                    return dct[j]
                else:
                    j+=1
        
        num += 1

    # 最後までいってもみつからなかった場合
    return "Not Found"

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description='与えられた文字列に対してAnagramを返すプログラム')
    parser.add_argument('-i','--input',help='入力として与える文字列',default='google')
    args = parser.parse_args()

    anagram = homework1_1(args.input)
    print(anagram)