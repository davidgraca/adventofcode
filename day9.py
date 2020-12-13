def getdata():
    mylines = []                             # Declare an empty list named mylines.
    with open ('data9.txt', 'rt') as myfile:
        str=""
        for myline in myfile:                # For each line, stored as myline,
            mylines.append(int(myline.replace("\n","")))
    return mylines

def getinvalid(numbers):
    data= getdata()
    count=0
    for i,val in enumerate(data):
        if i<numbers:continue
        sample = data[i-numbers:i]
        for j,u in enumerate(sample):
            gg= sample[:j] + sample[j+1:]
            for k,l in enumerate(gg):
                if sample[j] + gg[k]==data[i]:
                    #print(sample[j] , gg[k], data[i])
                    count+=1
                    break
        if count==0: print("none "+ str(data[i]));break
        count=0
            


getinvalid(25)