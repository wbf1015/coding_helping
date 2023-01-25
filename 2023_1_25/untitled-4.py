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
i = 0
for i in range(len(ages)):
    # new = f"{names[i]}".join(ages[i])
    new = f"{names[i]}"+" "+str(ages[i]) 
    i = i+1
    print(f'{new}')




character = input("Enter the character's name: ")
age = int(input("Enter the character's age: "))
for item in ages :
     i= 0
    if age > item:
        i = i+1
        print(f'{character} is {age} years old, and they are older than {names[i]}.')
        
    elif age < item:
        i = i+1
        print(f'{character} is {age} years old, and they are younger than {names[ i]}.')
     