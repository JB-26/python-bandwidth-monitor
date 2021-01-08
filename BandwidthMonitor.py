import psutil
import matplotlib.pyplot as plt
import datetime
import os

#lists used for storing data
bytesSnt = []
bytesRec = []
bytesSntX = []
bytesRecY = []

def recordBandwidth():
    '''
    Function for recording internet bandwidth
    '''
    #clears for each run
    del bytesSnt[:]
    del bytesRec[:]
    del bytesSntX[:]
    del bytesRecY[:]
    currentTime = datetime.datetime.now().time().strftime("%H:%M:%S")
    print('Set the time when you want the network monitoring to stop')
    hour = int(input('Enter the hour - '))
    minute = int(input('Enter the minute - '))
    second = int(input('Enter the second - '))
    setTime = datetime.time(hour,minute,second)
    setTime = str(setTime)
    graph = plt
    graph.title(label=f'Bandwidth Usage from {currentTime} to {setTime}')
    graph.xlabel('Bytes Sent')
    graph.ylabel('Bytes Received')
    print(f'Now monitoring network usage - monitoring will stop at {setTime}')


    while currentTime != setTime:
        currentTime = datetime.datetime.now().time().strftime("%H:%M:%S")
        bytesSnt.append(psutil.net_io_counters().bytes_sent / 1000000)
        bytesSntX.append(psutil.net_io_counters().bytes_sent)
        bytesRec.append(psutil.net_io_counters().bytes_recv / 1000000)
        bytesRecY.append(psutil.net_io_counters().bytes_recv)

    print('Monitoring complete!')
    return graph


def showResults(graph):
    '''
    Function for showing the results of the monitoring
    '''
    totalSent = int(sum(bytesSnt) / 1000000)
    totalRec = int(sum(bytesRec) / 1000000)
    graph.plot(bytesSntX, bytesRecY)
    graph.savefig('results')
    print(f'You sent a total of {totalSent} MB')
    print(f'You received a total of {totalRec} MB')
    print(f'The graph has also been saved to the following directory - {os.getcwd()}')
    graph.show()



def main():
    '''
    Function for running the main program
    '''

    dataRecorded = False

    while True:
        print('Welcome to the bandwidth monitor program!')
        print('Please enter a command (the letter in brackets)')
        print('(R)ecord bandwidth')
        print('(S)how results')
        print('(Q)uit')

        choice = input('Enter your choice - ').upper()

        if choice == 'R':
            graph = recordBandwidth()
            dataRecorded = True
        elif choice == 'S':
            if dataRecorded == True:
                showResults(graph=graph)
            else:
                print('No data has been recorded - record some data and then try again!')
        elif choice == 'Q':
            print('Goodbye!')
            break
        else:
            print(f"I don't understand - {choice} - please try again!")

main()