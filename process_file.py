def read_file(filename):
    listOfWords = {}
    with open(filename, encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace('\n', '').split(' : ')
            listOfWords[line[0]] = line[1]
    return listOfWords

def save_as_file(listOfWords, filename):
    with open(filename, 'w', encoding='UTF-8') as file:
        for element in listOfWords:
            for word in listOfWords[element]:
                file.write(word + ' : ' + listOfWords[element][word] + '\n')
    print('Successfully Saved To File')
    
list_of_words = read_file('data\\list_of_words.txt')