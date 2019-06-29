import fileContainer

def serialParse(serial):
    print(serial)
    fileContainer.serialWrite(serial)

    if serial != None and serial != '':
        try:
            serial = serial.replace("@", "")
            serial = serial.replace("--", "-")
            splitText= serial.split(",")

            result= ""

            text= splitText[0].split(":")
            result+= "온도: "
            result+= "{}.{}도\n".format(text[1][0:4], text[1][4:6])

            text= splitText[1].split(":")
            result+= "습도: "
            result+= "{}.{}%\n".format(text[1][1:3], text[1][3:5])

            text= splitText[2].split(":")
            result+= "PM2.5: "
            result+= "{}μg/m3\n".format(text[1][0:4])

            text= splitText[3].split(":")
            result+= "PM10: "
            result+= "{}μg/m3\n".format(text[1][0:4])

            result+= "\n"
            fileContainer.baseWrite(result)
            fileContainer.averWrite(result)

            return result
        
        except Exception as ex:
            print('error for serial', ex)
            return "error serial"