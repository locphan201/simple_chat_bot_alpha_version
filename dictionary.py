class Vocabulary:
    def __init__(self):
        self.alphabet = []
        
    def add(self, word):
        if word == '':
            print('Cannot pass an empty word')
            return
        self.alphabet.append(word)
    
    def get_list_of_words(self):
        return self.alphabet
    
    def print(self):
        for element in self.alphabet:
            print(element)

class Nouns(Vocabulary):
    def __init__(self):
        super().__init__()
        
class Verbs(Vocabulary):
    def __init__(self):
        super().__init__()
        
class Adjectives(Vocabulary):
    def __init__(self):
        super().__init__()