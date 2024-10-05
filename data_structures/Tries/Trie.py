class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

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
        current_node.is_word = True
    
    def find(self, word):
        node = self.root
        for char in word:
            if node.children.get(char):
                node = node.children[char]
            else:
                return None
        return node
        
    def search(self, word):
        node = self.find(word)
        return node and node.is_word
    
    def is_prefic(self, prefix):
        return self.find(prefix)
    
    def collect_all_words(self, node=None, word='', words=[]):
        current_node = node or self.root
        
        for (key, collection_node) in current_node.children.items():
            if key == True:
                words.append(word)
            else:
                self.collect_all_words(collection_node, word+key, words)
        return words
    
    def autocomplete(self, prefix):
        current_node = self.search(prefix)
        
        if not current_node:
            return None
        return self.collect_all_words(current_node)
    
    def autocorrect(self, word):
        current_node = self.root
        word_found_so_far = ''
        
        for char in word:
            if current_node.children.get(char):
                word_found_so_far += char
                current_node = current_node.children[char]
            else:
                return word_found_so_far + self.collect_all_words(current_node)[0]
        return word