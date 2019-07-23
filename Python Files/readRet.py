path = r'C:\Users\kkb19103\Desktop\LUCENE\lucene4ir8-master\out\bigram.out'
wPath = r'C:\Users\kkb19103\Desktop\LUCENE\lucene4ir8-master\out\out.ret'

f = open(path,'r')
#w = open(wPath,'w')
i = 0
for line in f:
    parts = line.split(' ',7)
    num = parts[6]
    fl = float(num[:-1])
    if (fl == 0):
        i+=1
   #     w.write(num)

print(i)