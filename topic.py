from dictionary import *

class Topic:
    def __init__(self, filename):
        self.nouns = Nouns()
        self.verbs = Verbs()
        self.adjs  = Adjectives()
        self.read_file(filename)
    
    def read_file(self, filename):
        current_list = self.nouns
        with open('data\\' + filename, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            for line in lines:
                if line == 'nouns\n':
                    current_list = self.nouns
                elif line == 'verbs\n':
                    current_list = self.verbs
                elif line == 'adjs\n':
                    current_list = self.adjs
                else:
                    current_list.add(line.replace('\n', ''))
                    
    def print(self):
        self.nouns.print()
        self.verbs.print()
        self.adjs.print()