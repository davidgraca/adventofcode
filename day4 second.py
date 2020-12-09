from os import replace
import re


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
    if len(firstchars)>= len(expected) and all(item in firstchars for item in expected):
        dict = {}
        list(map(lambda y : dict.update({y[0:3]:y[4:]}),passport))
    
        heigth = False
        if dict['hgt'][len(dict['hgt'])-2:] =='in':
            try:
                value = int(dict['hgt'][:len(dict['hgt'])-2])
                if 59 <= value<=76:heigth=True
            except:
                heigth=False
        if dict['hgt'][len(dict['hgt'])-2:] =='cm':
            try:
                value = int(dict['hgt'][:len(dict['hgt'])-2])
                if 150 <= value<=193:heigth=True
            except:
                heigth=False

        byr=1920<= int(dict['byr'])<=2002
        iyr= 2010 <= int(dict['iyr'])<=2020
        eyr = 2020 <=int(dict['eyr'])<=2030
        hcl = re.search("^\#[0-9a-f]{6}$", dict["hcl"])!= None
        pid=re.search("^[0-9]{9}$", dict["pid"])!= None
        ecl = re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", dict["ecl"])!= None
        if heigth and byr and iyr and eyr and hcl and ecl and pid:
            valid+=1

print(valid)                           # Print the list.