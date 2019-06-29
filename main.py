#import SerialModual
import re
from fileContainer import container
from serialParser import *
from datetime import datetime
import schedule
from serialAverager import serialAverager
import time

def main():
   # business logic...
    while True:
        port= input('input port number: ')
        regex= re.compile("[^0-9]")
        regexList= regex.findall(port)

        if regexList == None:
            print('serial connecting...{} port'.format(port))
            break
        else:
            for val in regexList:
                port= port.replace(val, '')
            
            if port != '':
                print('serial connecting...{} port'.format(port))
                break
    now = datetime.now()
    container.fileIOStart("{}-{}-{}".format(now.year, now.month, now.day))
    serialAverager.average()
    
    schedule.every().day.at("00:00").do(fileRefresh)
    schedule.every().minute.at(":00").do(averaging)

    print(serialParse("@@T:+0201205,H:041291A,PM25:0037:,PM10:00505"))
    while True:
        schedule.run_pending()
        time.sleep(1)

def fileRefresh():
    container.fileIOStart("{}-{}-{}".format(now.year, now.month, now.day))

def averaging():
    serialAverager.average()

if __name__ == "__main__":
    main()