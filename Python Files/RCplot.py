
import matplotlib.pyplot as plt
import numpy

path = r'C:\Users\kkb19103\Desktop\LUCENE\lucene4ir8-master\out\RetrievabilityCalculatorList.ret'
rValues = []
zeroCtr = 0
nonZeroCtr = 0

with open(path,'r') as f:
    for line in f:
        parts = line.split(' ',2)
        val = float(parts[1][:-1])
        if (val == 0):
            zeroCtr+=1
        else:
            nonZeroCtr +=1
        rValues.append(val)

    rValues.sort()
    for i in range(5):
        print (str(i) + " Count : " + str(rValues.count(i)))

    N = rValues.__len__() - 1
    i = 1
    num = 0
    den = 0

    for v in rValues:
        num += (2 * i - N) * v
        den += v
        i+=1

print(rValues)
G = num / ((N+1) * den)
summery = "\n\n Zero r values count = " + str(zeroCtr) + \
          "\n Non Zero r Values Count = " + str(nonZeroCtr) + \
          "\n All Values Count = " + str(zeroCtr + nonZeroCtr) + \
          "\n G = " + str(G)
plt.xlabel ("Doc ID" + summery)
plt.ylabel ("Retrievability")


# plt.title("Non Zero R Values\nDocument Retrievability\nBased on document counter" )
# plt.title("All R Values\nDocument Retrievability\nBased on document counter" )
# plt.title("Non Zero R Values\nDocument Retrievability\nBased on Query Weight" )
plt.title("All R Values\nDocument Retrievability\nBased on Query Weight" )

plt.plot(rValues, lw=2 )
plt.show()
print('Done')

