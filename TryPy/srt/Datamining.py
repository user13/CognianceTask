import re

f = open('datamining.log', 'r')
w = open('result', 'w')
patern = re.compile('2014:(\d\d).{0,}HTTP/1.1" (\d\d\d)')
myStr = str(f.read())
resu = patern.findall(myStr)

a = set()
for i in range(len(resu)):
    a.add(resu[i][0])
b = a.copy()

for j in range(len(b)):
    countAll = 0
    countSucc = 0   
    hou = a.pop()
    for i in range(len(resu)):
        if(int(resu[i][0]) == int(hou)):
            countAll += 1
        if(resu[i][0] == hou) and (int(resu[i][1]) == 200):
            countSucc += 1
    w.write('Hour: ' + str(hou) + ". Count of all request: " + str(countAll) + ". Count of success request: " + str(countSucc) + ". Result = " + str(countSucc/countAll*100) + '%\n')
f.close()
w.close()