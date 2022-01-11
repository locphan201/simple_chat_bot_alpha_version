from dictionary import Nouns, Verbs, Adjectives

def read_file(listOfWords, filename):
    with open(filename, encoding='UTF-8') as file:
        line = file.readline().replace('\n', '').split(' : ')
        listOfWords.add(line[0], line[1])
    return listOfWords

def main():
    noun = Nouns()
    noun.add('a', 'test')
    noun.print()
    
main()
