# -*- coding: UTF-8 -*-

def make_map(data_path):
    '''
    指定したパスにあるファイルからフォロー関係の辞書を獲得
    '''
    f = open(data_path)
    lines = f.readlines()

    follow_map = {}

    for line in lines:

        pair_id = [int(i) for i in line.split()]
        key = pair_id[0]
        follower = pair_id[1]

        if follow_map.get(key) != None:
            follow_map[key].append(follower)
        else:
            follow_map[key] = [follower]
    
    return follow_map


def fix_follow_map(follow_map):
    '''
    フォロー関係は無向グラフとして扱うので、
    必ず相互フォローになっていると考える
    
    そうなるように、お互いがお互いのidを必ず含むように修正する

    そうでないとあとで不都合なので
    '''
    for key in follow_map:
        follower = follow_map[key]
        for f in follower:
            k = follow_map[f]
            if not key in k:
                k.append(key)
                follow_map[f] = k
    
    return follow_map

def get_ids_from_name(data_path,start_name,goal_name):
    '''
    指定したパスにあるファイルを読み込み、
    起点および終点となる人のニックネームからそのIDを取得し辞書に格納して返す関数
    '''

    f = open(data_path)
    lines = f.readlines()
    id_dct = {}

    for line in lines:

        if len(id_dct) == 2:
            break

        tmp = line.split()
        if tmp[1] == start_name:
            id_dct['start_id'] = int(tmp[0])
        if tmp[1] == goal_name:
            id_dct['goal_id'] = int(tmp[0])

    return id_dct


def bfs(follow_map,id_dct):

    start_id = id_dct['start_id']
    goal_id = id_dct['goal_id']
    queue = deque(follow_map[start_id])

    visited = {start_id:'checked'}

    for q in queue:
        visited[q] = 'checked'

    while queue:

        ID = queue.popleft()

        if visited.get(ID) == None:
            if ID == goal_id:
                print('Reached!!')
                return
            else:
                visited[ID] = 'checked'
                followers = follow_map[ID]
                queue.append(followers)

    return

def advanced_bfs(follow_map,id_dct):
    '''
    見つかったときに起点から何ノード目かも調べる
    正解ルートを全て探して距離の短い順に並べたリストを返す
    途中のノードも記憶していく
    '''

    visited = {}

    start_id = id_dct['start_id']
    goal_id = id_dct['goal_id']
    print('start:',start_id,'/ goal:',goal_id)

    visited[start_id] = 'checked'

    queue = deque()

    for ID in follow_map[start_id]:

        id_route = [ID,[start_id]]
        queue.append(id_route)

    print('queue:',queue)

    ways = {}

    while queue:

        id_route = queue.popleft()

        ID = id_route[0]
        route = id_route[1]

        if visited.get(ID) == None:

            print('route:',route)
            print('id_route:',id_route)

            if ID == goal_id:
                print('Reached')
                route.append(ID)
                key = len(route)
                ways[key] = route

            else:
                visited[ID] = 'checked'
                route.append(ID)
                followers = follow_map[ID]
                for f in followers:
                    id_route = [f,route]
                    queue.append(id_route)
        else:
            pass

    ways = sorted(ways.items())

    return ways

def get_min_and_max_route(ways):
    '''
    見つかったルートのリストから最短距離とそのルート、最長距離とそのルートを返す関数
    '''

    min_dis = ways[0][0]
    min_route = ways[0][1]

    max_dis = ways[-1][0]
    max_route = ways[-1][1]

    return min_dis,min_route,max_dis,max_route

def dfs(follow_map,id_dct):
    return False

def advanced_dfs(follow_map,id_dct):
    return False

if __name__ == '__main__':

    from collections import deque

    follow_map = make_map('data/class/links.txt')
    follow_map = fix_follow_map(follow_map)

    id_dct = get_ids_from_name('data/class/nicknames.txt','debra','adrian')

    for key in follow_map:
        print(key)
        print(follow_map[key])
        print('\n')

    
    '''
    follow_map = {1:[3,5,6],2:[4,5],3:[1,6],4:[2,6],5:[1,2],6:[1,3,4]}
    id_dct = {'start_id':1,'goal_id':2}
    '''

    ways = advanced_bfs(follow_map,id_dct)

    print(ways)

    #if len(ways) >= 1:
        #min_dis,min_route,max_dis,max_route = get_min_and_max_route(ways)
        #print(min_dis,min_route)
        #print(max_dis,max_route)