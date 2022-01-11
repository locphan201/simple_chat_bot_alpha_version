from dictionary import Nouns, Verbs, Adjectives
from process_file import read_file, save_as_file

def main():
    noun = read_file(Nouns(), 'nouns.txt')
    noun.add('a', 'test')
    save_as_file(noun.get_list_of_words(), 'nouns.txt')
    
main()
