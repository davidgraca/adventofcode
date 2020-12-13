def getdata():
    mylines = []                             # Declare an empty list named mylines.
    with open ('data8.txt', 'rt') as myfile:
        str=""
        for myline in myfile:                # For each line, stored as myline,
            mylines.append(myline.replace("\n",""))

    data=[]
    for instruction in mylines:
        right= instruction.split(" ")[1]
        data.append([instruction[:3],int(right),False])
    return data

def navigate(mydata, linenumber,end):
    acc=0
    if linenumber>= len(mydata): 
        return False, acc, True

    line= mydata[linenumber]
    loop=False
    if line[2]==True: return True,acc,False
    line[2]=True
    if line[0] =="acc": acc+= line[1]
    if line[0]=="nop" or line[0] =="acc": loop,acct,end=navigate(mydata,linenumber +1,end);  acc+=acct
    if line[0]=="jmp":  loop,acct,end=navigate(mydata,linenumber + line[1],end);  acc+=acct
    return loop, acc,end


def getchange():
    tryset = set({})
    loop=True
    acc=0
    orignal= getdata().copy()
    numrows=len(orignal)
    for i in range(0,numrows):
        tempdata= getdata()
        if tempdata[i][0]== "jmp" or tempdata[i][0]== "nop" and loop and i not in tryset:
            if tempdata[i][0]== "jmp": 
                tempdata[i][0]="nop"
            else:
                tempdata[i][0]="jmp"
            tryset.add(i)
            loop, acc,end = navigate(tempdata,0,False)
            if end == True:
                print(acc)
                break
    print(acc)
           

getchange()