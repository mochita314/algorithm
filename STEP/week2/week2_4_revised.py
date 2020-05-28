import sys

# Cache is a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.
class Cache:
  # Initializes the cache.
  # |n|: The size of the cache.
  def __init__(self, n):

    self.oldest = None
    self.newest = None
    self.size = n
    self.cache = [[None,None,None,None] for i in range(self.size*1000)]
    self.mod = self.size*1000
    self.cnt = 0

  def url_to_index(self,url):
    # urlを数字のindexに変換

    key = 0
    for s in url:
        key += ord(s)

    return key
  
  def disjoint(self,a,b):
    
    lmt = min(a,b)

    for i in range(2,lmt+1):
        if a % i == 0 and b % i == 0:
          return False
    
    return True

  def h1(self,key):

    key = key % self.mod
    
    return key
  
  def h2(self,key):

    tmp = 1 + key % (self.mod-1)

    while not self.disjoint(self.h1(key),tmp):
      tmp += 1
    
    key = tmp

    return key

  def h(self,key,i):
    # iは衝突回数
    # 衝突が起きた場合、h1に対して別のハッシュ関数h2を組み合わせて別のキーを探す

    key = (self.h1(key) + i * self.h2(key)) % self.mod

    return key
  
  def find_key(self,url):
  
    n = self.size

    '''
    flag is set to be 
    0 : when the url is not in the cache and cache is not full.
    1 : when the url is not in cache and cache is full.
    2 : when the url is already in the cache.
    '''

    key = -1
    flag = 0

    i = 0
    while True:
    
      # 最大（配列の長さ）回iを更新すれば、同じkeyを重複して参照することなく、全てのkeyを参照できるようにh2に制約をかけている

      key = self.h(self.url_to_index(url),i)

      if self.cache[key] == [None,None,None,None]:

        if self.cnt < self.size:
          # そこが空いている
          return key,flag
        else:
          flag = 1
          # 空いてるけど容量がいっぱい
          return key,flag

      elif self.cache[key][0] == url:
        # そこにすでに格納されている
        flag = 2
        return key,flag
      
      else:
        i+=1

  # Access a page and update the cache so that it stores the most
  # recently accessed N pages. This needs to be done with mostly O(1).
  # |url|: The accessed URL
  # |contents|: The contents of the URL
  def access_page(self, url, contents):
  
    # 新しいurlをcacheに追加、cacheの親子関係の修正

    # 親のkeyを見つけて、そのvalueに子情報（新しく追加するurl）を追加する
    # 追加するkeyのvalueのほうにも、親のurlを追加する
    key,flag = self.find_key(url)

    # flagの値に応じて場合分けをして、親子関係の修正・新しいurlの登録をおこなう
    # 関数にまとめて抽象化できないか考えたが、むしろ煩雑になってしまったのでこのままにしておく

    if flag == 0:
      self.cnt += 1
      # when the url is not in the cache and the cache is not full

      new_parent_url = self.newest

      self.newest = url

      if new_parent_url != None:

        self.cache[key] = [url,contents,new_parent_url,0]

        new_parent_key,flag2 = self.find_key(new_parent_url)
        self.cache[new_parent_key][3] = url

        if self.oldest == None:
          self.oldest = new_parent_url

      else:

        self.cache[key] = [url,contents,0,0]
        self.oldest = url

    elif flag == 1:
      self.cnt += 1
      # when the url is not in cache and cache is full.

      oldest_url = self.oldest
      oldest_key,flag2 = self.find_key(oldest_url)

      second_oldest = self.cache[oldest_key][3]

      second_oldest_key,flag2 = self.find_key(second_oldest)
      self.cache[second_oldest_key][2] = 0

      new_parent_url = self.newest
      new_parent_key,flag2 = self.find_key(new_parent_url)
      self.cache[new_parent_key][3] = url

      self.cache[oldest_key] = [None,None,None,None]
      self.cache[key] = [url,contents,new_parent_url,0]

      self.newest = url
      self.oldest = second_oldest
    
    else:
      # when the url is already in the cache

      pre_parent_url = self.cache[key][2]
      pre_child_url = self.cache[key][3]

      if pre_child_url != 0:

        if pre_parent_url != 0:
          pre_parent_key,flag2 = self.find_key(pre_parent_url)
          self.cache[pre_parent_key][3] = pre_child_url

        pre_child_key,flag2 = self.find_key(pre_child_url)
        self.cache[pre_child_key][2] = pre_parent_url

        new_parent_url = self.newest
        new_parent_key,flag2 = self.find_key(new_parent_url)
        self.cache[new_parent_key][3] = url

        self.cache[key] = [url,contents,new_parent_url,0]
        self.newest = url

        if pre_parent_url == 0:
          # when the url was the oldest
          self.oldest = pre_child_url
      
      else:
        # when the url is newest now
        pass

  # Return the URLs stored in the cache. The URLs are ordered
  # in the order in which the URLs are mostly recently accessed.
  def get_pages(self):
    
    #for i in range(len(self.cache)):
      #if self.cache[i] != None:
        #print(self.cache)

    '''
    この関数の計算量はO(X)になっているが、求められている機能（urlにアクセスしたときそれがキャッシュ内にあるかを確認し、
    ある場合は最新ページにそれを移動し、なかったら最古のものを捨てて追加）はほぼ（衝突が起き続けない限り）O(1)で実現できているので良し
    '''

    pages = []

    if self.newest == None:
      return pages
    
    pages.append(self.newest)
    cnt = 1

    while cnt < self.size:

      key,flag = self.find_key(pages[-1])
      parent_page = self.cache[key][2]

      if parent_page == 0:
        break
      else:
        pages.append(parent_page)
        cnt += 1

    return pages

