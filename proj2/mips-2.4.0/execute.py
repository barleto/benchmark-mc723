#!/usr/bin/python3
import subprocess

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
for line in stdoutdata.split("\n"):
    if line == "##### Final Report: #####":
        flag = True
    if flag:
        report.append(line)
print("\n".join(report))
