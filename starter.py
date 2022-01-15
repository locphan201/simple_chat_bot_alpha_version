from process_file import list_of_words
from topic import *

def greet():
    from datetime import datetime
    now = datetime.now()
    hour = now.hour
    greeting = ''
    if 6 < hour < 10:
        greeting = 'Chào buổi sáng!'
    elif hour < 14:
        greeting = 'Chào buổi trưa!'
    elif hour < 18:
        greeting = 'Chào buổi chiều!'
    elif hour < 22:
        greeting = 'Chào buổi tối!'
    else:
        greeting = 'Sorry, Simi is sleeping now!\nSimi is undermaintenance!'
    print('Simi:', greeting)

def indicate_words(sentence):
    main_idea = []
    ideas = sentence.lower().split(',')
    key = list_of_words.keys()
    for idea in ideas:
        idea = idea.split(' ')
        for i in range(len(idea)):
            if any(element in idea[i] for element in key):
                main_idea.append(idea[i])
    return main_idea

def start():
    greet()
    current_topic = Topic('greeting.txt')
    sentence = ''
    while True:
        sentence = input('You: ')
        break