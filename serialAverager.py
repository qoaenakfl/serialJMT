from fileContainer import container

class serialAverager():
    def __init__(self):
        self.t= 0
        self.h= 0
        self.pm25= 0
        self.pm10= 0
        self.cnt= 0
    
    def clear(self):
        self.t= 0
        self.h= 0
        self.pm25= 0
        self.pm10= 0
        self.cnt= 0

    def sum(self, _t, _h, _pm25, _pm10):
        self.t+= float(_t)
        self.h+= float(_h)
        self.pm25+= float(_pm25)
        self.pm10+= float(_pm10)
        self.cnt+= 1

    def average(self):
        print("평균.....")
        result= ""

        if(self.cnt <= 0):
            result+= "온도: 0도\n습도 0%\npm2.5: 0μg/m3\npm10: 0μg/m3\n"
        else:
            result+= "온도: {}도\n습도 {}%\npm2.5: {}μg/m3\npm10: {}μg/m3\n".format(round(self.t/self.cnt, 2),round(self.h/self.cnt, 2),round(self.pm25/self.cnt, 2),round(self.pm10/self.cnt, 2))

        container.averWrite(result)
        self.clear()


serialAverager= serialAverager()