import subprocess
stdoutdata = subprocess.getoutput("./runMips.sh")
report = []
flag = False
for line in stdoutdata.split("\n"):
    if line == "##### Final Report: #####":
        flag = True
    if flag:
        report.append(line)
print("\n".join(report))
