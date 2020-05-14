from collections import OrderedDict

class Node:
    def __init__(self):
        self.children = OrderedDict()
        self.terminating = False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.getNode()
        

    def getNode(self):
        return Node()
    
    def getIndex(self, char):
        return ord(char) - ord('a')
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        length = len(word)
        for i in range(len(word)):
            index = self.getIndex(word[i])
            if index not in root.children:
                root.children[index] = self.getNode()
            root = root.children.get(index)
        root.terminating = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        length = len(word)
        for i in range(len(word)):
            index = self.getIndex(word[i])
            if index not in root.children:
                return False
            root = root.children.get(index)
        return root.terminating == True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        length = len(prefix)
        for i in range(len(prefix)):
            index = self.getIndex(prefix[i])
            if index not in root.children:
                return False
            root = root.children.get(index)
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
