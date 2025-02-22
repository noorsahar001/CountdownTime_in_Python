#Countdown Timer In Python:

import time
def countdown_timer(seconds) :
    while seconds > 0:
        mins , secs = divmod(seconds, 60)    #mins & secs calculated
        time_format = '{:02d}:{:02d}'.format(mins, secs)      #MM:SS format
        print(time_format, end='\r')
        time.sleep(1)      #delay
        seconds -= 1
    print("00:00 \n Time's up!")

#user_input for timer
total_seconds = int(input("Enter time in second for countdown: "))
countdown_timer(total_seconds)
