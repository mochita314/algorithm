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

    while queue:

        ID = queue.popleft()

        if visited.get(ID) == None:
            if ID == goal_id:
                print('Reached!!')
                return
            else:
                visited[ID] = 'checked'
                followers = follow_map[ID]
                queue.extend(followers)

    return

'''
def advanced_bfs(follow_map,id_dct):

    start_id = id_dct['start_id']
    goal_id = id_dct['goal_id']
    
    queue = deque()
    for f in follow_map[start_id]:
        queue.append([f,[start_id]])

    visited = {start_id:'checked'}

    ways = {}

    while queue:

        ID_route = queue.popleft()
        ID = ID_route[0]

        # そこまでのルート
        route = ID_route[1]

        # そのIDを取り出した=訪れたときにrouteに追加する
        route.append(ID)
        
        if visited.get(ID) == None:
    
            if ID == goal_id:
                print('Reached!!')
                key = len(route)
                ways[key] = route
            else:
                visited[ID] = 'checked'
                followers = follow_map[ID]
                for f in followers:
                    queue.append([f,route])
        
        #route = None # 必要ないはずだけど挙動がおかしいから初期化してみる

    return ways
'''
def advanced_bfs(follow_map,id_dct):

    start_id = id_dct['start_id']
    goal_id = id_dct['goal_id']

    queue = deque()

    for f in follow_map[start_id]:
        queue.append([f,[start_id]])

    visited = {start_id:'checked'}

    ways = {}

    while queue:

        ID_route = queue.popleft()
        ID = ID_route[0]
        route = ID_route[1]

        if visited.get(ID) == None:
            if ID == goal_id:
                print('Reached!!')
                new_route = []
                for r in route:
                    new_route.append(r)
                new_route.append(ID)
                key = len(new_route)
                if ways.get(key) == None:
                    ways[key] = []
                ways[key].append(new_route)
            else:
                visited[ID] = 'checked'
                followers = follow_map[ID]
                new_route = []
                for r in route:
                    new_route.append(r)
                new_route.append(ID)
                for f in followers:
                    if visited.get(f) == None:
                        queue.append([f,new_route])

    return ways

def dfs(follow_map,pos,goal,dis,visited):
 
    for f in follow_map[pos]:
        if f == goal:
            print('Reached',dis)
            return dis
        elif visited.get(f) == None:
            visited[f] = 'checked'
            dfs(follow_map,f,goal,dis+1,visited)

def get_min_and_max_route(ways):
    '''
    見つかったルートのリストから最短距離とそのルート、最長距離とそのルートを返す関数
    '''

    min_dis = ways[0][0]
    min_route = ways[0][1]

    max_dis = ways[-1][0]
    max_route = ways[-1][1]

    return min_dis,min_route,max_dis,max_route


if __name__ == '__main__':

    from collections import deque

    follow_map = make_map('data/class/links.txt')
    follow_map = fix_follow_map(follow_map)

    id_dct = get_ids_from_name('data/class/nicknames.txt','debra','adrian')
    ways = advanced_bfs(follow_map,id_dct)
    print(ways)

    pos = id_dct['start_id']
    goal = id_dct['goal_id']
    ways = dfs(follow_map,pos,goal,0,{pos:'checked'})