# Does your code pass all test cases? :)
def cache_test():
  # Set the size of the cache to 4.
  cache = Cache(4)
  # Initially, no page is cached.
  equal(cache.get_pages(), [])
  # Access "a.com".
  cache.access_page("a.com", "AAA")
  # "a.com" is cached.
  equal(cache.get_pages(), ["a.com"])
  # Access "b.com".
  cache.access_page("b.com", "BBB")
  # The cache is updated to:
  #   (most recently accessed)<-- "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["b.com", "a.com"])
  # Access "c.com".
  cache.access_page("c.com", "CCC")
  # The cache is updated to:
  #   (most recently accessed)<-- "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["c.com", "b.com", "a.com"])
  # Access "d.com".
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
  # Access "d.com" again.
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
  # Access "a.com" again.
  cache.access_page("a.com", "AAA")
  # The cache is updated to:
  #   (most recently accessed)<-- "a.com", "d.com", "c.com", "b.com" -->(least recently accessed)
  equal(cache.get_pages(), ["a.com", "d.com", "c.com", "b.com"])
  cache.access_page("c.com", "CCC")
  equal(cache.get_pages(), ["c.com", "a.com", "d.com", "b.com"])
  cache.access_page("a.com", "AAA")
  equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
  cache.access_page("a.com", "AAA")
  equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
  # Access "e.com".
  cache.access_page("e.com", "EEE")
  # The cache is full, so we need to remove the least recently accessed page "b.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "e.com", "a.com", "c.com", "d.com" -->(least recently accessed)
  equal(cache.get_pages(), ["e.com", "a.com", "c.com", "d.com"])
  # Access "f.com".
  cache.access_page("f.com", "FFF")
  # The cache is full, so we need to remove the least recently accessed page "c.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "f.com", "e.com", "a.com", "c.com" -->(least recently accessed)
  equal(cache.get_pages(), ["f.com", "e.com", "a.com", "c.com"])
  print("OK!")

# A helper function to check if the contents of the two lists is the same.
def equal(list1, list2):
  assert(list1 == list2)
  for i in range(len(list1)):
    assert(list1[i] == list2[i])

if __name__ == "__main__":
  cache_test()
