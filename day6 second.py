mylines = []                             # Declare an empty list named mylines.
with open ('data6.txt', 'rt') as myfile:
    countt=0
    common=[]
    for myline in myfile:
        
        if myline != "\n": 
            answer = myline.replace("\n","")
            common.append(set([c for c in answer]))
        else:
            countt+=len(common[0].intersection(*common[1:]))
            common=[]
    countt+=len(common[0].intersection(*common[1:]))

print(countt)

