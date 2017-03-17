import sys
import os
import subprocess
import time

allFiles = os.listdir("./zips")
results = []
print "numer of files " + str(len(allFiles))
if not os.path.exists("temp-unzipped"):
    os.makedirs("temp-unzipped")

file = "arquivoExemplo.zip"
for i in range(0, 10):
    print i
    if os.path.exists("temp-unzipped/"+str(file)):
        subprocess.call(["rm", "-fr", "temp-unzipped/"+str(file)])
    initialTime = time.time()
    subprocess.call(["unzip", "./zips/" + str(file), "-d", "temp-unzipped/" + str(file)])
    endTime = time.time()
    results.append(endTime - initialTime)

for result in results:
    print result

print "##################################"

mean = 0
for result in results:
    mean += result
mean /= len(results)

stdDeviation = 0
for result in results:
    stdDeviation += (result - mean)**2
stdDeviation /= (len(results)-1)
stdDeviation = stdDeviation**0.5

stdError = stdDeviation/(10**0.5)
print "mean : " + str(mean)
print "standart Deviation : " + str(stdDeviation)
print "standart error: " + str(stdError)
