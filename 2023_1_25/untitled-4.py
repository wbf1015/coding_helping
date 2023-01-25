import sys

names = [
    "Frodo",
    "Samwise",
    "Gandalf",
    "Legolas",
    "Gimli",
    "Aragorn",
    "Boromir",
    "Merry",
    "Pippin",
]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]

# i = 0
# for i in range(len(ages)):
#     # new = f"{names[i]}".join(ages[i])
#     new = f"{names[i]}"+" "+str(ages[i])
#     i = i+1
#     print(f'{new}')


character = input("Enter the character's name: ")
age = int(input("Enter the character's age: "))

elder = []
younger = []

if age < 0:
    print('Invalid age')
    sys.exit(0)

for i in range(len(ages)):
    # 输入的年龄比数组当前这个人的年龄小
    if age < ages[i]:
        elder.append(names[i])
    if age > ages[i]:
        younger.append(names[i])

print('%s is %d years old' % (character, age), end=",")
print('and they are older than ', end="")
for i in range(len(younger)):
    print(younger[i], end="")
    if i != len(younger) - 1:
        print(',', end='')

print('')
print('%s is %d years old' % (character, age), end=",")
print('and they are younger than ', end="")
for i in range(len(elder)):
    print(elder[i], end="")
    if i != len(elder) - 1:
        print(',', end='')