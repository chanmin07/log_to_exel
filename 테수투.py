import pandas as pd

frame = {}

data = {
    "time" : [],
    "stat" : [],
    "info" : [],
    "user" : []
}

def found(strs,cnt):
    index = strs.find(']')
    #print(strs[1:index].strip())
    tp = ''
    if cnt == 0:
        tp = "time"
    elif cnt == 1:
        tp = "stat"
    elif cnt == 2:
        tp = "info"
    else:
        tp = "user"
    data[tp] = strs[1:index].strip()
    strs = strs[index + 1:].strip()
    if len(strs) != 0:
        found(strs,cnt+1)

file2 = open("log2.txt",'r')
lines = file2.readlines()

for i in range(0, len(lines)):
    strs = lines[i].strip()
    if strs != "":
        #print(strs)
        found(strs,0)
        temp = data.copy()
        frame[i] = temp

#strs = lines[0].strip()
#found(strs,0)

print(frame)
df = pd.DataFrame(frame)
df = df.T
df.to_excel('드디어2.xlsx',index=False)
