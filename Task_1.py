
''''
Task 1
Darshan Doshi.
'''
import time #for calculating elapsed time
from subprocess import Popen #for executing commands
import sys, os



def main(commands):
    '''
    calls exec_command and calculate time method
    :param commands: list of commands to execute.

    '''
    time = exec_commands(commands)
    calculate_time(time)

def exec_commands(cmd):
    '''

    :param: cmd: list of commands to execute.
    :return: dict: dictionary of  commands as keys and elapsed time as values.
    '''
    dict = {} #create dictionary which stores commands as keys and time elapsed as values
    for c in cmd:
        start=time.time()
        p = Popen(c, shell=True)
        p.poll()
        time_elapsed=time.time()- start
        dict["".join(c)]=time_elapsed
    return dict

def calculate_time(time):
    '''
    calculates average, maximum and minimum time elapsed.
    Sends all these data to generate_report function
    :param time: dictionary of  commands as keys and elapsed time as values.

    '''
    total_time = 0
    for k, v in time.items():
        print(k, v)
        total_time = total_time + v  # calculate total time elapsed

    key_max = max(time.keys(), key=(lambda k: time[k]))  # find the command which took maximum amount of time to execute
    key_min = min(time.keys(), key=(lambda k: time[k]))  # find the command which took minimum amount of time to execute
    avg = total_time / 8  # Calculate average amount of time
    generate_report(time,key_max,key_min,avg,total_time)

def generate_report(time,key_max,key_min,avg,total_time):
    '''
    Displays report of average, maximum and minimum time elapsed.\
    Created report file to store data.
    :param time: dictionary of  commands as keys and elapsed time as values.
    :param key_max: key(command) of maximum value(time)
    :param key_min: key(command) of minimum value(time)
    :param avg: average of of values

    '''
    
    
    print("-------------------------------------------------------")
    print("Total elapsed time  : ",total_time)
    print('Average elapsed time: ', avg)
    print('Maximum elapsed time: ', key_max, time[key_max])
    print('Minimum elapsed time: ', key_min, time[key_min])
    print("-------------------------------------------------------")
    
    path=os.path.dirname(os.path.abspath(sys.argv[0]))
    file = open(path+"/"+"Report.txt", "w")  # store the report in the text file
    file.write("This text file displays the report of time elapsed \n\n\n")
    file.write("Total elapsed time:   "+str(total_time)+"\n")
    file.write('Average elapsed time: ' + str(avg) + "\n")
    file.write('Maximum elapsed time: ' + str(key_max) + "-\t" + str(time[key_max]) + "\n")
    file.write('Minimum elapsed time: ' + str(key_min) + "-\t" + str(time[key_min]))
    file.close()

if __name__ == "__main__":
    commands = [
        ['sleep 3'],
        ['ls -l /'],
        ['find /'],
        ['sleep 4'],
        ['find /usr'],
        ['date'],
        ['sleep 5'],
        ['uptime']

    ]  # commands to execute
    main(commands)
