from os import replace


mylines = []                             # Declare an empty list named mylines.
with open ('data.txt', 'rt') as myfile:
    str=""
    for myline in myfile:                # For each line, stored as myline,
        if myline != "\n": 
            str+=myline.replace("\n"," ")
        else:
            mylines.append(str.replace("\n"," "))    
            str=""       # add its contents to mylines.
    mylines.append(str)
expected = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl','pid']

valid=0
passports= list(map(lambda x: x.split(),mylines))
for passport in passports:
    firstchars=list(map(lambda y : y[0:3],passport))
    if len(firstchars)>= len(expected) and all(item in firstchars for item in expected):valid+=1

print(valid)                           # Print the list.