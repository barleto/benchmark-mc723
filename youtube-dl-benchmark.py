import sys
import os
import subprocess
import time

# if "-w" in sys.argv:
#     osFlag = "W"
#     initialTime = time.time()
#     subprocess.call(["youtube-dl.exe", "https://www.youtube.com/watch?v=5q9gk5_-4fY", "-o", "arquivoVideo"])
# elif "-u" in sys.argv:
    subprocess.call(["chmod", "a+rx", "./youtube-dl"])
    osFlag = "U"
    initialTime = time.time()
    subprocess.call(["youtube-dl", "https://www.youtube.com/watch?v=5q9gk5_-4fY", "-o", "arquivoVideo"])
# else:
#      print "Please specify your kind of OS with flag -w (windows) or -u (unix base systems)"
#      sys.exit()

endTime = time.time()

print ""
print ""
print "The total execution time is " + str(endTime-initialTime)

if os.path.exists("arquivoVideo.mkv"):
    os.remove("arquivoVideo.mkv")
