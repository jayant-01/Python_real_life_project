import time
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec,60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        time_sec -= 1


        print(time_sec)
num=int(input("set your timer in sec :"))
countdown(num)
print("BOOOOOM")


