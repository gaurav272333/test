import webbrowser
import time

print ("This program started on"+time.ctime())

for i in range(1,2):
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=drNtpPVgJ30")
