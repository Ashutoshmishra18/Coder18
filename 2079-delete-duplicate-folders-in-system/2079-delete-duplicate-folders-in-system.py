from collections import defaultdict

class Trie:
    def __init__(self, id=""):
        self.id = id
        self.links = {}
        self.mark = False

    def insert(self, path):
        node = self
        for s in path:
            if s not in node.links:
                node.links[s] = Trie(s)
            node = node.links[s]

class Solution:
    def __init__(self):
        self.trie = Trie()
        self.mp = {}
        self.ans = []

    def serial(self, node):
        if not node.links:
            return ""

        sorted_items = sorted(node.links.items())
        dir_str = ""

        for id_, child in sorted_items:
            dir_str += "(" + id_ + self.serial(child) + ")"

        if dir_str in self.mp:
            self.mp[dir_str].mark = True
            node.mark = True
        else:
            self.mp[dir_str] = node

        return dir_str

    def to_ans(self, node, path):
        for id_, child in node.links.items():
            if child.mark:
                continue
            path.append(id_)
            self.ans.append(list(path))
            self.to_ans(child, path)
            path.pop()

    def deleteDuplicateFolder(self, paths):
        for path in paths:
            self.trie.insert(path)

        self.serial(self.trie)
        self.to_ans(self.trie, [])
        return self.ans
