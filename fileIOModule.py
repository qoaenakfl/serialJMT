import os

class fileIOModule():
    def __init__(self, filename, date):
        self.filename= filename
        self.date= date
        with open(os.path.abspath("./")+"/"+filename, "w") as f:
            print(os.path.abspath("./")+"/"+filename)
            f.write("{} starting program\n\n".format(date))
    
    def fileWrite(self, str):
        with open(self.filename, "a") as f:
            f.write(str+"\n")