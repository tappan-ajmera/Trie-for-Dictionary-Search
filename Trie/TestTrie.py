import pickle
from Trie import Trie,TrieNode

def main():
    '''
    Function made for testing the Trie Data Structure
    :return:
    '''

    tree = pickle.load(open('autocomplete.p','rb'))
    print("Type :q to exit")
    word = ""
    while word != ":q":
        word = input().strip()
        print(tree.search(word))


if __name__ == "__main__":
    main()

