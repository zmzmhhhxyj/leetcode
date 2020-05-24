from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.nodes = {}
        self.isword = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.root
        for c in word:
            if c not in t.nodes:
                t.nodes[c] = TrieNode()
            t = t.nodes[c]
        t.isword=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.root
        for c in word:
            if c not in t.nodes:
                return False
            t = t.nodes[c]
        return t.isword==True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.root
        for c in prefix:
            if c not in t.nodes:
                return False
            t = t.nodes[c]
        return True
        

obj = Trie()
# obj.insert("apple")
# param_2 = obj.search("apple")
# param_3 = obj.startsWith("app")
# print(param_2,param_3)

operations = ["insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
words = [["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]

def process(obj,operations,words):
    for i,op in enumerate(operations):
        word = words[i][0]
        if op=="insert":
            obj.insert(word)
        elif op == "search":
            print(obj.search(word))
        elif op == "startsWith":
            print(obj.startsWith(word))
    print("done!")

process(obj,operations,words)