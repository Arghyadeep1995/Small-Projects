from random import randint, shuffle
from time import sleep
from xlrd import open_workbook

file_name = input("Enter Filename: ")
try:
    book = open_workbook(file_name)
except FileNotFoundError:
    input("File not found. Enter any key to exit")
    exit(0)
num_winners = int(input("Enter number of winners: "))
file_to_write = "winners_list.txt"

sheet = book.sheet_by_index(0)
names = sheet.col_values(0)
total_names = len(names)

print("Shuffling names, please wait!")
for i in range(1, 10000):
    shuffle(names)
for i in range(1, randint(11, 15)):
    print("=", end="")
    sleep(1)


def check_duplicate(num, num_list):
    for it in range(0, len(num_list)):
        if num_list[it] == num:
            flag_inner = 1
            break
        else:
            flag_inner = 0
    return flag_inner


number_list = [9999999]
for i in range(1, num_winners + 1):
    number = randint(0, total_names - 1)
    flag = check_duplicate(number, number_list)
    if flag == 1:
        number = randint(0, total_names - 1)
        flag = check_duplicate(number, number_list)
        if flag == 1:
            number = randint(0, total_names - 1)
    else:
        print("\nWinner %s is %s" % (i, names[number]), end="")
        with open(file_to_write, 'a') as file:
            file.write('Winner %s is %s\n' % (i, names[number]))
        number_list.append(number)

input("\n\nCongratulations Winners!!\nPlease press any key to exit")
