from fileIOModule import fileIOModule
from datetime import datetime

class fileContainer():
    def fileIOStart(self, day):
        now = datetime.now()
        self.serialFile= fileIOModule('serial{}.txt'.format(day), '{}.txt'.format(day))
        self.averFile= fileIOModule('aver{}.txt'.format(day), '{}.txt'.format(day))
        self.baseFile= fileIOModule('base{}.txt'.format(day), '{}.txt'.format(day))

    def serialWrite(self, serial):
        self.serialFile.fileWrite(serial)
    
    def averWrite(self, aver):
        self.averFile.fileWrite(aver)

    def baseWrite(self, base):
        self.baseFile.fileWrite(base)

container= fileContainer()