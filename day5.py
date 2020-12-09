
def seatId(data):
    up = 0
    low = 128

    for c in data[:len(data)-3]:
        if(c=='F'):low= low - (low-up)/2
        if(c=='B'):up= up +(low - up)/2
        if(c=='L'):up= (up - low)/2
        if(c=='R'):up= (up - low)/2

    #print(up, low-1)

    lseat=0
    hseat=8

    for c in data[len(data)-3:]:
        if(c=='L'):hseat= hseat - (hseat-lseat)/2
        if(c=='R'):lseat= lseat +(hseat - lseat)/2
    #print(up, hseat-1)
    return (up*8)+hseat-1


mylines = []                             # Declare an empty list named mylines.
with open ('datad5.txt', 'rt') as myfile:
    lines= list(myfile)
    mylines= map(lambda x: seatId(x.replace("\n","")),lines)

print(max(mylines))