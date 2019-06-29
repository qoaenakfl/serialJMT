class fileIOModule():
    def __init__(self, filename, date):
        self.filename= filename
        self.date= date
        with open(filename, "w") as f:
            f.write("{} starting program".format(date))
    
    def fileWrite(self, str):
        with open(self.filename, "a") as f:
            f.write(str+"\n")
