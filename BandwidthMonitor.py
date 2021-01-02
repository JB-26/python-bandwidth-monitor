import psutil
import matplotlib.pyplot as plt
import datetime

bytesSnt = []
bytesRec = []
currentTime = datetime.datetime.now().time().strftime("%H:%M:%S")
resGraph = plt
print('Set the time when you want the network monitoring to stop')
hour = int(input('Enter the hour - '))
minute = int(input('Enter the minute - '))
second = int(input('Enter the second - '))
setTime = datetime.time(hour,minute,second)
setTime = str(setTime)
resGraph.title(label=f'Bandwidth Usage from {currentTime} to {setTime}')
resGraph.xlabel('Bytes Sent')
resGraph.ylabel('Bytes Received')
print(f'Now monitoring network usage - monitoring will stop at {setTime}')


while currentTime != setTime:
    currentTime = datetime.datetime.now().time().strftime("%H:%M:%S")
    bytesSnt.append(psutil.net_io_counters().bytes_sent / 1000000)
    bytesRec.append(psutil.net_io_counters().bytes_recv / 1000000)

print('Monitoring complete!')
totalSent = int(sum(bytesSnt) / 1000000)
totalRec = int(sum(bytesRec) / 1000000)
print(f'You sent a total of {totalSent} MB')
print(f'You received a total of {totalRec} MB')
resGraph.plot(bytesSnt, bytesRec)
resGraph.show()
