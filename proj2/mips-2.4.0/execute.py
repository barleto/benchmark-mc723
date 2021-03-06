#!/usr/bin/python3
import subprocess
import sys

sys.argv = sys.argv[1:]

if(len(sys.argv)!=5):
    print("Usage: ./execute.py programName USING_FOWARDING	IS_SUPERESCALAR	isPredictorActive pipeLineSize")
    quit()
else:
    configFileTemplate = """//Here we put all variables and MACROS that control processor configuration

//Cache trace config
string programName = "{}";
bool generateTraces = true;//generate traces for later use in DineroIV

//Data hazard config
#define USING_FOWARDING	{}

//Superscalar config
#define IS_SUPERESCALAR	{}

//Control Hazard config
bool isPredictorActive = {};

//Pipeline Size
int pipeLineSize = {};
""".format(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

    # Open the file with writing permission
    myfile = open("configMIPS.h", 'w')

    # Write a line to the file
    myfile.write(configFileTemplate)

    # Close the file
    myfile.close()


def findError(strOut,err):
    if strOut.find("Error")!=-1 or strOut.find("error")!=-1 or strOut.find("ERROR")!=-1:
        print("ERROR FOUND:")
        print(strOut)
        raise Exception("Error found when building!",err)

stdoutdata = subprocess.getoutput("acsim mips.ac -abi")
findError(stdoutdata,"acsim")
stdoutdata = subprocess.getoutput("make")
findError(stdoutdata,"make")
stdoutdata = subprocess.getoutput("mips-newlib-elf-gcc -specs=archc hello2.c -o hello2.mips")
findError(stdoutdata,"mips-gcc")
stdoutdata = subprocess.getoutput("./mips.x --load=hello2.mips")
findError(stdoutdata,"mips.x")
report = []
flag = False
tracefilename = ""
for line in stdoutdata.split("\n"):
    if line == "##### Final Report: #####":
        flag = True
    if flag:
        report.append(line)
    if line.find("Trace File Name: ")!=-1:
        tracefilename = line[17:]

stdoutdata = subprocess.getoutput("./dineroIV -maxtrace 20 -l1-usize 32K -l1-ubsize 64 -l1-uassoc 2 -l2-usize 256K -l2-ubsize 1024 -l2-uassoc 2 -informat d < {}".format(tracefilename))
findError(stdoutdata,"dinero 1")
stdoutdata = subprocess.getoutput("./dineroIV -maxtrace 20 -l1-usize 64K -l1-ubsize 128 -l1-uassoc 2 -l2-usize 512K -l2-ubsize 1024 -l2-uassoc 2 -informat d < {}".format(tracefilename))
findError(stdoutdata,"dinero 2")
stdoutdata = subprocess.getoutput("./dineroIV -maxtrace 20 -l1-usize 128K -l1-ubsize 128 -l1-uassoc 2 -l2-usize 1024K -l2-ubsize 2048 -l2-uassoc 2 -informat d < {}".format(tracefilename))
findError(stdoutdata,"dinero 3")
stdoutdata = subprocess.getoutput("./dineroIV -maxtrace 20 -l1-usize 128K -l1-ubsize 128 -l1-uassoc 2 -l2-usize 1024K -l2-ubsize 2048 -l2-uassoc 4 -informat d < {}".format(tracefilename))
findError(stdoutdata,"dinero 4")

print("\n".join(report))
