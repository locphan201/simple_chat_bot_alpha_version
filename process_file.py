def read_file(listOfWords, filename):
    with open(filename, encoding='UTF-8') as file:
        line = file.readline().replace('\n', '').split(' : ')
        listOfWords.add(line[0], line[1])
    return listOfWords

def save_as_file(listOfWords, filename):
    with open(filename, 'w', encoding='UTF-8') as file:
        for element in listOfWords:
            for word in listOfWords[element]:
                file.write(word + ' : ' + listOfWords[element][word] + '\n')
    print('Successfully Saved To File')