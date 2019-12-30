import os
import glob2
import time

files = glob2.glob("fullvid*")
for file in files:
    os.remove(file)

files = glob2.glob("output*")
for file in files:
    os.remove(file)

link = input("video link :\n")
timestamp = input("timestamp (format HH:MM:SS(.d)) :\n")
endtime = input("endtime (format HH:MM:SS(.d)) :\n")

endtime = endtime.split(':')
endtime.extend(endtime.pop(-1).split('.'))

temptime = timestamp.split(':')
temptime.extend(temptime.pop(-1).split('.'))

for i in range(len(temptime)):
    temptime[i] = int(endtime[i]) - int(temptime[i])

duration = str(temptime[0]) + ':' + str(temptime[1]) + ':' + str(temptime[2]) + '.' + str(temptime[3])

os.system('cmd /c youtube-dl.exe "{0}" -o fullvid.%(ext)s'.format(link))

while len(glob2.glob("fullvid*")) < 1:
    print("stuck")
    time.sleep(1)
    
filename = glob2.glob("fullvid*")[0]

os.system('cmd /c ffmpeg.exe -ss {0} -i {1} -t {2} -async 1 -strict -2 "output.mp4"'.format(timestamp, filename, duration))

files = glob2.glob("fullvid*")
for file in files:
    os.remove(file)
