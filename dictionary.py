from vn_letters import special_letter

class Vocabulary:
    def __init__(self):
        self.alphabet = {}
        self.setup()
        
    def setup(self):        
        for i in range(97, 123):
            self.alphabet[chr(i)] = {}
            
            if i == 97:
                self.alphabet['ă'] = {}
                self.alphabet['â'] = {}
            elif i == 100:
                self.alphabet['đ'] = {}
            elif i == 101:
                self.alphabet['ê'] = {}
            elif i == 111:
                self.alphabet['ô'] = {}
                self.alphabet['ơ'] = {}
            elif i == 117:
                self.alphabet['ư'] = {}
        
    def add(self, word, definition):
        if word == '':
            print('Cannot pass an empty word')
            return
        
        if special_letter.get(word[0]):
            special_case(word[0])
        self.alphabet[word[0]][word] = definition
    
    def find(self, word):
        find_word(self, word, 'data.txt')
    
    def get_list_of_words(self):
        return self.alphabet
    
    def print(self):
        for element in self.alphabet:
            print(element, ':', self.alphabet[element])

class Nouns(Vocabulary):
    def __init__(self):
        super().__init__()

    def find(self, word):
        find_word(self, word, 'nouns.txt')
        
class Verbs(Vocabulary):
    def __init__(self):
        super().__init__()

    def find(self, word):
        find_word(self, word, 'verbs.txt')
        
class Adjectives(Vocabulary):
    def __init__(self):
        super().__init__()

    def find(self, word):
        find_word(self, word, 'adjectives.txt')
        
def special_case(letter):
    return special_letter[letter]

def find_word(self, word, filename):
    if word == '':
        print('Cannot find an empty word')
        return []
    elif self.alphabet[word[0]].get(word):
        return [self.alphabet[word[0]].get(word)]
    else:
        print('\'', word, '\' is not in the database')
        if (input('Add this word to the database? (Y/N) ')).lower() == 'y':
            definition = input('Definition: ')
            self.add(word, definition)
            with open(filename, 'a') as file:
                file.write(word + ' : ' + definition + '\n')