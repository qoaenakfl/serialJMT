import fileIOModule
from datetime import datetime

class fileContainer():
    def fileIOStart(self):
        now = datetime.now()
        self.serialFile= fileIOModule.fileIOModule('serial{}-{}-{}.txt'.format(now.year, now.month, now.day), '{}-{}-{}.txt'.format(now.year, now.month, now.day))
        self.baseFile= fileIOModule.fileIOModule('base{}-{}-{}.txt'.format(now.year, now.month, now.day), '{}-{}-{}.txt'.format(now.year, now.month, now.day))
        self.averFile= fileIOModule.fileIOModule('aver{}-{}-{}.txt'.format(now.year, now.month, now.day), '{}-{}-{}.txt'.format(now.year, now.month, now.day))

    def serialWrite(self, serial):
        self.serialFile.fileWrite(serial)
    
    def averWrite(self, aver):
        self.averFile.fileWrite(aver)

    def baseWrite(self, base):
        self.baseFile.fileWrite(base)