import sys
import random

filename = "klingon-english.txt"
filemode = "r"
file = open(filename, filemode)
new_flie = file.readlines()
file.close()


# [start,end]
def genRandom(start, end):
    return random.randint(start, end)


dictionary = {}
consonant = ["b", "ch", "D", "gh", "H", "j", "l", "m", "n", "p", "q", "Q", "r", "S", "t", "v", "w", "y", "'"]
for i in new_flie:
    split_list = i.split('|')  # breaking the left and right side part of each line
    print(split_list)
    dictionary[split_list[0]] = split_list[1].strip()  # storing in as left side as key and right side as value

for key, value in dictionary.items():
    print('key: ' + key, end='   ')
    print('value:  ' + value)

# taking user input until it is valid

while True:

    while True:
        name = input('Which consonant do you want to work with ? ')
        if name not in consonant:
            print('Please enter a valid consonant:  ')
        else:
            break

    # finding the key that starts with the given consonant
    # for i in dictionary:
    #     if i.startswith(name):
    #         word = dictionary[i]
    #         key = i

    for key, value in dictionary.items():
        if key.startswith(name):
            count = 3
            while count > 0:
                print('How do you translate ' + str(value) + ' to Klingon? You have ' + str(count) + ' attempts left. ')
                if count == 2:
                    ss = ""
                    ss = ss.center(len(key), '*')
                    t = list(ss)
                    t[0] = key[0]
                    t[len(key) - 1] = key[len(key) - 1]
                    ss = ''.join(t)
                    print('Hint:' + ss)
                if count == 1:
                    ss = ""
                    ss = ss.center(len(key), '*')
                    t = list(ss)
                    t[0] = key[0]
                    t[len(key) - 1] = key[len(key) - 1]
                    index = genRandom(1, len(key) - 2)
                    t[index] = key[index]
                    ss = ''.join(t)
                    print('Hint:' + ss)
                s = input()
                if s == key:
                    print('correct')
                    sys.exit()  # 我觉得题目是这个意思 就是正确了才能退出，如果我理解错了你再改改
                else:
                    count -= 1
                    print('Sorry, you\'re wrong!')
                    if count == 0:
                        print('The correct answer is ' + key)
                        sys.exit()
