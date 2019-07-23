
import tkinter.filedialog as dlg
from scipy import stats;

def getMapValues (inFile):
    mapValues = []
    inFile = str(inFile)
    if (inFile.endswith(".perf")):
        inFile = open(inFile,"r")
        for line in inFile:
            if (line.startswith("map")):
                parts = line.split("\t",2)
                currentMap = parts[2].replace("\n", "")
                mapValues.append(float(currentMap))
            if (line.__contains__("all")):
                break
    return mapValues

# Main Function
mapValues = []
#root = dlg.Tk;

for i in range(2):
    chosenFile =  dlg.askopenfilename(title=  "Please Choose File : " + str(i+1))
    mapValues.append(getMapValues(chosenFile))

#root.quit()
if mapValues[0].__sizeof__() > 0 and mapValues[1].__sizeof__() > 0:
    tTest = stats.ttest_rel(mapValues[0],mapValues[1],nan_policy='omit')
    print("MAP List 1 :" , mapValues[0])
    print("MAP List 2 :" , mapValues[1])
    print(tTest)