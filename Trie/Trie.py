import pickle

class TrieNode:

    __slots__ = "children", "eow", "data"

    def __init__(self, data):
        self.children = {}
        self.eow = False
        self.data = data


class Trie:

    __slots__ = "root"

    def __init__(self):
        self.root = TrieNode("")

    def insert(self,word):
        '''
        Method to insert a word in Trie data structure
        It stores True at the end of the word and False otherwise
        :param word:
        :return: None
        '''

        current = self.root
        for i in range(len(word)):
            ch = word[i]
            try:
                current = current.children[ch]
            except:
                node = TrieNode(ch)
                current.children[ch] = node
                current = node
        current.eow = True


    def search(self,word):
        '''
        This method searches for a string in the trie structure
        It returns true only if the word exist. False even if prefix exist
        :param word:
        :return: boolean
        '''
        current = self.root
        for i in range(len(word)):
            ch = word[i]
            try:
                current.children[ch]
            except:
                return False
            current = current.children[ch]

        return current.eow



    def delete(self,word):
        self.__delete(self.root, word, 0)

    def __delete(self,current,word,index):
        if index == len(word):
            if not current.eow:
                return False
            current.eow = False
            return len(current.children) == 0

        ch = word[index]
        try:
            node = current.children[ch]
            children_empty = self.__delete(node,word,index+1)
        except:
            return False

        if children_empty:
            current.children.pop(ch,None)
            return len(current.children) == 0
        return False




def main():
    tree = Trie()
    print("~~~~~~Creating Dictionary~~~~~~")
    with open("words.txt") as dictionary:
        for word in dictionary:
            filter_word = word.strip()
            tree.insert(filter_word)
    pickle.dump(tree, open("autocomplete.p","wb"))
    print("Dictionary Created!")
   


if __name__ == "__main__":
    main()