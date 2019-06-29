#import SerialModual
import re
import fileContainer
from serialParser import *

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
    
    fileContainer.fileContainer.fileIOStart()
    print(serialParse("@@T:+0201205,H:041291A,PM25:0037:,PM10:00505"))
    


    

       

if __name__ == "__main__":
    main()