import time
from datetime import datetime
from dictionary import Vocabulary

#-------------------------------------------------#
#-This is a tester for performance and efficiency-#
#-------------------------------------------------#

# Times to loop
iterator = 1000000
# Block of codes needs to test
def code_for_test():
    s = Vocabulary()

# Please don't change anything below
def save_testing_log(prompt, average_time, note):
    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S %d/%m/%Y")
    with open('testing_log.txt', 'a') as file:
        file.write(dt_string + '\n')
        file.write(' - ' + prompt + '\n')
        file.write(' - Iterator: ' + str(iterator) + '\n')
        file.write(' - Average time: ' + str(average_time) + '\n')
        file.write(' - Note: ' + note + '\n\n')

def main():
    prompt = input('Kind of test: ')
    
    t0 = time.time()
    for i in range(iterator):
        code_for_test()
    t1 = time.time()
    for i in range(iterator):
        code_for_test()
    t2 = time.time()

    average = round(((t1-t0) + (t2-t1))/2, 3)
    print(average)
    note = input('Note after testing: ')
    save_testing_log(prompt, average, note)
    print('Successfully Save This Test')

main()