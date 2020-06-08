def make_map(data_path):
    '''
    make dictionary with 
     key: ID number
     value: IDs of those who are followed by the member with key ID
    from the file in data_path
    '''
    follow_map = {}
    f = open(data_path)
    lines = f.readlines()
    for line in lines:
        pair_id = [int(i) for i in line.split()]
        key = pair_id[0]
        follower = pair_id[1]
        if follow_map.get(key) != None:
            follow_map[key].append(follower)
        else:
            follow_map[key] = [follower]
    return follow_map

def get_ids_from_name(data_path,start_name,goal_name):
    f = open(data_path)
    lines = f.readlines()
    id_dct = {}
    for line in lines:
        if len(id_dct) == 2:
            break
        tmp = line.split()
        if tmp[1] == start_name:
            id_dct[start_id] = int(tmp[0])
        if tmp[1] == goal_name:
            id_dct[goal_id] = int(tmp[1])
    return id_dct

def bfs(follow_map,id_dct):
    visited = {}
    return False

def dfs(follow_map,id_dct):
    return False

if __name__ == '__main__':
    follow_map = make_map('data/class/links.txt')
    get_ids_from_name('data/class/links.txt','a','b')
