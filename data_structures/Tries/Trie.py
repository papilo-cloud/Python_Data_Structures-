class TrieNode:
    def __init__(self) -> None:
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        current_node = self.root
        
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node
                current_node = new_node
        current_node.children['*'] = None
        
    def search(self, word):
        current_node = self.root
        
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None
        return current_node
    
    def collect_all_words(self, node=None, word='', words=[]):
        current_node = node or self.root
        
        for (key, collection_node) in current_node.children.items():
            if key == '*':
                words.append(word)
            else:
                self.collect_all_words(collection_node, word+key, words)
        return words
    
    def autocomplete(self, prefix):
        current_node = self.search(prefix)
        
        if not current_node:
            return None
        return self.collect_all_words(current_node)