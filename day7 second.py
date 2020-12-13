import re
from typing import NoReturn
class Bag:
    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            self.number= args[0]
            self.name=args[1]
        if len(args)==1:
            self.extract(args[0])
    def extract(self,text) -> None:
        trynumber = re.search("^[1-9][0-9]*\s", text)
        if trynumber != None and len(trynumber.regs)!=0 :
            self.number= int(text[:trynumber.regs[0][1]])
            self.name=text[trynumber.regs[0][1]:].replace("bags","").replace("bag","").strip()
        else:
            self.number=0
            self.name=text.strip()
    def __str__(self):
        return [self.number,self.name]
    def __repr__(self):
        return str((self.number,self.name))

data={}
with open ('data7.txt', 'rt') as myfile:
    for myline in myfile:                # For each line, stored as myline,
        line=list(map(lambda x:x.strip(),myline.replace("\n","").replace(".","").strip().split("contain")))
        bags= line[1].split(",")
        data.update({line[0].replace("bags","").replace("bag","").strip() : list(map(lambda x:Bag(x.strip()) ,bags))})

searchstr = "shiny gold"

def search(bag):
    count = 1
    if bag not in data and bag!="shiny gold": return 1
    for s in data[bag]:
        multiplier = s.number
        count += multiplier * search(s.name)
    return count
print(search(searchstr )-1)