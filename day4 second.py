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
        tt =re.search("[1920-2002]",dict['byr'])
        if re.search("[1920-2002]",dict['byr'])!= None and re.search("[2010-2020]",dict['iyr'])!= None and re.search("[2020-2030]",dict['eyr'])!= None and re.search("^([150-193]cm|[59-76]in)$",dict['hgt'])!= None and re.search("^#[0-9a-f]{6}", dict["hcl"])!= None and re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", dict["hcl"])!= None and re.search("^#[0-9]{9}", dict["pid"])!= None:
            valid+=1
re.search("([150-193]cm)|([59-75])",dict['hgt'])
print(valid)                           # Print the list.