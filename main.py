from dictionary import Vocabulary

def read_file(listOfWords):
    with open('data.txt', encoding='UTF-8') as file:
        line = file.readline().replace('\n', '').split(' : ')
        listOfWords.add(line[0], line[1])
    return listOfWords

def main():
    listOfWords = Vocabulary()
    
    listOfWords = read_file(listOfWords)
    # listOfWords.print()
    listOfWords.find('tôi')
    listOfWords.find('anh')
    listOfWords.find('em')
    
main()
