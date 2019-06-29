from fileContainer import container
from serialAverager import serialAverager

def serialParse(serial):
    print(serial)
    container.serialWrite(serial)

    if serial != None and serial != '':
        try:
            serial = serial.replace("@", "")
            serial = serial.replace("--", "-")
            splitText= serial.split(",")

            result= ""

            text= splitText[0].split(":")
            result+= "온도: "
            t= "{}.{}".format(text[1][0:4], text[1][4:6])
            result+= t+"도\n"

            text= splitText[1].split(":")
            result+= "습도: "
            h= "{}.{}".format(text[1][1:3], text[1][3:5])
            result+= h+"%\n"

            text= splitText[2].split(":")
            result+= "PM2.5: "
            pm25= text[1][0:4]
            result+= pm25+"μg/m3\n"

            text= splitText[3].split(":")
            result+= "PM10: "
            pm10= text[1][0:4]
            result+= pm10+"μg/m3\n"

            result+= "\n"
            container.baseWrite(result)
            serialAverager.sum(t, h, pm25, pm10)

            return result
        
        except Exception as ex:
            print('error for serial', ex)
            return "error serial"