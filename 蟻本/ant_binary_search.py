# -*- coding : UTF-8 -*-

# binary_search_tree.py
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
class BinarySearchTree:
    def __init__(self, key):
        self.root = Node(key)
 
    def search(self, key):
        node = self.root
        while node:
            if node.key == key:
                print("Found!")
                return node
            elif node.key > key:
                node = node.left
            else:
                node = node.right
        return None
 
    def insert(self, key):
        node = self.root
        while node:
            parent = node
            if node.key == key:
                print("Data already exists.")
                return
            elif node.key > key:
                node = node.left
                flag = "left"
            else:
                node = node.right
                flag = "right"
        new = Node(key)
        if flag == "left":
            parent.left = new
        else:
            parent.right = new
 
    def deletemin(self, node):
        parent = node
        tmp = node.right
        while tmp.left:
            parent = tmp
            tmp = tmp.left
        parent.right = tmp.right
        return tmp
 
    def delete(self, key):
        node = self.root
        parent = node
        flag = None
        while node:
            if node.key == key:
                if node.left == None and node.right == None:
                    if flag == "left":
                        parent.left = None
                    else:
                        parent.right = None
                elif node.left == None:
                    if flag == "left":
                        parent.left = node.right
                    else:
                        parent.right = node.right
                elif node.right == None:
                    if flag == "left":
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    tmp = self.deletemin(node)
                    if flag == "left":
                        parent.left = tmp
                    else:
                        parent.right = tmp
                    tmp.right = node.right
                    tmp.left = node.left
            parent = node
            if node.key > key:
                node = node.left
                flag = "left"
            else:
                node = node.right
                flag = "right"
 
    def inorder(self, tree):
        tmp = tree
        if tmp == None:
            return
        else:
            self.inorder(tmp.left)
            print(tmp.key)
            self.inorder(tmp.right)
 
t = BinarySearchTree(4)
t.insert(2)
t.insert(1)
t.insert(3)
t.insert(6)
t.insert(5)
t.insert(7)

t.search(5)
"""
print("delete 6")
t.delete(6)
print("print data...")
t.inorder(t.root)
"""