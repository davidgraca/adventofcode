mylines = []                             # Declare an empty list named mylines.
with open ('data8.txt', 'rt') as myfile:
    str=""
    for myline in myfile:                # For each line, stored as myline,
        mylines.append(myline.replace("\n",""))

data=[]
for instruction in mylines:
    right= instruction.split(" ")[1]
    data.append([instruction[:3],int(right),False])

print(data)

def startprogram(linenumber):
    acc=0
    line= data[linenumber]
    if line[2]==True: return acc
    line[2]=True
    if line[0] =="acc": acc+= line[1]
    if line[0]=="nop" or line[0] =="acc": acc+=startprogram(linenumber +1)
    if line[0]=="jmp":  acc+=startprogram(linenumber + line[1])
    return acc


print(startprogram(0))