special_letter = {}

with open('vn_letters.txt', 'r', encoding="UTF-8") as file:
    lines = file.readlines()
    
    for line in lines:
        letter = line.replace('\n', '').split(',')
        special_letter[letter[0]] = letter[1]