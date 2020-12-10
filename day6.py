mylines = []                             # Declare an empty list named mylines.
with open ('data6.txt', 'rt') as myfile:
    str=""
    for myline in myfile:                # For each line, stored as myline,
        if myline != "\n": 
            str+=myline.replace("\n","")
        else:
            mylines.append(str.replace("\n",""))    
            str=""       # add its contents to mylines.
    mylines.append(str)

different = []
for answer in mylines:
    different.append(set([c for c in answer]))
print(sum(map(lambda x: len(x), different)))

