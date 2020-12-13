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

search = "shiny gold"
def findinlow(search,data):
    ret=0
    firstbags=set([])
    # bottom up DFS
    for i in list(data.items()):
        #get bags
        for j in i[1]:
            #bag
            if j.name== search: 
                ret+=1
                firstbags.add(i[0])
    return firstbags

print(findinlow(search,data))

def visit(search, startbags, data):
    ret = set()
    ret.update(findinlow(search,data))
    if len(ret)!=0:
        for i in list(ret):
            ret.update(visit(i,"",data))
    return ret

results = visit(search,"",data)
print(results)
print(len(results))





# def visit(search, lst, original):
#     ret=0
#     if type(lst) is Bag: 
#         return 1 if lst.name==search else 0
#     if type(lst) is tuple: 
#         return 1 if lst.name==search else 0
#     if type(lst) is list:
#         for bag in lst:
#             ret+=visit(search,bag,original)
#     if type(lst) is dict:
#         for bag in lst.items():
#             ret+=visit(search,bag,original)
#     return ret

# print(visit("shiny gold", data,data))